# Auralethi Weekly Progress | October 17–23, 2026

**Status: UNPUBLISHED DRAFT — editorial approval required before publication**

## Making the work clearer, and the website easier to trust

This week, Auralethi focused on two practical questions: How can we explain experimental technology without overstating what it can do? And how can we keep a growing resource website understandable and maintainable?

### Completed

**A clearer window into research.** The public [CortexOS introduction](https://github.com/JamesGaidin/auralethi.github.io/pull/20) now explains the architecture in plain language, including its separation of cognitive work, governance, runtime, and records. It describes research, not a publicly available AI service.

**More accurate terminology.** Follow-up corrections aligned the public description with Serenari's locked v1.0 design: nine cognitive layers, including the Herald, with Calyrix classified separately as a Witness. The entity term is now Eidolon; Halorin is historical terminology. These were documentation corrections, not claims of new technical capabilities. [Naming correction](https://github.com/JamesGaidin/auralethi.github.io/pull/24) · [Classification correction](https://github.com/JamesGaidin/auralethi.github.io/pull/25)

**A tidier, more maintainable site.** Obsolete website files were retired, and an automated link-checking workflow was added. Initial checks completed successfully, but automated link checks do not establish that every listed service's hours, eligibility, or contact details are accurate. [Website cleanup and monitoring](https://github.com/JamesGaidin/auralethi.github.io/pull/22) · [Example successful check](https://github.com/JamesGaidin/auralethi.github.io/actions/runs/39174858282)

### In progress

**Making status explicit.** All 12 visitor-facing pages now carry machine-readable labels distinguishing published pages, research, and development. The experiment is to make those distinctions unambiguous for site tooling and visitors; the labels are in place, while broader real-world interpretation and accessibility still require review. [Page-status change](https://github.com/JamesGaidin/auralethi.github.io/pull/23)

### Next steps

Continue checking links, reviewing resource information against provider sources, and validating accessibility and page behavior. We will distinguish what has been built from what is still being explored, and publish additional research outcomes only when evidence and release approval support them.

**We build things. We test stuff. We document. We share what we learn.**

---

## Editorial notes — not part of the website article

- **Approval required:** Founder review of this article's wording and explicit authorization to publish.
- **Public evidence only:** All links above point to the public Auralethi website repository. No private Serenari or Jix repository content is disclosed.
- **Verification boundary:** Merged PRs confirm changes to public source; a successful workflow run does not substitute for manual content or accessibility testing.
- **Release state:** This Markdown file is a proposal on a non-live feature branch. It is not part of the live News page or public updates feed.
