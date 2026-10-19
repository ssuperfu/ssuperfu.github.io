#!/usr/bin/env python3
"""Poll main and deploy immutable GitHub snapshots with a tested image rollback."""
import datetime
import fcntl
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request

ROOT = Path('/opt/intro-site')
AUTO = ROOT / 'automation'
SOURCE = ROOT / 'source'
STATE = AUTO / 'last-deployed.json'
REPO = 'ssuperfu/ssuperfu.github.io'
HTTP = urllib.request.build_opener(urllib.request.ProxyHandler({}))

def log(message):
    print(f'{datetime.datetime.now(datetime.timezone.utc).isoformat()} {message}', flush=True)

def run(*args, capture=False, check=True):
    result = subprocess.run(args, check=check, text=True,
                            stdout=subprocess.PIPE if capture else None)
    return result.stdout.strip() if capture else result.returncode

def fetch(url):
    request = urllib.request.Request(url, headers={'User-Agent': 'personal-homepage-deployer',
                                                  'Accept': 'application/vnd.github+json'})
    with HTTP.open(request, timeout=45) as response:
        return response.read()

def smoke_container(name):
    for attempt in range(15):
        if run('docker', 'exec', name, 'sh', '-c',
               'wget -q -O /dev/null http://127.0.0.1/ && '
               'wget -q -O /dev/null http://127.0.0.1/zh/ && '
               'wget -q -O /dev/null http://127.0.0.1/assets/css/main.css', check=False) == 0:
            return
        time.sleep(2)
    raise RuntimeError(f'Container smoke check failed: {name}')

def compose_up():
    run('docker', 'compose', '--project-name', 'source', '--project-directory', str(SOURCE),
        '-f', str(SOURCE / 'compose.yaml'), 'up', '-d', '--no-build', 'homepage')

def main():
    AUTO.mkdir(parents=True, exist_ok=True)
    with (AUTO / 'deploy.lock').open('w') as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            log('Another deployment is running; skipping.')
            return
        revision = json.loads(fetch(f'https://api.github.com/repos/{REPO}/git/ref/heads/main'))['object']['sha']
        if not re.fullmatch(r'[0-9a-f]{40}', revision):
            raise RuntimeError('Unexpected GitHub revision')
        previous = json.loads(STATE.read_text()) if STATE.exists() else {}
        bootstrap = '--bootstrap' in sys.argv
        if bootstrap and previous:
            raise RuntimeError('Bootstrap is only allowed before the first successful deployment')
        if previous.get('commit') == revision:
            log(f'No change on main ({revision[:12]}).')
            return
        release = ROOT / 'releases' / revision
        release.parent.mkdir(parents=True, exist_ok=True)
        # Only a completed extraction becomes a build context.
        with tempfile.TemporaryDirectory(prefix='extract-', dir=release.parent) as temp:
            context = Path(temp) / 'source'
            context.mkdir()
            if bootstrap:
                shutil.copytree(SOURCE, context, dirs_exist_ok=True,
                                ignore=shutil.ignore_patterns('.git', '.env', '_site', '.bundle', '.DS_Store'))
                log('Bootstrapping from the currently deployed source, preserving unpublished local edits.')
            else:
                archive = Path(temp) / 'source.tar.gz'
                log(f'Downloading main at {revision}.')
                archive.write_bytes(fetch(f'https://codeload.github.com/{REPO}/tar.gz/{revision}'))
                run('tar', '-xzf', str(archive), '--strip-components=1', '-C', str(context), '--no-same-owner')
            # Migration files may not yet have been committed. Supply only missing build infrastructure.
            for name in ('Dockerfile', '.dockerignore', 'deploy/nginx.conf'):
                target = context / name
                if not target.exists():
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(AUTO / 'template' / name, target)
            if release.exists():
                shutil.rmtree(release)
            shutil.move(str(context), release)
        settings = {}
        for line in (SOURCE / '.env').read_text().splitlines():
            if line.strip() and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                settings[key] = value
        candidate = 'personal-homepage:' + ('bootstrap-' if bootstrap else '') + revision
        command = ['docker', 'build', '--tag', candidate]
        for key in ('SITE_URL', 'DEBIAN_MIRROR', 'GEM_MIRROR'):
            if key in settings:
                command += ['--build-arg', f'{key}={settings[key]}']
        command += [str(release)]
        log(f'Building {candidate}.')
        run(*command)
        test_name = 'mypage-candidate-' + revision[:12]
        try:
            run('docker', 'run', '-d', '--name', test_name, '--network', 'npm_default', candidate)
            smoke_container(test_name)
        finally:
            run('docker', 'rm', '-f', test_name, check=False)
        previous_image = run('docker', 'inspect', '--format', '{{.Image}}', 'source-homepage-1', capture=True)
        run('docker', 'tag', previous_image, 'personal-homepage:rollback')
        try:
            run('docker', 'tag', candidate, 'personal-homepage:local')
            compose_up()
            smoke_container('source-homepage-1')
            # Docker DNS is resolved dynamically by the existing proxy. Reload to switch immediately.
            run('docker', 'exec', 'npm_app', 'nginx', '-t')
            run('docker', 'exec', 'npm_app', 'nginx', '-s', 'reload')
            for path in ('/', '/zh/', '/assets/css/main.css'):
                # Verify the actual TLS vhost without depending on stale recursive DNS.
                run('curl', '--fail', '--silent', '--show-error', '--max-time', '20',
                    '--resolve', 'intro.archois.cn:443:127.0.0.1',
                    '--output', '/dev/null', 'https://intro.archois.cn' + path)
        except BaseException:
            log(f'Deployment failed; restoring {previous_image}.')
            run('docker', 'tag', previous_image, 'personal-homepage:local')
            compose_up()
            smoke_container('source-homepage-1')
            run('docker', 'exec', 'npm_app', 'nginx', '-s', 'reload')
            raise
        record = {'commit': revision, 'image': candidate, 'source': str(release),
                  'bootstrap': bootstrap, 'deployed_at': datetime.datetime.now(datetime.timezone.utc).isoformat()}
        pending = STATE.with_suffix('.tmp')
        pending.write_text(json.dumps(record, indent=2) + '\n')
        pending.replace(STATE)
        log(f'Deployed {revision} successfully; rollback image retained.')
        # Keep five source snapshots and their image tags; rollback/local tags are never removed.
        old = sorted((ROOT / 'releases').iterdir(), key=lambda p: p.stat().st_mtime, reverse=True)
        for directory in old[5:]:
            if directory.is_dir() and re.fullmatch(r'[0-9a-f]{40}', directory.name):
                shutil.rmtree(directory)
        kept = {p.name for p in old[:5]}
        tags = run('docker', 'image', 'ls', '--filter', 'reference=personal-homepage:*',
                   '--format', '{{.Tag}}', capture=True).splitlines()
        for tag in tags:
            revision_tag = tag.removeprefix('bootstrap-')
            if re.fullmatch(r'[0-9a-f]{40}', revision_tag) and revision_tag not in kept:
                run('docker', 'image', 'rm', 'personal-homepage:' + tag, check=False)

if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        log(f'ERROR: {exc}')
        sys.exit(1)
