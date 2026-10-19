FROM ruby:3.3-slim-bookworm AS build
ARG DEBIAN_MIRROR=deb.debian.org
RUN sed -i "s|deb.debian.org|${DEBIAN_MIRROR}|g" /etc/apt/sources.list.d/debian.sources && apt-get update && apt-get install -y --no-install-recommends build-essential git libcurl4-openssl-dev pkg-config && rm -rf /var/lib/apt/lists/*
WORKDIR /src
COPY Gemfile Gemfile.lock ./
ARG GEM_MIRROR=https://rubygems.org
RUN gem install bundler -v 2.5.16 --no-document && bundle config set mirror.https://rubygems.org "$GEM_MIRROR" && bundle install --jobs 2
COPY . .
ARG SITE_URL=http://124.222.211.146
ENV JEKYLL_ENV=production
RUN ruby -ryaml -e 'File.write("/tmp/production.yml", {"url"=>ARGV[0], "baseurl"=>"", "exclude"=>(YAML.load_file("_config.yml").fetch("exclude", []) + %w[Dockerfile compose.yaml deploy Gemfile.lock run_server.sh run_server_docker.sh]).uniq}.to_yaml)' "$SITE_URL" \
    && bundle exec jekyll build --config _config.yml,/tmp/production.yml --destination /output \
    && rm -f /output/CNAME /output/run_server.sh /output/run_server_docker.sh
FROM nginx:stable-alpine
COPY deploy/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /output/ /usr/share/nginx/html/
HEALTHCHECK --interval=30s --timeout=3s CMD wget -q -O /dev/null http://127.0.0.1/ || exit 1
