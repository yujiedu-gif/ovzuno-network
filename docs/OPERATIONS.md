# OvZuno publishing network: operations

Source of truth: this repository's remote main branch. Production: https://ovzuno.com.

Management console source: https://github.com/yujiedu-gif/website-admin (private).
Planned console: https://admin.ovzuno.com (use only after its acceptance report says deployed).

## Content

Use the private console to save drafts, check the exact source version, and request publication. Saving does not deploy. Publishing creates a GitHub PR and observes existing branch protection. A failed deployment is not a successful publication.

## Recovery

Clone main into a new directory. Read the pinned build configuration in README.md. Obtain secrets separately from the credential owner. Do not copy an old computer's virtual environments. Restore encrypted operational snapshots into a temporary directory with website-admin/scripts/backup.py; validate hashes and databases before selecting the working state.

Restore public content with a new commit. Do not reset or force-push production history.

For OvZuno, preserve prelaunch robots/noindex settings until the editorial launch gate is separately completed.
