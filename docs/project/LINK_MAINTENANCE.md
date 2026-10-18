# Website link and resource maintenance

Run `python3 scripts/check_site_links.py` from the site repository. The script audits source references, including static HTML routes, CSS assets, JavaScript literal links and JSON resource URLs. Its report is written to `link-audit-report.json` (ignored by git).

The GitHub Actions workflow runs on Fridays at **16:00 UTC**, on affected pushes, and manually from the Actions tab. This is 9 AM Pacific in daylight time and 8 AM in standard time; GitHub cron does not automatically observe Pacific DST. It checks external HTTP destinations and writes an artifact. Confirmed missing internal files or HTTP 404/410 external responses fail the check and create or update a maintenance issue. 403, 429, timeouts and other ambiguous responses are reported as needing manual review, not proof a provider is dead.

**Editorial safety boundary:** HTTP 200 does not prove the address, phone number, eligibility, hours or program details are accurate. Every resource also needs periodic human content review against authoritative provider sources. Never silently drop a resource after one failed network check; find a verified replacement or make its status explicit. Avoid sending personal visitor data to providers or link-check tools. Never commit audit outputs containing credentials or personal data.

**Current-tree cleanup:** Historical website files retired from `main` stay in Git history. This does not rewrite past commits. Keep private implementation artifacts outside the public tree; do not delete canonical project docs, current logos, or research evidence without individual review.

**Known limits:** This checks static and literal links, not destinations constructed at runtime, pages discoverable only through browser interactions, or visual accessibility. Review rendered behavior separately. Outbound sites may block automated agents. For unlinked HTML routes, compare the current site tree with Jix's generated World list and decide whether each page should be made reachable or removed.
