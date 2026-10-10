# Project Governance and Public-Disclosure Rules

## Authority and release policy
- James is project owner and final authority for public-facing claims and releases.
- AI collaborators may research, draft, code, test, document, and prepare branches/PRs.
- **Do not commit changes straight to `main`, merge, or intentionally trigger a live deployment without James's explicit approval for that release.**
- Prefer reversible, incremental commits on `feature/*` branches. Preserve existing production content until replacement is approved.

## Truthfulness and disclosure
- Every service/project description distinguishes **Active / In Development / Research / Future Vision** based on evidence, not enthusiasm.
- No invented results, capabilities, partnerships, program availability, funding, impact metrics, or dates.
- Work from private repos and conversations is **not automatically public**. Use only specifically approved disclosures; redact security-sensitive details, internal identities, and protected personal information.
- Cite public sources where relevant; if a draft lacks verification, label it pending.
- Progress reports describe what happened, why it matters, what's next, and any meaningful limitations or failed tests.

## Accessibility, agency, and privacy
- Respect WCAG-oriented accessibility practices: semantics, keyboard navigation, contrast, descriptive links, screen reader usability, responsive layout, reduced motion.
- Splash intro must be skippable or nonblocking; Jix must always be optional.
- No dark patterns or coercive intake; visitors shouldn't have to disclose private information to browse.
- No analytics/tracking, forms, or third-party widgets without assessing privacy and costs first.

## Change records
For significant changes, record: date, rationale, files impacted, test evidence, potential risks, deployment status, and rollback path. When updating claims, reference the actual evidence and approval.

## Data classification
All content committed here is **public by default**, including docs, commit messages, branches and pull requests. Do not include secrets/API keys, DNS credentials, private addresses, internal server diagrams, private Serenari source or protected personal information.

## Review gates
1. Content accuracy and status labeling.
2. Accessibility and mobile behavior.
3. No broken links or unexpected loss of legacy pages.
4. No private-content disclosure.
5. Test/deployment validation and explicit publication approval.
