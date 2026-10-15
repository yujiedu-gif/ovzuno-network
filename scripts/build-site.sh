#!/usr/bin/env bash
set -euo pipefail

site="${1:-}"
case "$site" in
  root|aiinfra|crypto|workplace) ;;
  *) echo "Usage: $0 {root|aiinfra|crypto|workplace}" >&2; exit 2 ;;
esac

repo_dir="$(cd "$(dirname "$0")/.." && pwd)"
hugo \
  --source "$repo_dir/sites/$site" \
  --themesDir "$repo_dir/themes" \
  --destination "$repo_dir/dist/$site" \
  --cleanDestinationDir \
  --minify \
  --cacheDir "$repo_dir/.cache/hugo/$site"

