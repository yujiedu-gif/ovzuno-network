# Publication launch checklist

A publication remains `noindex` until every item is true:

- At least three coherent topic clusters exist.
- Each cluster contains at least four substantial articles.
- At least 12 articles have passed source and factual review.
- About, Editorial Standards, Publication Disclosure, Contact, Privacy, and Terms are complete.
- Canonical URLs and JSON-LD match the production host.
- No placeholder, thin, duplicated, or future-dated content remains.

At launch:

1. Change `params.prelaunch` to `false`.
2. Remove the wildcard `X-Robots-Tag` from `static/_headers`.
3. Remove `sitemap` from `disableKinds` and enable the production sitemap templates.
4. Build and inspect every generated host.
5. Deploy, create the Google Search Console domain property, and submit each host's sitemap.
6. Check live canonical, robots, JSON-LD, and URL Inspection results.

