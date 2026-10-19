#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "$0")/.." && pwd)"
failed=0

for site in root aiinfra crypto workplace; do
  output="$repo_dir/dist/$site"
  config="$repo_dir/sites/$site/hugo.yaml"
  if [[ ! -d "$output" ]]; then
    echo "Missing build output: $output" >&2
    failed=1
    continue
  fi

  if grep -q 'prelaunch: true' "$config"; then
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
  else
    if find "$output" -name '*.html' -type f -print0 | xargs -0 grep -l 'name=robots content="noindex,follow,noarchive"' | grep -q .; then
      echo "Published site still contains noindex meta: $site" >&2
      failed=1
    fi
    if grep -qi 'X-Robots-Tag:.*noindex' "$output/_headers"; then
      echo "Published site still contains noindex header: $site" >&2
      failed=1
    fi
    if [[ ! -s "$output/sitemap.xml" ]]; then
      echo "Published site is missing sitemap.xml: $site" >&2
      failed=1
    fi
    if ! grep -q "Sitemap: https://$site.ovzuno.com/sitemap.xml" "$output/robots.txt" && [[ "$site" != "root" ]]; then
      echo "Published site robots.txt is missing its sitemap: $site" >&2
      failed=1
    fi
  fi
done

if [[ "$failed" -ne 0 ]]; then
  exit 1
fi

echo "Indexing-state checks passed for all four sites."
