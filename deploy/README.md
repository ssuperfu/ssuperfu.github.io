# 云服务器部署

日常网页更新采用 GitHub `main` 手动触发部署，推送后通知 Codex 拉取；服务器不定时检查。详见 [部署说明](AUTO-DEPLOY.md)。以下手动构建命令仅用于维护；服务器 `source` 目录不会自动同步 GitHub 源码。

源码目录：`/opt/intro-site/source`。静态页面由 Jekyll 在镜像构建阶段生成，运行时仅运行 Nginx。

现有服务器用 Nginx Proxy Manager 占用 80/443；本项目加入已有 `npm_default` 网络，代理目标为 `personal-homepage:80`。本地诊断入口为 `127.0.0.1:8090`。

## 构建与更新

将更新的源码同步到服务器目录，保留服务器 `.env`，然后执行：

```sh
cd /opt/intro-site/source
sudo docker compose build
sudo docker compose up -d
curl -I http://127.0.0.1:8090/
sudo docker compose ps
```

`.env` 中的 `SITE_URL` 必须是最终访问地址，例如 `SITE_URL=https://intro.archois.cn`。修改后需重新构建镜像，才能更新 canonical 和 sitemap URL。

## 回滚

更新前保留旧镜像：

```sh
sudo docker tag personal-homepage:local personal-homepage:rollback
```

需要回滚时：

```sh
sudo docker tag personal-homepage:rollback personal-homepage:local
sudo docker compose up -d --no-build
```

## 域名与 HTTPS

将域名 A 记录指向 `124.222.211.146`；若原配置为 CNAME，先删除冲突记录。检查是否存在仍指向其他主机的 AAAA 记录。
域名解析生效后，通过现有反向代理接入主页并申请 HTTPS 证书。原 GitHub Pages 可保留，确认新站可访问后再决定是否关闭。

Google Scholar 引用统计仍通过 GitHub Actions 和 jsDelivr 获取；迁移静态托管不会自动迁移该数据更新任务。

此服务器的代理配置为 `/home/ubuntu/npm/data/nginx/custom/mypage.conf`，由已有 `http.conf` 引入。
DNS 切换后，在服务器运行以下命令完成证书签发、HTTPS 跳转和自动续期：

```sh
cd /opt/intro-site/source
bash deploy/enable-https.sh
```

证书续期由 `mypage-certificate.timer` 每天检查两次，可用 `systemctl list-timers mypage-certificate.timer` 查看。
服务器构建时 `.env` 中可设置 `DEBIAN_MIRROR=mirrors.cloud.tencent.com` 使用腾讯云软件源。
