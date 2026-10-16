# OvZuno publishing network

- Production origin: https://ovzuno.com. Read README.md and docs/OPERATIONS.md before editing or publishing.
- This repository contains only this website/network. Never read another project's secrets or write content into another repository without an explicit task.
- Preserve existing URLs, metadata, editorial rules and deployment settings.
- Drafts created by website-admin live in its private repository until publication is requested.
- The admin_publication_id metadata field is written by the management publishing job. The layout emits it solely to verify the deployed version.
- Production edits must pass the repository build. Never bypass branch protection.
- Runtime state, secrets and caches are not interchangeable with the Git history. Follow the recovery guide before replacing them.
