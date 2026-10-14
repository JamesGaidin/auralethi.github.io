# Shared Event Records, v1

## Purpose
One governed record of evidence-linked events can support Our Journey, individual projects, and research pages without creating conflicting histories. Version one renders only the Our Journey view. Other filtered views are future work.

## Source of truth
`content/updates/events.json` contains an array of records. Each must include:
- `id`: stable unique identifier
- `type`: `update` for this initial version
- `title`, `summary`: founder-reviewed public wording
- `event_date`: ISO YYYY-MM-DD date when event occurred; `event_timezone` names the reference zone
- `recorded_date`: date retrospectively entered into the dataset
- `published_date`: date actually released; null until confirmed after publication
- `status`: current description of the specific milestone (e.g. completed), not a blanket project status
- `visibility`: `public-candidate` prior to review, and approved for website exposure only when founder approves the PR containing that exact record
- `reviewed_by`: null until human review is recorded; never fabricate a signature
- `verification_status`: `verified-public-merge` for public commit/PR-backed events; other evidence levels must be defined before use
- `project_ids`, `tags`: stable cross-page filters
- `evidence_links`: labeled public citations, which the current renderer allows only from github.com

## Editorial release gate
Records in this initial PR are **candidates**. The News renderer displays candidates once its source files are merged. Therefore **merging the PR is explicit approval to publish all five included historical summaries**. If any record is unapproved, edit or remove it before merging. No private repository claims or internal Serenari test claims are included.
After merge, verify live rendering, record the actual publish date and reviewer in a follow-up documentation update. GitHub merge alone is not verification that browsers rendered the page.

## Historical integrity
Never silently substitute the recording date or publication date for an event date. Dates in this first batch correspond to the America/Los_Angeles calendar date of publicly verifiable GitHub PR merges. The timeline is intentionally retrospective.
Do not duplicate a record for each project; use its tags and project_ids for later program views. No automatic public posting from scheduled tools without human approval.

## Current limits
The renderer is plain browser JavaScript fetching static JSON. It fails with a readable fallback when the file cannot load. Browser QA, accessibility audits and eventual no-JavaScript pre-rendering remain to be done. Only the organization-wide Journey uses this data so far.
