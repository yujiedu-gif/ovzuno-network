#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "$0")/.." && pwd)"
failed=0

for site in root aiinfra crypto workplace; do
  output="$repo_dir/dist/$site"
  if [[ ! -d "$output" ]]; then
    echo "Missing build output: $output" >&2
    failed=1
    continue
  fi

  while IFS= read -r -d '' file; do
    if ! grep -q 'name=robots content="noindex,follow,noarchive"' "$file"; then
      echo "Missing pre-launch robots meta: $file" >&2
      failed=1
    fi
  done < <(find "$output" -name '*.html' -type f -print0)

  if [[ -e "$output/sitemap.xml" || -e "$output/index.xml" ]]; then
    echo "Pre-launch sitemap or RSS unexpectedly generated for $site" >&2
    failed=1
  fi

  if ! grep -q 'X-Robots-Tag: noindex, follow, noarchive' "$output/_headers"; then
    echo "Missing X-Robots-Tag for $site" >&2
    failed=1
  fi
done

if [[ "$failed" -ne 0 ]]; then
  exit 1
fi

echo "Pre-launch checks passed for all four sites."

