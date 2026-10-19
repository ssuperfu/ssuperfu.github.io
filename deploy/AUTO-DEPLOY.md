# GitHub 手动触发部署

服务器不再定时检查 GitHub，`mypage-deploy.timer` 已停止并禁用。

以后修改网页并推送到 `ssuperfu/ssuperfu.github.io` 的 `main` 分支后，告诉 Codex 拉取并部署；也可以自行执行下面的部署命令。推送本身不会触发服务器更新。

首次启动以当前线上源码建立基线，保留已发布但尚未提交的导航栏修改；下一次 `main` 更新时，以 GitHub 上该提交的完整内容为准。

## 服务器管理

```sh
# 查看部署日志
sudo journalctl -u mypage-deploy.service -n 100 --no-pager

# 立即检查 main 并在有更新时部署
sudo systemctl start mypage-deploy.service

# 查看最近成功版本
sudo cat /opt/intro-site/automation/last-deployed.json

```

## 部署和回滚行为

- 从 GitHub 公共 API 读取完整提交 SHA，再从官方 codeload 接口下载该 SHA 的源码。
- 构建时网站继续提供旧版本。候选镜像在临时容器通过检查后才切换正式容器。
- 正式容器和 HTTPS 检查失败时，自动恢复前一个镜像；失败提交不标记成功，可再次手动触发重试。
- 保留最近五份源码快照及镜像标签，并保留 `personal-homepage:rollback`。Docker 构建缓存由服务器单独维护。
- 拉取源码或构建失败时，线上版本继续运行。日志保存在 systemd journal。

紧急手动回滚：

```sh
sudo systemctl stop mypage-deploy.service
sudo docker tag personal-homepage:rollback personal-homepage:local
cd /opt/intro-site/source
sudo docker compose -p source up -d --no-build homepage
sudo docker exec npm_app nginx -s reload
```

源码快照位于 `/opt/intro-site/releases/<提交SHA>`，运行参数和 Compose 配置位于 `/opt/intro-site/source`，部署脚本及缺失构建文件的兼容模板位于 `/opt/intro-site/automation`。

`/opt/intro-site/source` 保留初次部署源码，不会随着部署改写。日常更新通过 GitHub 推送后手动触发部署；直接在此目录重新构建会使用该目录的源码。服务器 `.env`、域名代理、HTTPS 续期服务保持独立管理。

项目还未提交 Docker 配置时，服务器会补齐缺失的 Dockerfile、.dockerignore 和 Nginx 配置；提交这些文件后，镜像构建会采用仓库中的版本。运行端口、域名及服务器配置变更需另外部署。
