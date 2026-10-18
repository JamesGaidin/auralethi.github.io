# Public page status metadata

Every visitor-facing HTML page declares one status in the HTML head:

`<meta name="auralethi:status" content="active">`

Vocabulary:
- `active`: This page is presently published and usable. **It does not claim every service mentioned on the page is operated by Auralethi, open for enrollment, or already implemented.**
- `research`: This page describes a research program or research topic; publication does not certify the underlying technology.
- `development`: The described implementation is under development; not necessarily public or deployable.
- `future`: A page whose primary subject is a planned, not yet available initiative. No whole-page `future` page presently exists; future projects on Projects retain explicit visible future labels.

Status describes the page's primary purpose, not every linked destination. The Projects index is `active` as an index even though it contains future initiatives. The News page is `active` because the dated updates are already published, and a call to follow along does not mean it is in development. Likewise Free to Meet and Safe to Become describe accessible *published navigation pages*, not a promise of access to third-party services.

Jix's World generator should take status from the declared meta tag, never a nearby CSS class or a third-party resource card. If the value is absent or unknown, fail closed and report a site-content issue. Preserve visible labels about actual capabilities and verify rendered content separately.

These status claims are editorial metadata, not independent evidence that systems have passed tests.
