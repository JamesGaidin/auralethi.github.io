# Current State / Conversation Handoff

**As of 2026-10-09; verify live state each time you resume.**

## Confirmed by GitHub repository inspection
- Public repository `JamesGaidin/auralethi.github.io`, default branch `main`.
- Existing root files include `index.html`, `style.css`, `README.md`, `CNAME`; directories include `about`, `research`, `systems`, `get-involved`, `shared`.
- `CNAME` contains `auralethi.org`.
- Existing site is manually maintained static HTML/CSS, with some animation code; it currently foregrounds AI safety research.
- Working branch `feature/auralethi-homecoming` exists, based on `2959d89014` before these documentation additions.
- No verified .NET / Blazor solution at the repository root as of inspection.
- GitHub connector has read/write access. This **does not guarantee** GitHub Pages admin configuration or automatic deployment access.

## Reported by founder, not independently verified
- Domain believed registered through Squarespace for three years, expiring in 2027.
- Google handled email previously; current mail/DNS status uncertain.
- Budget very limited; no new paid hosting.
- Desired near-term release: weekend October 10–11, 2026.
- Dedicated servers and Jix infrastructure are later-stage goals.

## Work performed
- 2026-10-09: Created project documentation on development branch. This is **not** a redesign launch.
- A weekly Friday morning ChatGPT automation was configured to review verifiable progress and prepare **unpublished** drafts for approval. It is outside the repository; actual delivery and GitHub PR creation are not yet tested. It must not imply auto-publishing.

## Not yet done / verify
- Create redesigned home and supporting pages; capture baseline and test.
- Confirm real GitHub Pages publication source and deployment behavior before merging.
- Confirm registrar, expiry, DNS nameservers, MX records and email provider through independent account or DNS checks; never modify DNS casually.
- Establish draft-news format and approval/publishing mechanism; do not assume scheduled automation can run arbitrary scripts or automatically merge.
- Future Visual Studio / Blazor solution strategy; consider whether a static-first implementation is preferable for first launch.

## Handoff protocol
On return: inspect `AGENTS.md` → project docs → current Git tree/history → open branches/PRs → live website. Update this page with dated **observed** facts; mark uncertain claims as such. Never represent a plan as an accomplishment.
