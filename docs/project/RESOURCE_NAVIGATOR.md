# Oregon Resource Navigator v0.1

## Scope
Oregon is the initial service region. Colorado is a candidate future editorial region, not an active or verified directory. Do not display Colorado services until separately researched and approved.

## Structure
- `content/resources/oregon.json`: independently editable, sourced resource records.
- `assets/js/resource-navigator.js`: simple client-side filtering by human need and disclosure of actionable instructions.
- `free-to-meet/index.html`: navigator entry point, while retaining the existing resource guide.
- No account, geolocation, cookies, API key, personal data collection, eligibility engine, or AI recommendations.

## Resource record fields
`id`, `name`, `region`, `needs`, `audience`, `steps`, `url`, optional `phone`, `source`, `verified_on`, `status`, `limitations`. Unique IDs; official source URLs when possible.

## Editorial process
1. Confirm official provider contact and service scope, not funding availability or individual eligibility.
2. Record verification date and source URL. Recheck after meaningful provider changes or before promoting high-stakes time-specific instructions.
3. Explain how to begin and what to ask, without promising that an application will be accepted.
4. Make correction workflow visible in future iteration; never collect medical, financial, identity, or immigration records in a static site.
5. When an assistance path is unavailable, route to a different starting point, such as 211, instead of asserting failure for all alternatives.

## Validation
Before merge: keyboard, screen-reader labeling, touch/mobile layout, failure fallback, source-link check, and read-through by a person unfamiliar with the system. Connector-side markup checks do not constitute browser QA.

## Next build candidates
- Clarify need subtypes, urgency and county as optional choices without collecting data.
- Resource update/correction process and freshness review schedule.
- Comprehensive catalog coverage beyond first five entries.
- Print-friendly instructions and truly useful alternative paths.
- Later: Colorado catalog as independently verified data, separated from Oregon.
