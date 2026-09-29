#!/usr/bin/env python3
"""Static page generator for 111176.com.
Run:  python3 tools/build.py   (writes HTML files into the repo root)
Edit page bodies in tools/pages.py and tools/articles.py.
"""
import json, os, datetime
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://111176.com"
UPDATED = "2026-09-29"
INQUIRY = "https://web.works/contact"
V = "20260929"

NAV = [
    ("Tools", None, [("decoder.html", "🔢 Number Decoder"), ("tools.html", "🧰 All Number Tools"), ("zodiac.html", "🐉 Zodiac &amp; Lucky Numbers"), ("lucky-dates.html", "📅 Lucky Dates Calendar")]),
    ("Meanings", "meanings.html", None),
    ("Learn", "learn.html", [("learn.html", "📚 All Guides"), ("learn/why-8-is-lucky.html", "Why 8 Is Lucky"), ("learn/why-4-is-unlucky.html", "Why 4 Is Avoided"), ("learn/chinese-number-slang.html", "Number Slang 520 · 666 · 88"), ("learn/singles-day-11-11.html", "Singles’ Day 11.11"), ("learn/meaning-of-111176.html", "What 111176 Means"), ("learn/numeric-domains-china.html", "Numeric Domains in China")]),
    ("Videos", "videos.html", None),
    ("For Business", "business.html", None),
    ("Domains", "domains.html", None),
    ("Contests", "contests.html", None),
    ("Support", "support.html", [("support.html", "❤️ Donate &amp; Support"), ("support.html#sponsor", "🤝 Sponsorship"), ("support.html#advertise", "📣 Advertise"), ("support.html#careers", "💼 Careers / Talent"), ("contact.html", "✉️ Contact")]),
]

def nav_html(r):
    out = []
    for label, href, sub in NAV:
        if sub:
            items = "".join(f'<li><a href="{r}{h}">{t}</a></li>' for h, t in sub)
            top = f'<a href="{r}{href}">{label} ▾</a>' if href else f'<button type="button" aria-haspopup="true">{label} ▾</button>'
            out.append(f'<li>{top}<ul class="dropdown">{items}</ul></li>')
        else:
            out.append(f'<li><a href="{r}{href}">{label}</a></li>')
    return "".join(out)

def ad(slot="default", cls=""):
    return f'<div class="ad-slot {cls}" data-slot="" aria-label="Advertisement"></div>'

def breadcrumb(r, items):
    parts = [f'<a href="{r}index.html">Home</a>'] + [f'<a href="{r}{h}">{t}</a>' if h else t for h, t in items]
    ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + "/" + (h or "")} for i, (h, n) in enumerate([("", "Home")] + items)]}
    return f'<nav class="breadcrumb" aria-label="Breadcrumb">{" › ".join(parts)}</nav><script type="application/ld+json">{json.dumps(ld)}</script>'

def report_form(r, title="Get your FREE full Lucky Number Report", sub="Personalised meanings, zodiac match, lucky dates for the next 90 days &amp; better alternatives — delivered to your inbox."):
    return f'''
<div class="cta-band" id="full-report">
  <div class="split">
    <div>
      <span class="eyebrow" style="color:#ffe7a3">Free · 60 seconds</span>
      <h2>{title}</h2>
      <p>{sub}</p>
      <div class="trust"><span>✔ 100% free</span><span>✔ No spam — unsubscribe anytime</span><span>✔ Human-checked</span></div>
    </div>
    <form class="js-form card" id="report" data-subject="Lucky Number Report request" style="color:var(--text)">
      <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
      <input type="hidden" name="form" value="Full Lucky Number Report">
      <div class="field"><label for="rp-name">First name</label><input id="rp-name" name="name" required autocomplete="given-name"></div>
      <div class="field"><label for="rp-email">Email</label><input id="rp-email" type="email" name="email" required autocomplete="email" placeholder="you@example.com"></div>
      <div class="row"><div class="field"><label for="rp-dob">Birth date</label><input id="rp-dob" type="date" name="birth_date"></div>
      <div class="field"><label for="report-number">Number to analyse</label><input id="report-number" name="number" placeholder="phone / plate / date"></div></div>
      <div class="field"><label for="rp-goal">Main goal</label><select id="rp-goal" name="goal"><option>Personal luck</option><option>Choose a phone / plate number</option><option>Wedding or moving date</option><option>Business name, price or launch</option><option>Buying / selling a numeric domain</option></select></div>
      <label class="check"><input type="checkbox" name="newsletter" value="yes" checked> Also send me the weekly “Lucky Number” email</label>
      <button class="btn btn-primary btn-block" type="submit" style="margin-top:12px">Send my free report →</button>
      <p class="form-note">By submitting you agree to our <a href="{r}privacy.html">Privacy Policy</a>.</p>
    </form>
  </div>
</div>'''

def newsletter_inline(r, id_="newsletter"):
    return f'''<form class="js-form" id="{id_}" data-subject="Newsletter signup" data-next="stay">
<input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
<input type="hidden" name="form" value="Newsletter">
<div class="input-group"><label class="skip" for="{id_}-e">Email</label><input id="{id_}-e" type="email" name="email" required placeholder="Your email for the weekly lucky number"><button class="btn btn-gold" type="submit">Subscribe</button></div>
</form>'''

def page(path, title, desc, body, schema=None, og_type="website", noindex=False):
    depth = path.count("/")
    r = "../" * depth
    canonical = SITE + "/" + ("" if path == "index.html" else path)
    full_title = title if "111176" in title else f"{title} | 111176"
    ld = [{"@context": "https://schema.org", "@type": "WebSite", "name": "111176", "url": SITE + "/",
           "potentialAction": {"@type": "SearchAction", "target": SITE + "/decoder.html?n={query}", "query-input": "required name=query"}},
          {"@context": "https://schema.org", "@type": "Organization", "name": "111176", "url": SITE + "/", "logo": SITE + "/assets/img/favicon.svg"}] if path == "index.html" else []
    if schema: ld += schema if isinstance(schema, list) else [schema]
    ld_html = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    robots = '<meta name="robots" content="noindex,follow">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large">'
    BASE = '<script>document.write(\'<base href="\'+(location.pathname.indexOf("/111176-com/")===0?"/111176-com/":"/")+\'">\')</script>\n' if path == "404.html" else ""
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
{BASE}<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{desc}">
{robots}
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#c8102e">
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="111176">
<meta property="og:title" content="{full_title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}"><meta property="og:image" content="{SITE}/assets/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{r}assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{r}assets/img/favicon.svg">
<link rel="manifest" href="{r}manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Noto+Serif+SC:wght@600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/css/style.css?v={V}">
<script>try{{var t=localStorage.getItem("theme");if(t)document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
{ld_html}
</head>
<body data-root="{r}">
<a class="skip" href="#main">Skip to content</a>
<div class="topbar" role="note">Contact, if you are interested in this <a href="{INQUIRY}" target="_blank" rel="noopener">website / domain name / Sponsorship / Advertisement / Partnership</a></div>
<header class="site-header">
  <div class="container nav">
    <a class="brand" href="{r}index.html" aria-label="111176 home"><span class="brand-mark" aria-hidden="true">吉</span><span>111176<small>Chinese Number Decoder</small></span></a>
    <ul class="menu" id="menu">{nav_html(r)}</ul>
    <div class="header-actions">
      <button class="icon-btn theme-toggle" type="button" aria-label="Toggle dark mode">◐</button>
      <a class="btn btn-primary btn-sm" href="{r}decoder.html" style="white-space:nowrap">Decode</a>
      <button class="icon-btn burger" type="button" aria-label="Open menu" aria-controls="menu" aria-expanded="false">☰</button>
    </div>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a class="brand" href="{r}index.html" style="color:#fff"><span class="brand-mark">吉</span><span>111176</span></a>
        <p style="margin-top:12px">Free tools and plain-English guides to Chinese number meanings, lucky numbers, lucky dates, number slang and China commerce.</p>
        <p class="small">Get the weekly lucky number:</p>
        {newsletter_inline(r, "newsletter-foot")}
      </div>
      <div><h4>Tools</h4><ul><li><a href="{r}decoder.html">Number Decoder</a></li><li><a href="{r}tools.html#generator">Lucky Number Generator</a></li><li><a href="{r}tools.html#converter">Chinese Numeral Converter</a></li><li><a href="{r}zodiac.html">Zodiac Finder</a></li><li><a href="{r}lucky-dates.html">Lucky Dates</a></li><li><a href="{r}tools.html#domain">Numeric Domain Scorer</a></li></ul></div>
      <div><h4>Explore</h4><ul><li><a href="{r}meanings.html">Number Dictionary</a></li><li><a href="{r}learn.html">Guides</a></li><li><a href="{r}videos.html">Videos</a></li><li><a href="{r}business.html">For Business</a></li><li><a href="{r}domains.html">Numeric Domains</a></li><li><a href="{r}contests.html">Contests &amp; Prizes</a></li></ul></div>
      <div><h4>Company</h4><ul><li><a href="{r}about.html">About</a></li><li><a href="{r}contact.html">Contact</a></li><li><a href="{r}support.html">Donate / Support</a></li><li><a href="{r}support.html#advertise">Advertise</a></li><li><a href="{r}support.html#careers">Careers</a></li><li><a href="{INQUIRY}" target="_blank" rel="noopener">Buy / Partner on this domain</a></li></ul></div>
    </div>
    <div class="footer-bottom">
      <p>© <span data-year>2026</span> 111176.com. Original content and code; all rights reserved. “111176” is used as a domain name and descriptive number only — no trademark is claimed in the number itself. Third-party names and marks belong to their owners. <a href="{r}disclaimer.html">Disclaimer &amp; Trademark/Copyright Notice</a> · <a href="{r}privacy.html">Privacy</a> · <a href="{r}terms.html">Terms</a> · <a href="{r}sitemap.xml">Sitemap</a></p>
      <p>Content is for cultural education and entertainment — not financial, legal, medical or religious advice.</p>
    </div>
  </div>
</footer>
<script src="{r}assets/js/config.js?v={V}"></script>
<script src="{r}assets/js/numbers.js?v={V}" defer></script>
<script src="{r}assets/js/main.js?v={V}" defer></script>
</body>
</html>'''

def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

def faq_html(faqs):
    return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

def write(path, html):
    full = os.path.join(ROOT_DIR, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import pages, articles
    all_pages = pages.build() + articles.build()
    for p in all_pages:
        write(p["path"], page(p["path"], p["title"], p["desc"], p["body"], p.get("schema"), p.get("og", "website"), p.get("noindex", False)))
    urls = [p["path"] for p in all_pages if not p.get("noindex")]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        loc = SITE + "/" + ("" if u == "index.html" else u)
        pr = "1.0" if u == "index.html" else ("0.9" if u in ("decoder.html", "meanings.html", "tools.html") else "0.7")
        sm.append(f"  <url><loc>{loc}</loc><lastmod>{UPDATED}</lastmod><priority>{pr}</priority></url>")
    sm.append("</urlset>")
    write("sitemap.xml", "\n".join(sm) + "\n")
    print(f"Built {len(all_pages)} pages")
