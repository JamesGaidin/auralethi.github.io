#!/usr/bin/env python3
"""Static site reference audit. No third-party dependencies or user data."""
import json, re, sys, time, urllib.request, urllib.error
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git", ".github", "docs", "scripts"}
TIMEOUT = 12

class Refs(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        for k in ("href", "src", "action"):
            if d.get(k):
                self.refs.append(d[k])
        if d.get("srcset"):
            self.refs.extend(p.strip().split()[0] for p in d["srcset"].split(",") if p.strip())

def source_files():
    for p in ROOT.rglob("*"):
        if p.is_file() and not any(x in SKIP for x in p.relative_to(ROOT).parts):
            if p.suffix.lower() in (".html", ".css", ".json", ".js"):
                yield p

def normalize_ref(ref, source):
    ref = ref.strip()
    if not ref or ref.startswith(("#", "mailto:", "tel:", "sms:", "data:", "javascript:")):
        return None
    if ref.startswith("//"):
        return ("external", "https:" + ref)
    u = urlsplit(ref)
    if u.scheme in ("http", "https"):
        if u.netloc.lower().removeprefix("www.") in ("auralethi.org", "jamesgaidin.github.io"):
            ref = u.path or "/"
        else:
            return ("external", ref)
    elif u.scheme:
        return None
    else:
        ref = u.path
    if not ref:
        return None
    raw = unquote(ref)
    if raw.startswith("/"):
        target = ROOT / raw.lstrip("/")
    else:
        target = source.parent / raw
    target = target.resolve()
    if not target.is_relative_to(ROOT.resolve()):
        return ("missing", raw)
    if target.is_dir():
        target /= "index.html"
    elif not target.exists() and not target.suffix:
        target /= "index.html"
    return ("internal", str(target.relative_to(ROOT.resolve())))

def extract(path):
    txt = path.read_text(encoding="utf-8")
    if path.suffix == ".html":
        parser = Refs()
        parser.feed(txt)
        return parser.refs
    if path.suffix == ".json":
        return re.findall(r'https?://[^\s"<>]+', txt)
    if path.suffix == ".css":
        return re.findall(r"""url\(\s*['"]?([^)'" ]+)""", txt)
    # JavaScript: catch quoted root-relative assets and literal external URLs.
    return re.findall(r"""["']((?:https?://|/)[^"']+)["']""", txt)

def verify_external(url):
    req = urllib.request.Request(url, headers={"User-Agent": "AuralethiResourceAudit/1.0 (+https://auralethi.org)", "Accept": "text/html,*/*"}, method="HEAD")
    for method in ("HEAD", "GET"):
        if method == "GET":
            req = urllib.request.Request(url, headers={"User-Agent":"AuralethiResourceAudit/1.0", "Range":"bytes=0-1023"}, method="GET")
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
                status = response.status
                end_url = response.url
                return ("ok" if status < 400 else "review", status, end_url)
        except urllib.error.HTTPError as e:
            if method == "HEAD" and e.code in (403, 405, 429, 501):
                continue
            if e.code in (404, 410):
                return ("broken", e.code, url)
            return ("review", e.code, url)
        except Exception as e:
            if method == "HEAD":
                continue
            return ("review", type(e).__name__, url)
    return ("review", "unavailable", url)

def main():
    pages = list(source_files())
    refs = {}
    missing = []
    external = {}
    for p in pages:
        rel = str(p.relative_to(ROOT))
        for raw in extract(p):
            result = normalize_ref(raw, p)
            if result is None:
                continue
            kind, value = result
            if kind == "external":
                external.setdefault(value, []).append(rel)
            elif kind == "missing" or not (ROOT / value).is_file():
                missing.append({"source": rel, "url": raw, "target": value})
            else:
                refs.setdefault(value, []).append(rel)
    checked = []
    for url, used in sorted(external.items()):
        state, status, final = verify_external(url)
        checked.append({"url":url, "sources": sorted(set(used)), "result":state, "status":status, "resolved":final})
        time.sleep(0.15)
    report = {"files_scanned":len(pages), "internal_missing":missing, "external_checked":len(checked), "external_broken":[x for x in checked if x["result"]=="broken"], "external_review":[x for x in checked if x["result"]=="review"], "external_results":checked}
    out = ROOT / "link-audit-report.json"
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False)+"\n",encoding="utf-8")
    print(f"Scanned {len(pages)} files; missing internal {len(missing)}, external broken {len(report['external_broken'])}, review needed {len(report['external_review'])}")
    for x in missing: print("MISSING",x)
    for x in report["external_broken"]: print("BROKEN",x["status"],x["url"])
    for x in report["external_review"]: print("REVIEW",x["status"],x["url"])
    return 1 if missing or report["external_broken"] else 0

if __name__ == "__main__":
    sys.exit(main())
