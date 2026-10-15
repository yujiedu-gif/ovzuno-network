# Cloudflare Pages deployment

Connect the same GitHub repository to four Cloudflare Pages projects.

| Project | Production domain | Build command | Output directory | Build watch paths |
| --- | --- | --- | --- | --- |
| `ovzuno-main` | `ovzuno.com` | `./scripts/build-site.sh root` | `dist/root` | `sites/root/*,themes/ovzuno/*,scripts/*` |
| `ovzuno-aiinfra` | `aiinfra.ovzuno.com` | `./scripts/build-site.sh aiinfra` | `dist/aiinfra` | `sites/aiinfra/*,themes/ovzuno/*,scripts/*` |
| `ovzuno-crypto` | `crypto.ovzuno.com` | `./scripts/build-site.sh crypto` | `dist/crypto` | `sites/crypto/*,themes/ovzuno/*,scripts/*` |
| `ovzuno-workplace` | `workplace.ovzuno.com` | `./scripts/build-site.sh workplace` | `dist/workplace` | `sites/workplace/*,themes/ovzuno/*,scripts/*` |

Set `HUGO_VERSION=0.146.0` for every project. The production branch is `main`.

Add each custom domain from the Pages project's **Custom domains** screen rather than creating only a manual CNAME. Redirect `www.ovzuno.com/*` to `https://ovzuno.com/$1` with an account-level redirect rule.

Before deployment, confirm that `dist/<site>/_headers` contains the pre-launch `X-Robots-Tag`. Do not submit any property to Search Console during pre-launch.

