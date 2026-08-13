#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"

# 必须用 Homebrew 的 ruby 对应的 bundle，否则 conda 等环境里的 `bundle` 会把包装到别的 Ruby 下，
# 导致 `bundle exec jekyll` 找不到 jekyll。
# Ruby 3.3 与 github-pages 自带的 Jekyll 3.9 在标准库 Logger 上存在兼容性问题，优先使用 3.1/3.2。
BUNDLE=""
for candidate in \
  /opt/homebrew/opt/ruby@3.1/bin/bundle \
  /usr/local/opt/ruby@3.1/bin/bundle \
  /opt/homebrew/opt/ruby@3.2/bin/bundle \
  /usr/local/opt/ruby@3.2/bin/bundle \
  /opt/homebrew/opt/ruby@3.3/bin/bundle \
  /usr/local/opt/ruby@3.3/bin/bundle \
  /opt/homebrew/opt/ruby/bin/bundle \
  /usr/local/opt/ruby/bin/bundle; do
  if [ -x "$candidate" ]; then
    BUNDLE="$candidate"
    break
  fi
done

if [ -z "$BUNDLE" ]; then
  echo "未找到 Homebrew 的 bundle，请先执行: brew install ruby@3.1" >&2
  exit 1
fi

export PATH="$(dirname "$BUNDLE"):$PATH"

if ! "$BUNDLE" check >/dev/null 2>&1; then
  echo "正在为 $(dirname "$BUNDLE")/ruby 安装 Gemfile 依赖…"
  "$BUNDLE" install
fi

exec "$BUNDLE" exec jekyll liveserve
