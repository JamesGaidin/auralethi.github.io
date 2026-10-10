# Website Project Context

**Project:** Auralethi public website — Homecoming redesign  
**Repository:** `JamesGaidin/auralethi.github.io`  
**Domain:** `auralethi.org` (repository CNAME; registrar and DNS not independently verified)  
**Status:** Planning and development, not yet published  
**Last documented:** 2026-10-09

## Purpose
Build the public front door for Auralethi: a growing, community-centered nonprofit vision that invites people to connect, explore and choose their own paths. The site should show concrete research and ongoing work alongside transparently labeled future aspirations. The community is its people; Auralethi seeks to support the conditions in which people can connect and thrive.

## Experience direction
- Brief, optional, accessible introductory splash displaying **Auralethi** and three values (working words: *Community, Belonging, Possibility*; not final), followed by **Free to meet. Safe to become.**
- Homepage introduces the organization first, then asks about the visitor's interests, needs, aspirations and possibilities.
- **Free to Meet:** community, connections, exploration, technology, education, creativity, research.
- **Safe to Become:** stability and practical supports, accessible living, independence, care, opportunities.
- Project pages show status, evidence of progress, next steps, and distinguish plans from availability.
- News/progress page shows a verifiable journey including setbacks, not promotional filler.
- Future **Jix** assistant/receptionist is optional and never required to navigate the site. Architecture may reserve an integration point; do not claim it is deployed.

## Proposed information architecture
Home; Free to Meet; Safe to Become; Projects; Research; About; News / Our Journey. These are proposals, not confirmation that routes already exist.

## Design constraints
Accessible, responsive, keyboard navigable, fast-loading, support reduced motion, respect privacy, usable without conversational AI or authentication. Minimal cost: existing GitHub Pages/static frontend. Future Visual Studio/Blazor option must not force paid server hosting.

## Origin and continuity
Original 2025 site focused on belonging and a sanctuary for misunderstood people. April 2026 redesign emphasized AI safety research. October 2026 goal reconnects the original community mission with the matured research and systems as enabling projects. Preserve research substance without making technology the organization's entire identity.

## Relevant source baseline
Commit `1a395b2bb7` (2025-05-15) contains pre-AI-safety homepage; commit `fb3da811fa` (2026-04-17) introduces AI-safety positioning; `2959d89014` (2026-04-17) is the latest known `main` baseline at the time this document was authored.

See STATE, GOVERNANCE, WORKFLOW, ROADMAP.
