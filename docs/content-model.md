# Content model

Articles live under `sites/<publication>/content/articles/` and start as drafts.

```yaml
---
title: ""
description: ""
date: 2027-01-01T09:00:00Z
lastmod:
content_type: "explainer"
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

Only set `lastmod` after a substantive, verified update. Partner-supported work requires both `partner` and a plain-language `disclosure`. One article has one canonical publication; related publications link to it rather than republishing it.

