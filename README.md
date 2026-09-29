# 111176.com — Chinese Number Decoder

A static website for GitHub Pages' free plan: pure HTML, CSS and vanilla JS, no build step needed to serve it. It offers Chinese number meanings, lucky-number tools, guides, lead generation, donations, contests and ad slots.

**Live (GitHub Pages):** https://webworksa1.github.io/111176-com/
**Strategy, research and the phase-wise build prompt:** [`docs/STRATEGY-AND-BUILD-PROMPT.md`](docs/STRATEGY-AND-BUILD-PROMPT.md)

## Pages
| Area | Files |
|---|---|
| Tools | `decoder.html`, `tools.html` (generator, compatibility, numeral converter, domain scorer), `zodiac.html`, `lucky-dates.html` |
| Content | `meanings.html` (65+ codes), `learn.html` plus 6 guides in `learn/`, `videos.html` |
| Revenue & leads | `business.html` (multi-step B2B form), `domains.html`, `support.html` (donate/sponsor/advertise/careers), `contests.html` |
| Trust | `about.html`, `contact.html`, `privacy.html`, `terms.html`, `disclaimer.html` (trademark/copyright), `404.html`, `thank-you.html` |

## Configure — `assets/js/config.js`
- `ADSENSE_CLIENT`: set to your `ca-pub-…` ID and ads load automatically. Until then, "Advertise here" house ads link to the inquiry page.
- `DONATE`: PayPal.me, Buy Me a Coffee, Ko-fi and GitHub Sponsors URLs. When a URL is empty, its button opens a pledge form instead.
- `GA_ID`: optional GA4 ID. It only loads after the visitor accepts cookies.
- **Forms** post via FormSubmit to the owner inbox. The inbox address is stored encoded and is never shown on the site.
  - The **first form submission** triggers a one-time activation email. Click *Activate* in that email.
  - Optionally, paste the random alias FormSubmit gives you into `FORM_ALIAS`.

## Edit and rebuild
Page bodies live in `tools/pages.py`, `tools/pages_b.py` and `tools/articles.py`. Rebuild with:
```
python3 tools/build.py
```
This regenerates all the HTML files and `sitemap.xml`. A GitHub Action (`.github/workflows/build.yml`) also rebuilds automatically on every push that touches `tools/`.

## Custom domain
1. Point the DNS for 111176.com to GitHub Pages:
   - A records: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - `www` CNAME: `webworksa1.github.io`
2. Go to Settings → Pages → Custom domain, enter `111176.com`, and enable HTTPS.

## Legal
Original content and code © 2026 111176.com. No trademark is claimed in the number "111176". See `disclaimer.html`.
