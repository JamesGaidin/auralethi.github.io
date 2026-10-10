# Auralethi Research Publication Model (Draft for Founder Review)

## Central rule
The **Open Research Backlog is primarily research for other people to do**, not Auralethi's internal engineering to-do list. An entry is an open invitation to investigate independently. No obligation to return findings, seek permission, adopt Auralethi designs, or work for Auralethi.

## Separate content types
- `program`: an Auralethi or collaborator research effort (e.g., CortexOS, Serenari, relational AI safety). May have independent per-program updates.
- `publication`: a published artifact such as a paper, documentation, results, or a methods essay. State maturity and evidence level.
- `question`: an open research opportunity, independently useful without access to internal IP or any particular architecture.
- `update`: a dated, sourced/verified progress record tagged with zero or more programs/topics. One approved record can appear both in the global Our Journey feed and applicable program/research feeds.

## Suggested data contract (not deployed yet)
Keep one text record per item under a future `content/research/` tree. JSON, YAML, or frontmatter Markdown can be used without a backend.

Required fields: `id`, `type`, `title`, `summary`, `status`, `created`, `updated`, `visibility`, `reviewed_by`, `links` and `tags`.
For questions, add `research_question`, `possible_directions`, `success_criteria`, `existing_work` and `contributions`. For updates, add `program_ids`, `evidence_links`, `verification_status`.

## Editorial and governance rules
1. Backlog questions are **not work assignments or paid commissions**. The default invitation is independent investigation.
2. Questions can be wrong, answered already, superseded, or deliberately open ended. Record that instead of quietly erasing history.
3. Keep private data, credentials, access-control weaknesses, and unreleased confidential material outside public content. Public design discussion is welcome, but publication is a deliberate choice.
4. Treat contributors as independent authors; get permission and agree on attribution/licensing before reproducing their work.
5. No promises of official research collaboration, moderation, response time or review turnaround before the mechanism exists.
6. A single approved update can render in organization-wide and program-specific feeds. Never clone conflicting copies.
7. A question may inspire different architectures. Comparison, criticism and independent approaches are successes, not defections.
8. Distinguish `proposed`, `inquiry`, `investigating`, `results available`, `answered`, and `archived` without implying the founder is personally executing every entry.
9. Publication requires founder editorial approval. Merely merging implementation scaffolding doesn't approve new factual claims.
10. Accessible static-first delivery on GitHub Pages, with any interactive filtering progressively enhanced.

## Canonical records and release boundary
- Primary current source is `Research_Backlog.xlsx` outside this public website repository. Its October 6 snapshot contains RES-0001 through RES-0008, marked Backlog and Unassigned.
- Follow **Suggest, Discuss, Admit, Release**. Capture/admission alone do not authorize public release.
- PR #4 already merged the public Research page scaffold, but no canonical backlog items were published. A planned feed is not a built feed.
- The researcher for an open backlog question is intended to be an independent interested person, not the founder by default.

## Immediate next iterations
- Founder approves first backlog entries, sources and exact public phrasing.
- Separate program landing pages and reusable update record template.
- Dated feeds and tags derived from the same content records.
- Contribution/contact route only after an organizational channel is verified.

## Lessons from Serenari document discussions
Governance can be taught through the form of an artifact: explicit scope, visible uncertainties, reviewable decisions, traceable amendments and independent challenges. The research portal should demonstrate those properties itself, without claiming the design proves an implementation.
