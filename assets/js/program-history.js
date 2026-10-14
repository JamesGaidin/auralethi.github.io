(() => {
  "use strict";
  const root = document.getElementById("serenari-history");
  if (!root) return;
  fetch("/content/updates/events.json")
    .then(r => {if (!r.ok) throw new Error("History not available"); return r.json();})
    .then(data => {
      if (!Array.isArray(data.records)) throw new Error("Invalid history");
      const records = data.records.filter(e => e.verification_status === "verified-public-merge" && e.visibility === "public-candidate" && Array.isArray(e.project_ids) && e.project_ids.includes("serenari")).sort((a,b) => b.event_date.localeCompare(a.event_date));
      root.replaceChildren();
      if (!records.length) {root.textContent = "Verified public milestones are being curated.";return;}
      records.forEach(e => {
        const card=document.createElement("article");card.className="card journey-entry";
        const when=document.createElement("time");when.dateTime=e.event_date;when.className="eyebrow";when.textContent=e.event_date;
        const h=document.createElement("h3");h.textContent=e.title;
        const p=document.createElement("p");p.textContent=e.summary;
        const evidence=document.createElement("p");evidence.className="journey-source";
        (e.evidence_links||[]).forEach(link=>{if(typeof link.url!=="string" || !link.url.startsWith("https://github.com/"))return;const a=document.createElement("a");a.href=link.url;a.rel="noopener noreferrer";a.textContent=link.label||"Evidence";evidence.append(a);});
        card.append(when,h,p,evidence);root.append(card);
      });
    }).catch(() => {root.textContent="Related updates are temporarily unavailable.";});
})();