# Current State and Next Session Handoff

Verified GitHub snapshot, 2026-10-09, main HEAD: 8c2e2407a00e8d80c66f49b40f11057135fc5913. Recheck before acting.

## Mandatory restart
1. Read AGENTS.md, docs/project/README.md, STATE.md, GOVERNANCE.md, WORKFLOW.md, ROADMAP.md, RESEARCH_PUBLICATION.md.
2. Fetch current main HEAD and current PR status from GitHub. Compare against this checkpoint. Do not use remembered PR status.
3. Check actual page HTML/CSS and the real public site before making claims about visual rendering.
4. Flag discrepancies, then plan a bounded feature-branch change. Keep these docs current after merges.

## GitHub verified
- Repository JamesGaidin/auralethi.github.io, default branch main, static GitHub Pages compatible site, CNAME auralethi.org.
- PR #1 Homecoming homepage and mission/navigation/content scaffolds merged.
- PR #2 brand palette and public motto updates merged.
- PR #3 JPEG logo workaround merged. Previously broken image handling must not be treated as resolved by existence alone.
- Original full-size brand proof image uploaded by founder: assets/logo.png. It is an opaque proof sheet, NOT a transparent icon.
- PR #4 Research rebuild MERGED. Merge SHA 7fbed025dd023fa7f2dc4776a92590919eb995e8.
- PR #5 About restore, CSS image sprite and animated hero MERGED. Merge SHA 8c2e2407a00e8d80c66f49b40f11057135fc5913. An assistant mistakenly claimed PR #5 was still pending: this is why fresh retrieval is mandatory.
- About uses the founder's first-person 2025 text recovered from commit 1a395b2bb7, with the Standing at the Edge section deliberately omitted. Do not explain that omission publicly. The rest stays in original voice.
- Research now includes programs, publications, an open-question section and description of future feeds. The canonical backlog is NOT yet published, and automated feeds are NOT built.
- About and Contact Us belong in footer only. Contact is still a placeholder; no unverified organizational inbox or personal phone.
- Website header/footer on Homecoming pages render the logo via CSS background sprite of assets/logo.png, not regenerated emblem; homepage animated orbit uses the same genuine art and CSS, and supports reduced motion.
- Exact hero/header sprite crop coordinates have not been verified in browser. Current favicon references older JPEG on some pages, needing replacement with a verified true crop.
- Public tagline: Free to meet. Safe to become.
- Public motto: We build things. We test stuff. We document. We share what we learn.
- New writing must NOT use em dashes. Original founder text is a historical exception, preserve its punctuation.

## Research policy
Canonical Research_Backlog.xlsx is stored outside this public repo. Snapshot of Oct 6 has IDs RES-0001 through RES-0008, all Unassigned/Backlog. Admission does not authorize publication. Governed path: Suggest, Discuss, Admit, Release. Independent researchers may freely explore questions without obligation. Avoid treating conversation-generated examples as canonical.

## Unverified or unfinished
- Real browser testing for visual logo crop, splash, mobile, desktop, link correctness, keyboard usability, reduced-motion, caching and favicon.
- Deployment behavior and status must be checked against public URL, not inferred from a merge alone. Founder reports the redesign looks excellent.
- Dedicated properly cropped favicon and cleanup of older JPEG/SVG logo assets.
- Content data model and shared tagged project feeds, research backlog publishing, independent contributor credit and verified project details.
- Original personal 2025 About story restored; extended bios, org chart and official contact channel are future work.
- Older systems/get-involved routes may still use legacy styling.
- Registrar/DNS and actual email service unverified. Jix is not deployed.
- Weekly Friday automated progress draft was configured separately in ChatGPT; do not infer it publishes, writes PRs or has passed an end-to-end test.

## Next actions
1. Verify merged PR #5 visually and functionally on desktop/mobile, especially real-logo sprite crop and orbit motion.
2. Make verified favicon/logo fixes on a new branch without altering original artwork.
3. Create shared content templates and evidence/approval rules for Projects, Research, News.
4. Review each canonical backlog question for explicit public release.
5. Populate verified CortexOS, Serenari and organization bios; establish official contact channels when available.
6. At every merge: update this document and record merge SHA, tests and remaining gaps.

This documentation synchronization lives on docs/verified-homecoming-handoff pending human-approved merge.
