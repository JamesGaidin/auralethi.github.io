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

## Pending feature branch, 2026-10-10
- Branch `feature/about-research-detail-fix` removes the still-live (on prior `main`) visitor-facing editorial omission paragraph from `about/index.html`.
- Adds `research/cortexos/`, `research/serenari/` and `research/relational-surface-risk/` detail routes. Replaces Research and Projects index links that previously redirected back to general overview pages.
- Draft content intentionally distinguishes research and implementation from proven or operational public services; no unverified results were published.
- Original founding story, including historical punctuation, is otherwise preserved. About and Contact remain footer-only.
- **Not on main until founder-approved merge.** After merge, verify actual mobile/desktop rendered pages and continue deeper source-backed program content and news feeds. Browser verification has not been performed.

## Additional pending work, 2026-10-10
- About is now a second landing page for business card arrivals: welcome, links to Projects/Research/News/Get Involved, then the preserved 2025 founder story.
- Rebuilt /get-involved/ as a Homecoming styled community participation landing page. Forums, discussion boards and live chat are explicitly future plans, not currently available services. No unverified contact email or personal phone.
- Added Get Involved to footer navigation across Homecoming pages and legacy shared/footer.html. About, Contact and Get Involved remain absent from the primary header navigation.
- All these changes remain on feature/about-research-detail-fix, not published until approved and merged; check rendered links and mobile appearance after deployment.

## Icon cleanup branch (2026-10-11)
- Feature branch `feature/branding-icons-favicon-cleanup` changes header/footer/splash CSS to render the existing verified transparent source `assets/auralethi-logo-transparent-redo2.png`, replacing black-box crop of the opaque proof sheet.
- All current HTML page heads now reference that same PNG as a tab icon instead of the previous problematic JPEG link. Browser-specific favicon appearance still requires checking after merge and cache refresh.
- Resized favicon/icon binary files and `.ico` generated in the assistant runtime have NOT yet been uploaded into GitHub. The connector allows Git blob writes with base64 content, but does not directly accept container files. Do not claim the icon pack is published. A proper multiresolution favicon pack remains follow-up.
- The 'Auralethi Weekly Progress' Friday automation is enabled, but as inspected 2026-10-11 it has no confirmed runs; notifications are disabled. The automation does not publish without founder approval.

## Pending Our Journey content PR, 2026-10-13
- Branch `feature/our-journey-records` adds `content/updates/events.json`, `assets/js/journey.js`, a real retrospective `news/` timeline, `docs/project/EVENT_RECORDS.md`, and timeline styles.
- Five website milestones dated according to public GitHub PR merge evidence are candidates for founder review. PR merge is approval to publish these five summaries. No broader private or Serenari milestone history is released in this change.
- Subsequent work: use shared project tags for per-program timelines, verify mobile/browser render, and record actual reviewer and publication date after release.

## Pending Serenari history first pass (2026-10-13)
- `feature/serenari-project-history` adds a publicly tagged historical view on `/research/serenari/` using `assets/js/program-history.js` and existing `content/updates/events.json` (single source of truth).
- Only the existing public Research doorway event currently has the Serenari tag. It describes publication of a website index, not a technical Serenari milestone. The page explicitly says so.
- No private design chronology, internal code status, test outcome or birth-event claim has been added. Next release needs evidence gathering and founder sign-off for individual technical events.
- Separate splash fix is drafted in PR #11; do not conflate release status.

## Serenari retrospective expansion (2026-10-13)
- PR #12 now contains a substantive public-facing Serenari research story and an explicit personal-lab ownership boundary. The private design source states that Serenari is a single-user personal CortexOS node, not an Auralethi-owned product or service.
- The page includes retrospective July 2026 architecture work (period only), the October 4 v1.0 design lock (document-backed, private evidence), and an October 8 first local greeting (founder-reported, not independently verified). The page explains that design validation is not runtime autonomy proof.
- These retrospective page paragraphs are founder publication candidates. No private technical design documents or private-repo links are disclosed.
- Browser rendering and an isolated PR preview URL are not yet verified. Preview infrastructure remains separately pending.
