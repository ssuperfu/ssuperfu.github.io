#!/usr/bin/env bash
set -euo pipefail
docker run --rm \
  -v /home/ubuntu/npm/data/mypage-acme:/var/www/acme \
  -v /home/ubuntu/npm/letsencrypt/mypage:/etc/letsencrypt \
  certbot/certbot:v5.4.0 renew --quiet
docker exec npm_app nginx -t
docker exec npm_app nginx -s reload
