#!/usr/bin/env bash
set -euo pipefail
cd /opt/intro-site/source
if ! dig +short intro.archois.cn A @1.1.1.1 | sort -u | grep -qx '124.222.211.146'; then
    echo '请先把 intro.archois.cn 的 DNS A 记录指向 124.222.211.146，再运行本脚本。' >&2
    exit 1
fi
sudo mkdir -p /home/ubuntu/npm/data/mypage-acme /home/ubuntu/npm/letsencrypt/mypage
sudo docker run --rm \
  -v /home/ubuntu/npm/data/mypage-acme:/var/www/acme \
  -v /home/ubuntu/npm/letsencrypt/mypage:/etc/letsencrypt \
  certbot/certbot:v5.4.0 certonly --webroot -w /var/www/acme \
  --non-interactive --agree-tos --register-unsafely-without-email -d intro.archois.cn
sudo cp /home/ubuntu/npm/data/nginx/custom/mypage.conf /home/ubuntu/npm/data/nginx/custom/mypage.conf.before-https
sudo cp deploy/proxy-https.conf /home/ubuntu/npm/data/nginx/custom/mypage.conf
if ! sudo docker exec npm_app nginx -t; then
  sudo cp /home/ubuntu/npm/data/nginx/custom/mypage.conf.before-https /home/ubuntu/npm/data/nginx/custom/mypage.conf
  exit 1
fi
sudo docker exec npm_app nginx -s reload
sed -i 's|^SITE_URL=.*|SITE_URL=https://intro.archois.cn|' .env
sudo docker compose build
sudo docker compose up -d
sudo docker exec npm_app nginx -s reload
sudo cp deploy/renew-certificate.sh /usr/local/sbin/mypage-renew-certificate
sudo chmod 755 /usr/local/sbin/mypage-renew-certificate
sudo cp deploy/mypage-certificate.service deploy/mypage-certificate.timer /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now mypage-certificate.timer
curl --resolve intro.archois.cn:443:124.222.211.146 -fsSI https://intro.archois.cn/
