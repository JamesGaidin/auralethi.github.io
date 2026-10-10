# Homecoming — HTML/CSS Implementation Plan
**Status:** APPROVED 2026-10-09, with footer-only Contact Us added; implementation underway on development branch; NOT published  
**Date:** 2026-10-09  
**Source of direction:** Founder-approved visual mockup and conversation; final copy, artwork and service claims still require review.  
**Implementation target:** Existing static GitHub Pages site, without new hosting services or dependencies.

## 1. Product and editorial hierarchy
The visitor, not the organization, is the protagonist. Preserve the following homepage order:
1. Brief optional intro/splash: name + three values (words provisional) + "Free to meet. Safe to become."
2. Hero: **Who could you become if you had room to become?** plus concise introduction to Auralethi and clear exploration CTA.
3. Pillars: **Free to Meet** (people, ideas, technology, creative exploration) and **Safe to Become** (stability, accessible living, support and self-determination).
4. Selected initiatives: status-labeled cards linking to project details.
5. News / Our Journey: dated, verified updates, not placeholder achievements disguised as real posts.
6. Final invitation: **We want to meet you. Welcome home.**
7. Footer with secondary organization information and **About**.

**Contact navigation rule:** Provide a distinct `/contact/` page with its entry in the footer only, not the primary header or hero; do not publish a phone number, private address, or unverified contact channel. A truthful interim page may say contact details are being established.

**About navigation rule:** About must be linked in the footer only, not the main header, hero CTAs, persistent navigation, or repeated homepage promos. Keep /about/ directly accessible (including existing business-card QR links). On /about/ the organization, founder, people and collaborators can take center stage. A sitemap or accessibility-oriented full-site directory can include About if necessary, without promoting it in the primary visitor journey.

## 2. Navigation and route map
Primary header: Home · Free to Meet · Safe to Become · Projects · Research · News. Optional right CTA: Explore / Get Involved (only if destination has truthful content). **No About in header.**
Proposed paths:
- `/` — homepage
- `/free-to-meet/`
- `/safe-to-become/`
- `/projects/`
- `/research/` (preserve current research)
- `/news/` or `/journey/` (choose one; canonical URL + link)
- `/about/` (footer only)
- `/contact/` (footer only)
- `/get-involved/` (preserve existing path and avoid promising nonexistent contact channels)
- `/systems/` (keep old links functional until redirects or mapping verified)

Header and footer should share consistent markup/links across static pages, using existing shared partial system if robust or a documented static-generation method if justified. Do not require JavaScript for the core navigation to appear.

## 3. Homepage component / DOM blueprint
`<header>` with skip-to-content link and navigation  
Optional splash `<div class="intro" ...>` (progressive enhancement, never blocks page content)  
`<main id="main-content">`
- `<section class="hero" aria-labelledby="hero-title">`: eyebrow/intro label, h1, 1–2 short paragraphs, primary/secondary CTAs; decorative hero media with accessible semantics.
- `<section class="pillars" aria-labelledby="pillars-title">`: two `<article class="pillar-card">`, each with short summary, 3–4 theme bullets, CTA.
- `<section class="featured-projects">`: heading, one-sentence summary, 3–6 `<article class="project-card">`; status badges, verified summary, detail links.
- `<section class="latest-news">`: heading, short intro, 0–3 real dated news cards; if empty, clearly state updates are being prepared.
- `<section class="closing-invitation">`: welcoming line and one or two actions.
`</main>`
`<footer>`: mission signoff, footer-only About link, secondary/legal/accessibility links, optional approved maker motto.

Jix is a **future optional** placeholder only when visibly marked "Coming later"; no fake functioning chat UI, personal data collection, or blocking popup.

## 4. Copy budgets (design constraints, not rigid word limits)
| Surface | Desktop target | Mobile target | Rule |
|---|---:|---:|---|
| Splash | 1 name + 3 single words + tagline | same | No prose paragraph |
| H1 | ~8–12 words | same | Preserve approved question |
| Hero intro | 25–45 words | 25–45 words | State who Auralethi is before invitation |
| Hero actions | 2 short labels | 2 short labels | Real destinations only |
| Pillar heading | 2–4 words | same | Free to Meet / Safe to Become |
| Pillar description | 30–55 words each | same, natural wrap | No dense manifesto block |
| Pillar themes | 3–4 items, 2–6 words each | same | Specific, not duplicative |
| Project card | title + status + 15–30 words | same | Status must be factually verified |
| News card | date + title + 15–30 words | same | No invented dates/outcomes |
| Closing invitation | 15–40 words | same | End with Welcome home |

Long-form philosophy and service detail move to drill-down pages, where they can breathe. No text baked into artwork. User-supplied original long draft is a source for deeper copy, not a mandate to fit it all above the fold.

## 5. Visual system and constraints
Mockup is the **direction**, not a pixel-perfect build contract. Deep navy/violet surfaces with restrained cyan/teal and purple accents; occasional warm human-centered photography/artwork; editorial serif headings and highly readable sans-serif body copy; generous whitespace and subtle luminous accents. Visual imagery must support human connection, not promise built housing or facilities that don't exist.
Suggested design tokens in CSS:
`--bg`, `--surface`, `--surface-2`, `--text`, `--muted`, `--accent-violet`, `--accent-cyan`, `--accent-teal`, `--border`, `--content-width`, `--radius`, `--shadow-glow`.
Use fluid typography (`clamp()`), logical properties, and responsive grid. Desktop two-column pillars; tablet/mobile stack. Project grid 3-column desktop, 2-column tablet, 1-column mobile. News 3 → 1. Avoid microtype like the image's tiny captions.

## 6. Layout breakpoints (initial targets; test by content)
- Wide desktop >= 1200px: max content width ~1200–1280px, hero split text/art 45/55, pillars 2 columns.
- Small desktop/tablet ~768–1199px: hero may stack; cards 2 columns where readable.
- Mobile <768px: single-column reading order; no horizontal overflow; header collapses to an accessible, keyboard-operable menu.
- At 320px CSS width and 200% zoom, all meaningful content/actions remain available.
Responsive behavior is based on available space and measured text, not screenshots alone.

## 7. Splash & motion
- ~1–2.5 second nonblocking brand introduction, **skip** control, disabled by `prefers-reduced-motion: reduce`.
- No forced replay on every internal page or navigation; progressive enhancement may use sessionStorage, but content is always accessible if JS fails.
- Avoid auto-advancing carousels, scroll trapping, flashing, and heavy parallax.
- Animations should use CSS transform/opacity when possible and never obscure essential content.

## 8. Accessibility, performance, privacy
- Landmark structure, exactly one meaningful h1 per page, logical heading levels, visible focus, descriptive link text, usable skip link.
- WCAG AA contrast targets, text remains readable over art via overlays, accessible statuses use text rather than color alone.
- Responsive images with dimensions, modern compression (WebP/AVIF where feasible), alt text for informative images and empty alt for decorative ones.
- Avoid external dependencies, trackers, paid APIs and auto-loading AI chat.
- Budget: aim for fast static pages; optimize hero artwork aggressively; lazy-load below-fold images. Test on a slower phone/network.
- Do not expose private repo content or internal infrastructure details in public copy.

## 9. File plan (initial static release)
```
/
  index.html
  style.css                    # existing baseline; refactor thoughtfully
  assets/
    css/                       # optional: tokens.css, components.css
    js/intro.js                # only if necessary; enhancement only
    img/                       # licensed/owned optimized artwork
  free-to-meet/index.html
  safe-to-become/index.html
  projects/index.html
  research/                    # keep existing route and content
  news/index.html
  about/                       # keep existing route and QR targets
  get-involved/                # preserve existing legacy route
  systems/                     # preserve until explicit migration
  shared/                      # existing navbar/footer; audit before reuse
  AGENTS.md
  docs/project/
```
Choose between preserving current single `style.css` or splitting styles **after** inspecting duplication and deployment behavior. If using JS-injected shared headers/footers, verify no-JS fallbacks or replace with a build-time static include process.

## 10. Asset truthfulness
Image-generation mockup includes attractive **fictional imagery and possibly inaccurate card descriptions/statuses**. Never copy its example project descriptions, badges, dates, social icons or claims verbatim. Specifically Serenari is **not** an accessible housing development; it is the local entity / CortexOS implementation. Project labels and images require factual review.

## 11. Build / review gates
1. Capture current `main` commit and verify GitHub Pages publication source; preserve rollback.
2. Implement HTML shell and CSS tokens on `feature/auralethi-homecoming`.
3. Implement responsive layout with placeholder-free, truthful content.
4. Validate navigation, accessible splash, headings, keyboard, reduced motion, 320px/375px/768px/1280px layouts, color contrast, link targets.
5. Verify actual project descriptions and status labels; review artwork rights/size.
6. Inspect before/after in a browser, test no-JS fallback, measure page weight/performance.
7. Update STATE, ROADMAP, and release notes; open PR with test evidence; **James approves**.
8. Merge/deploy only after approval and verify public site; record commit/deployment outcome.

## 12. Explicit non-goals for first release
No backend, database, member login, chatbot service, donation payment integration, new DNS change, paid hosting, real-time sync, or automated unreviewed publication.

## 13. Open design decisions
- Final three splash words.
- Exact look of the hero artwork and ownership/licensing.
- Formal status of each project and approved public milestone.
- Which first-release pages get full depth vs succinct introductions.
- Whether News or Our Journey is canonical nav label.
- Whether the maker motto belongs in the public footer.
- Footer organization bio depth and how collaborator consent/profile details are handled.

**Completion condition:** This plan guides implementation; it is not a claim that the frontend has been coded, tested or launched.
