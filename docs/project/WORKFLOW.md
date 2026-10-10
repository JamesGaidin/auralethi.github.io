# Development, News, and Publication Workflow

## Low-cost operating model
Current site is static on an existing GitHub Pages repository. Prefer plain static site technology for near-term launch. HTML/CSS/JavaScript are fine; reserve potential Blazor WebAssembly migration for a later phase if beneficial. **Blazor Server / interactive server hosting requires separate infrastructure; do not silently introduce paid dependencies.**

## Development cycle
1. Read `AGENTS.md`, these docs, actual repository tree and current branch.
2. Make changes on `feature/*`; never treat draft branch content as deployed.
3. Test local behavior including semantic HTML, keyboard focus, reduced motion, mobile, URLs and accessibility.
4. Record updates to STATE and relevant notes in same change set.
5. Open PR to `main` with scope, screenshots if useful, tested checks, risks and rollback.
6. Obtain explicit owner approval; merge only after authorization.
7. Verify public deployment and update STATE with date/URL/results.

## News pipeline (proposed)
- Weekly progress automation drafts content using verified/public or founder-approved facts.
- Proposed content record should include: title, date, summary, body, project tags, status, evidence/source links, disclosure approval, publication state.
- Drafts remain in feature branches/PRs or owner review; private repo activity never flows automatically to public pages.
- After review/approval, merge and verify the live News page.
- Do not claim automatic PR authoring, deployment, or scheduled publication until demonstrated end to end.
- If there is no meaningful progress, say so; don't manufacture news.
- Consider machine-readable JSON or Markdown plus static generation only when the publishing process is tested.

## Reversibility
Avoid direct rewrites of `main`. Record commit SHAs and deployment state. Prior site is recoverable through Git history. Maintain working links for QR/business-card route `/about`.

## Domain and hosting
`CNAME` currently points to `auralethi.org`. Registrar, expiration, DNS and email services require verification before touching records. No domain/email changes are prerequisites to initial content redesign.

## Team collaboration
Documents are the portable memory fabric. Any agent returning from a new thread should verify the documents against Git HEAD; do not assume that chat memory is authoritative.
