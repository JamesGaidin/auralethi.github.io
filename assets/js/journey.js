(() => {
  "use strict";
  const root = document.getElementById("journey-records");
  if (!root) return;
  fetch("/content/updates/events.json", {cache:"no-store"})
    .then(response => { if (!response.ok) throw Error("Could not load records"); return response.json(); })
    .then(payload => {
      if (!payload || !Array.isArray(payload.records)) throw Error("Invalid records");
      const items = payload.records.filter(r => r.visibility === "public-candidate" && r.verification_status === "verified-public-merge" && r.feed_level === "journey")
        .sort((a,b) => b.event_date.localeCompare(a.event_date) || a.id.localeCompare(b.id));
      if (!items.length) { root.textContent = "Our public timeline is being prepared."; return; }
      root.replaceChildren();
      const heading = document.createElement("h2");
      heading.textContent = "Milestones from our journey";
      root.append(heading);
      const list = document.createElement("div");
      list.className = "journey-list";
      for (const item of items) {
        const article = document.createElement("article");
        article.className = "card journey-entry";
        const time = document.createElement("time");
        time.dateTime = item.event_date;
        time.className = "eyebrow";
        time.textContent = new Date(item.event_date + "T12:00:00").toLocaleDateString("en-US", {year:"numeric",month:"long",day:"numeric"});
        const title = document.createElement("h3");
        title.textContent = item.title;
        const desc = document.createElement("p");
        desc.textContent = item.summary;
        const source = document.createElement("p");
        source.className = "journey-source";
        for (const e of item.evidence_links || []) {
          if (typeof e.url !== "string" || !e.url.startsWith("https://github.com/")) continue;
          const link = document.createElement("a");
          link.href = e.url;
          link.rel = "noopener noreferrer";
          link.textContent = e.label || "Source";
          source.append(link);
        }
        const tags = document.createElement("p");
        tags.className = "journey-tags";
        tags.textContent = (item.tags || []).join(" · ");
        article.append(time,title,desc,source,tags);
        list.append(article);
      }
      root.append(list);
    })
    .catch(() => { root.textContent = "The timeline is temporarily unavailable. Please try again later."; });
})();
