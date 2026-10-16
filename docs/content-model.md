# Content model

Articles live under `sites/<publication>/content/articles/` and start as drafts.

```yaml
---
title: ""
description: ""
date: 2027-01-01T09:00:00Z
lastmod:
content_type: "explainer"
primary_keyword: ""
owned_question: ""
jurisdiction:
risk_level: "medium"
topics: []
tags: []
author: "editorial_team"
sources: []
partner:
disclosure:
draft: true
---
```

Allowed `content_type` values are `definition`, `explainer`, `guide`, `comparison`, `analysis`, and `partner-insight`.

Every article owns one `owned_question`. `primary_keyword` records the approved search phrase; it does not authorize keyword stuffing. Legal, tax, compliance, licensing, and product-availability pages require a non-empty `jurisdiction`. `risk_level` is `low`, `medium`, or `high` and controls review depth.

Only set `lastmod` after a substantive, verified update. Partner-supported work requires both `partner` and a plain-language `disclosure`. One article has one canonical publication; related publications link to it rather than republishing it.

Each source may set `sponsored: true`. Ordinary editorial citations use `rel="noopener"`; sponsored or materially influenced sources use `rel="sponsored nofollow noopener"`.
