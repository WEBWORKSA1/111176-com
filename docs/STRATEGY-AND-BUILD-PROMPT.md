# 111176.com — Strategy, Research Brief & Phase-Wise Build Prompt

> Owner contact is never written in plain text anywhere in this repository. All forms and mail links resolve the owner inbox at runtime from an encoded value in `assets/js/config.js`.

---

## 1. Research brief: what "111176" means

| Angle | Finding | Business implication |
|---|---|---|
| **Established Chinese meaning** | None. No recognised reading of "111176" exists in Chinese sources. | Don't sell a fake "ancient meaning". Build a **decoder brand** that explains *any* number, and use 111176 as the showcase. |
| **Digit 1 (yī / yāo 幺)** | Spoken "yāo" in phone and room numbers. "Yāo" sounds like 要 ("want/will"). "1" = first, unity, leadership. | The domain reads as a "want / first" brand. |
| **"1111"** | 光棍 = four "bare sticks" = singles. This is the origin of **Singles' Day (Double 11)**. Industry GMV: **RMB 1,441.8B (2024)** and **RMB 1,695B ≈ US$238B (2025)** (Syntun). | Gives the site a yearly traffic spike every October–November, plus B2B leads from brands that sell into China. |
| **Digit 7 (qī)** | Mixed. Sounds like 起 ("rise") and 气 ("energy"). It is also the number of Qixi (Chinese Valentine's) and of Ghost Month (lunar month 7). | Good material for evergreen articles. |
| **Digit 6 (liù)** | 六六大顺 ("everything goes smoothly"). **"666"** is huge internet slang meaning "awesome". | The number ends on a positive note. |
| **No 4, no 0** | Chinese domain investors call 6-digit numbers with no 0 and no 4 "premium chips" (无4). There are only 262,144 of them out of 1,000,000 possible 6N .coms. All 6N .coms were hand-registered by Nov 2015. | The domain is liquid in Chinese domain markets. Add a numeric-domain intel/lead section. |
| **6-digit systems** | Chinese postal codes are 6 digits; 111xxx is Liaoyang, Liaoning. The 111xxx range is used for SSE convertible-bond codes. **111176 is not an A-share stock code.** Lucky phone numbers have sold for RMB 2.25M, and HK plate "28" sold for HK$18.1M. | Tools for phone numbers, licence plates, addresses and prices meet real demand. |
| **Trademark** | A general search found no trademark on "111176". It is used only as part and catalogue numbers. Before commercial branding, run manual checks on USPTO and TMview. | Use a generic descriptive brand and publish a disclaimer. |

## 2. The winning idea (decision)

**111176.com = "The Chinese Number Decoder": lucky-number tools + a number-meaning encyclopedia + a Singles' Day/China-commerce hub.**

Why this idea beats the alternatives:

- **Rejected: a pure Singles' Day deals site.** It only gets traffic 6–8 weeks a year, and affiliate programs in China are hard to join.
- **Rejected: a domain marketplace.** Too few buyers, and Sedo and Afternic already own that space.
- **Chosen: tools plus reference content.**
  - Visitors come back year-round.
  - It fits AdSense well: long sessions, many pageviews per visit, broad commercial intent.
  - The results are shareable.
  - It has three lead streams:
    1. **Consumer:** free personalised Lucky Number Report, collected by email.
    2. **B2B, high value:** China-market pricing, launch dates and Singles' Day campaign consults. Agencies pay well for these leads.
    3. **Domain:** numeric-domain appraisal, buy and sell requests, plus inquiries about 111176.com itself.

Revenue stack, in order of expected size:

1. AdSense display ads, placed in-content, below tools and in the sidebar.
2. B2B leads (sold or referred to agencies, or fulfilled directly).
3. YouTube: embedded videos plus your own channel later.
4. Sponsorships and advertising, via the banner at the top of every page.
5. Donations and supporter tiers.
6. Affiliate links (language courses, VPNs for China travel, feng-shui products). Plug in later.

## 3. Competitor audit (29 sites fetched)

Sites fetched:

- yourchineseastrology.com, chinesenewyear.net, numerology.com
- chinahighlights.com (two pages), travelchinaguide.com (three pages)
- sacredscribesangelnumbers, astrology.com, cafeastrology.com, mdbg.net
- ltl-school.com, mandarinzone.com, thechairmansbao.com, lingoace.com
- calculator.net, omnicalculator.com, timeanddate.com
- yoyochinese.com, chinesepod.com, blog.duolingo.com, hanzii.net, trainchinese.com
- alibabagroup.com, wikipedia (Singles' Day), slickdeals.net
- afternic.com (and dan.com, which redirects to it), sedo.com

Patterns adopted:

- **Tool in the hero** (timeanddate, calculator.net). The number decoder is the first thing a visitor sees.
- **Tool input doubles as lead form** (numerology.com). The result is free; email unlocks the full report.
- **Colour semantics:** green = lucky, red = unlucky, amber = mixed (MandarinZone).
- **Page structure:** quick answer → table of contents → content → FAQ → related links (LTL, MandarinZone).
- **Hub-and-spoke internal links** (TravelChinaGuide).
- **Proof strip** of real auction records (Chairman's Bao).
- **Donation next to free tools**, with low-friction preset amounts (MDBG, Sacred Scribes).
- **Contest and draw mechanics** (Slickdeals giveaways).
- **For-sale and lease blocks** on domain pages (Afternic, Sedo).
- **Dark/light toggle** (MDBG). **Zodiac grid** (astrology.com). **Category cards** (Omni).

## 4. Phase-wise build prompt (copy/paste into any AI builder)

### PHASE 0 — Guardrails
> You are building **111176.com**, a static website on the GitHub Pages free plan, using only HTML, CSS and vanilla JS with no build step. Use relative links only, so the site works both at `username.github.io/111176-com/` and at a custom domain. Never print the owner email in any file. Store it encoded in `assets/js/config.js` and decode it at runtime for `mailto:` links and form endpoints. Every page must show a top banner reading "Contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership", linking to `https://web.works/contact`. Do not claim a trademark on "111176". Include a trademark/copyright disclosure page.

### PHASE 1 — Foundation & design system
> Create `assets/css/style.css` with CSS variables for the Chinese-red and gold accents, green/red/amber semantic colours, and a light/dark theme (defaulting to `prefers-color-scheme`, with a toggle that is remembered in localStorage). Build a mobile-first responsive grid, sticky header with dropdown and mobile drawer navigation, and components: card, badge, gauge, tabs, accordion, toast and modal. Also add a skip link, focus rings and reduced-motion support. Create `assets/js/main.js` for: theme, nav, the email decoder, the AJAX form handler (FormSubmit endpoint, honeypot, success toast, redirect to `thank-you.html`), cookie consent, lazy YouTube embeds, share buttons, the ad-slot loader (loads AdSense only when `ADSENSE_CLIENT` is set; otherwise shows a house "Advertise here" ad), countdowns and a newsletter popup that shows at most once every 7 days.

### PHASE 2 — Core tools (the traffic engine)
> 1. **Number Decoder** (`decoder.html`):
>    - Modes: phone, licence plate, address/unit, price, date, domain and free text.
>    - Show a meaning for each digit and each pair, pinyin, a homophone and a 0–100 luck score with a gauge.
>    - Flag "4" and Ghost Month dates.
>    - Offer a copyable result card, share buttons, and email-gated "Full Report".
> 2. **Tools hub** (`tools.html`):
>    - Lucky number generator (seeded by name + birth date).
>    - Number compatibility checker.
>    - Chinese numeral converter: normal, financial (大写 banker's numerals) and pinyin.
>    - Price-ending optimiser.
>    - Numeric-domain pattern scorer.
> 3. **Zodiac** (`zodiac.html`): find the zodiac from a birth date using `Intl.DateTimeFormat('en-u-ca-chinese')`, which handles the lunar new year boundary correctly. Include lucky and unlucky numbers for each of the 12 animals.
> 4. **Lucky Dates** (`lucky-dates.html`): a month calendar scored by digits and lunar month, with festivals marked (5/20, 6/18, 8/8, 11/11, Qixi, Ghost Month), for weddings, moves and openings.

### PHASE 3 — Content (the AdSense approval engine)
> 1. **Dictionary** (`meanings.html`): digits 0–9 plus 60+ number-slang codes (520, 1314, 666, 88, 886, 748, 250…), with live search, category filters and colour coding.
> 2. **Learn hub** (`learn.html`) with long-form original articles:
>    - Why 8 is lucky
>    - Why 4 is avoided
>    - Chinese number slang
>    - Singles' Day explained with GMV data
>    - What 111176 means
>    - Why Chinese buyers value numeric domains
> 3. **Every article** gets: quick-answer box, table of contents, FAQ with FAQPage JSON-LD, sources, a "last updated" date and related links.

### PHASE 4 — Monetization
> 1. **AdSense slots:** below the hero, in-article, below tool results and in the footer. Add `ads.txt` once the publisher ID is known.
> 2. **Videos** (`videos.html`): YouTube gallery using lightweight facade embeds, with a "submit your video" form.
> 3. **Business page** (`business.html`): China-market pricing and launch playbook, Singles' Day countdown, GMV table and a **high-conversion B2B lead form**. It should be multi-step: goal → budget → timeline → contact, with a benefit stack, trust badges and a "reply within 24h" promise.
> 4. **Domains page** (`domains.html`): 6N market explainer, pattern scorer, and appraisal / buy / sell / lease form, plus a "111176.com is open to offers & partnerships" block.

### PHASE 5 — Community & support
> 1. **Support page** (`support.html`) with four areas:
>    - **Donations:** preset tiers $8 / $18 / $88 / $888 (lucky amounts) plus a custom amount. Buttons go to PayPal, Buy Me a Coffee, Ko-fi and GitHub Sponsors (configurable). A pledge form is the fallback.
>    - **Sponsorship packages.**
>    - **Advertise-with-us rate card.**
>    - **Careers / talent hiring form**, for writers, video creators, translators and developers.
> 2. **Contests page** (`contests.html`): current contest ("My Lucky Number Story") with prizes, rules, a countdown, an entry form and a past-winners placeholder.

### PHASE 6 — Trust, legal, SEO
> 1. **Pages:** About, Contact (multi-purpose form), Privacy (AdSense/cookies disclosure), Terms, Disclaimer & Trademark/Copyright disclosure, 404 and Thank-you.
> 2. **Search and sharing:** `sitemap.xml`, `robots.txt`, `manifest.webmanifest`, favicon, OG image, WebSite and Organization JSON-LD, and canonical URLs.
> 3. **Quality bars:** Lighthouse ≥ 90 and WCAG AA contrast.

### PHASE 7 — Launch & growth
> 1. Enable GitHub Pages (Settings → Pages → Deploy from branch → `main` / root).
> 2. Point 111176.com DNS to GitHub Pages. Add the `CNAME` file only after DNS is live.
> 3. Submit the sitemap to Google Search Console. Apply for AdSense after 15–30 days of indexed content.
> 4. Publish 2 articles a week. Run a Singles' Day campaign every October, and a 520 campaign every May.

## 5. Configuration checklist (`assets/js/config.js`)
- `ADSENSE_CLIENT`: your `ca-pub-…` ID. Also create `ads.txt` with `google.com, pub-XXXX, DIRECT, f08c47fec0942fa0`.
- `ADSENSE_SLOTS`: optional slot IDs.
- `DONATE`: PayPal.me, Buy Me a Coffee, Ko-fi and GitHub Sponsors URLs.
- `YOUTUBE_CHANNEL`: your channel URL.
- `GA_ID`: optional GA4 ID.
- Forms use FormSubmit. The **first** submission sends a one-time activation email to the owner inbox; click "Activate" once. After that, you can optionally replace the encoded email with the random alias FormSubmit gives you (`FORM_ALIAS`).
