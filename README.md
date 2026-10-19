# OvZuno publishing network

OvZuno is a B2B technology publishing network built as four Hugo sites from one repository. Crypto is the first live publication; the parent publisher, AI Infrastructure, and Workplace remain in pre-launch mode.

## Sites

| Site | Canonical URL | Cloudflare Pages project | Indexing state |
| --- | --- | --- | --- |
| Parent publisher | `https://ovzuno.com/` | `ovzuno-main` | Pre-launch (`noindex`) |
| AI Infrastructure | `https://aiinfra.ovzuno.com/` | `ovzuno-aiinfra` | Pre-launch (`noindex`) |
| Crypto | `https://crypto.ovzuno.com/` | `ovzuno-crypto` | Published |
| Workplace | `https://workplace.ovzuno.com/` | `ovzuno-workplace` | Pre-launch (`noindex`) |

Pre-launch sites emit `noindex,follow,noarchive`, serve the matching `X-Robots-Tag`, and do not generate a sitemap. The Crypto publication emits indexable HTML, a public `robots.txt`, and its own sitemap.

## Local development

Hugo Extended 0.146 or newer is recommended.

```sh
./scripts/build-all.sh
hugo server --source sites/root --themesDir ../../themes --disableFastRender
```

Replace `root` with `aiinfra`, `crypto`, or `workplace` to preview another publication.

## Cloudflare Pages

Create four Pages projects from this repository. Use the build command and output directory listed in [Cloudflare deployment](docs/cloudflare-pages.md).

## Publishing later

Do not remove pre-launch controls until a publication meets the editorial launch gate. The complete checklist is in [Launch checklist](docs/launch-checklist.md). Articles use the contract documented in [Content model](docs/content-model.md).

## Brand files

Production SVG logos, favicon source, lockups, and the two unused exploration concepts are stored in `themes/ovzuno/static/brand/`. See [Brand guide](/brand-guide/) on the parent site for usage rules.
