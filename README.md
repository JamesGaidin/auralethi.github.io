# Auralethi website

Public, static website for [Auralethi](https://auralethi.org/), published from this repository.

## Active pages

- `/` Home
- `/free-to-meet/` Oregon and national resource navigation
- `/safe-to-become/` Support pathways and safety information
- `/projects/` Projects and long-term vision
- `/research/` Research, CortexOS, Serenari and relational risk
- `/news/` Our Journey
- `/about/`, `/contact/`, `/get-involved/` Footer destinations

The site's public content and current presentation use `assets/css/homecoming.css`, `assets/js/`, `content/resources/`, and `content/updates/`. Legacy Systems, shared HTML fragments and the old standalone stylesheet have been removed from the current tree. Prior versions remain available in Git history.

For contributor and publication guidance see `AGENTS.md` and `docs/project/`.

## Link maintenance

A weekly GitHub Actions audit checks site references and external resource destinations. See `docs/project/LINK_MAINTENANCE.md` and `scripts/check_site_links.py`. Confirmed failures are surfaced for human review, not silently deleted.
