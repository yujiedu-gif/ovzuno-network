#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "$0")/.." && pwd)"
for site in root aiinfra crypto workplace; do
  "$repo_dir/scripts/build-site.sh" "$site"
done
"$repo_dir/scripts/check-prelaunch.sh"
python3 "$repo_dir/scripts/check-crypto-indexing.py"
