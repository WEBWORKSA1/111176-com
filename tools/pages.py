from build import ad, breadcrumb, report_form, newsletter_inline, faq_schema, faq_html, INQUIRY

VIDEOS = [
    ("wf13M4MoHS4", "Chinese Lucky and Unlucky Numbers Explained", "Learn Chinese Now", "numbers"),
    ("pT52hREAf18", "Chinese Lucky Numbers", "Numberphile", "numbers"),
    ("sr673iAqLZY", "Meanings Behind Chinese Numbers", "YouTube", "numbers"),
    ("QwvlAbisiRc", "Most Lucky and Unlucky Numbers for Chinese People", "YouTube", "numbers"),
    ("Gx8AGhl8O9A", "Facts About Chinese Lucky & Unlucky Numbers and Colours", "YouTube", "numbers"),
    ("jxKWegGb-3I", "Chinese Lucky Numbers and Meanings", "Ziggy Natural", "numbers"),
    ("neHuJ34H5wY", "China’s Singles Day Explained", "YouTube", "commerce"),
    ("rqylW0IEufU", "Nov. 11 Is Singles’ Day, the Biggest Retail Holiday in the World", "YouTube", "commerce"),
    ("07M9H2FdlDg", "11.11 Singles’ Day — Episode 1", "YouTube", "commerce"),
]

def video_cards(r, items):
    return "".join(f'<div class="card" style="padding:12px"><div class="video" data-id="{i}" data-title="{t}"></div><h3 style="font-size:1rem;margin:10px 0 2px">{t}</h3><p class="small muted" style="margin:0">{c} · <a href="https://www.youtube.com/watch?v={i}" target="_blank" rel="noopener">Watch on YouTube</a></p></div>' for i, t, c, _ in items)

DECODER = '''<div data-decoder {attrs}>
  <div class="seg" role="group" aria-label="What are you checking?">
    <button type="button" data-mode="any" aria-pressed="true">Any number</button><button type="button" data-mode="phone" aria-pressed="false">📱 Phone</button><button type="button" data-mode="plate" aria-pressed="false">🚗 Plate</button><button type="button" data-mode="address" aria-pressed="false">🏠 Address</button><button type="button" data-mode="price" aria-pressed="false">🏷️ Price</button><button type="button" data-mode="date" aria-pressed="false">📅 Date</button><button type="button" data-mode="domain" aria-pressed="false">🌐 Domain</button>
  </div>
  <form class="input-group" role="search"><label class="skip" for="dec-{id}">Number</label><input id="dec-{id}" inputmode="text" placeholder="e.g. 111176, 5201314" autocomplete="off"><button class="btn btn-primary" type="submit">Decode →</button></form>
  <div class="result" aria-live="polite"></div>
</div>'''

def decoder(id_, attrs=""):
    return DECODER.replace("{attrs}", attrs).replace("{id}", id_)

def build():
    P = []
    r = ""
    # ---------------- HOME ----------------
    home_faq = [
        ("What is the luckiest number in Chinese culture?", "8 (bā), because it sounds like 发 (fā), “to prosper”. 6 (smooth) and 9 (long-lasting) are close behind."),
        ("Why do Chinese people avoid the number 4?", "4 (sì) sounds almost identical to 死 (sǐ), “death”. Many buildings in China skip floors 4, 14 and 24."),
        ("What does 520 mean?", "520 (wǔ èr líng) sounds like 我爱你 (wǒ ài nǐ), “I love you”. May 20 has become an unofficial online Valentine’s Day in China."),
        ("Is the Number Decoder free?", "Yes. Every tool on 111176 is free and needs no registration. The optional emailed report is free too."),
        ("Does 111176 have a traditional meaning?", "No established reading exists. It combines 1111 (Singles’ Day), 7 (rise/energy) and 6 (smooth flow) with no 4 — see our full breakdown."),
    ]
    body = f'''
<section class="hero">
  <div class="container split">
    <div>
      <span class="eyebrow">Free Chinese number intelligence</span>
      <h1>Decode <span>any number</span> the way China reads it.</h1>
      <p class="lead">Phone numbers, licence plates, prices, dates, addresses, domains — see the hidden meaning, the luck score and luckier alternatives in one second.</p>
      <div class="stat-row"><div class="stat"><b>10</b><span>digits decoded</span></div><div class="stat"><b>65+</b><span>number phrases</span></div><div class="stat"><b>12</b><span>zodiac profiles</span></div><div class="stat"><b>6</b><span>free tools</span></div></div>
    </div>
    <div class="hero-tool">
      <h2 style="font-size:1.25rem">🔢 What does your number mean?</h2>
      {decoder("home", 'data-demo="111176"')}
    </div>
  </div>
</section>
{ad()}
<section>
  <div class="container">
    <div class="section-head"><span class="eyebrow">Tools</span><h2>Everything you need to choose lucky numbers</h2><p class="lead">Built for travellers, couples, sellers, marketers and domain investors.</p></div>
    <div class="grid g3">
      <a class="card" href="decoder.html"><div class="ico">🔢</div><h3>Number Decoder</h3><p class="muted">Digit-by-digit meanings, hidden phrases, a luck score and better swaps.</p></a>
      <a class="card" href="meanings.html"><div class="ico">📖</div><h3>Number Dictionary</h3><p class="muted">520, 1314, 666, 88, 250, 748… 65+ codes with search and filters.</p></a>
      <a class="card" href="zodiac.html"><div class="ico">🐉</div><h3>Zodiac &amp; Lucky Numbers</h3><p class="muted">Find your true sign (lunar-calendar accurate) and its lucky digits.</p></a>
      <a class="card" href="lucky-dates.html"><div class="ico">📅</div><h3>Lucky Dates Calendar</h3><p class="muted">Weddings, moves, launches — with Ghost Month and festivals flagged.</p></a>
      <a class="card" href="tools.html#converter"><div class="ico">🀄</div><h3>Chinese Numeral Converter</h3><p class="muted">Standard, financial (大写) and cheque formats with pinyin.</p></a>
      <a class="card" href="tools.html#domain"><div class="ico">🌐</div><h3>Numeric Domain Scorer</h3><p class="muted">Grade 4N/5N/6N domains the way Chinese buyers do.</p></a>
    </div>
  </div>
</section>
<section class="section-alt">
  <div class="container split">
    <div>
      <span class="eyebrow">The digits at a glance</span>
      <h2>Lucky, unlucky and “it depends”</h2>
      <p>Chinese number luck is mostly about <strong>sound</strong>. A digit is lucky when it sounds like a good word and unlucky when it sounds like a bad one. That’s why 8 (sounds like “prosper”) is everywhere, and 4 (sounds like “death”) goes missing from lift buttons.</p>
      <a class="btn btn-primary" href="meanings.html">Open the full dictionary</a>
    </div>
    <div class="table-wrap"><table><thead><tr><th>Digit</th><th>Sounds like</th><th>Verdict</th></tr></thead><tbody>
      <tr><td><b>8</b> 八 bā</td><td>发 — prosper</td><td><span class="badge good">Luckiest</span></td></tr>
      <tr><td><b>6</b> 六 liù</td><td>溜 — smooth</td><td><span class="badge good">Lucky</span></td></tr>
      <tr><td><b>9</b> 九 jiǔ</td><td>久 — long-lasting</td><td><span class="badge good">Lucky</span></td></tr>
      <tr><td><b>2</b> 二 èr</td><td>好事成双 — pairs</td><td><span class="badge good">Good</span></td></tr>
      <tr><td><b>1</b> 一 yāo</td><td>要 — want</td><td><span class="badge mid">Neutral+</span></td></tr>
      <tr><td><b>7</b> 七 qī</td><td>起 rise / 气 anger</td><td><span class="badge mid">Mixed</span></td></tr>
      <tr><td><b>4</b> 四 sì</td><td>死 — death</td><td><span class="badge bad">Avoid</span></td></tr>
    </tbody></table></div>
  </div>
</section>
<section>
  <div class="container">
    <div class="section-head"><span class="eyebrow">Real money, real numbers</span><h2>Why number luck is serious business</h2></div>
    <div class="grid g4">
      <div class="card center"><div class="big-number" style="font-size:2.2rem">¥1.69T</div><p class="small muted">Double 11 (11.11) industry GMV in 2025, ≈ US$238B (Syntun estimate)</p></div>
      <div class="card center"><div class="big-number" style="font-size:2.2rem">¥2.25M</div><p class="small muted">Paid for a Chinese mobile number ending in five 8s (2020 court auction)</p></div>
      <div class="card center"><div class="big-number" style="font-size:2.2rem">HK$18.1M</div><p class="small muted">Hong Kong licence plate “28” — “easy prosperity” in Cantonese (2016)</p></div>
      <div class="card center"><div class="big-number" style="font-size:2.2rem">262,144</div><p class="small muted">6-digit .com domains with no 0 and no 4 — the “premium chip” pool</p></div>
    </div>
    <p class="center small muted" style="margin-top:14px">Sources on each guide page. <a href="learn/singles-day-11-11.html">Singles’ Day data</a> · <a href="learn/numeric-domains-china.html">Numeric domain market</a></p>
  </div>
</section>
{ad()}
<section class="section-alt">
  <div class="container split">
    <div>
      <span class="eyebrow">For brands &amp; sellers</span>
      <h2>Selling to Chinese customers? Get the numbers right.</h2>
      <p>Price endings, launch dates, SKU codes, hotline numbers and Singles’ Day timing all affect conversion with Chinese-speaking buyers. Tell us your goal. A specialist replies within 24 hours with a free action plan.</p>
      <ul><li>Price-point and promo-code optimisation (8, 88, 168, 518)</li><li>Launch-date selection and Double 11 / 618 / 520 campaign calendars</li><li>Brand-name and phone/hotline number audits</li></ul>
      <a class="btn btn-primary" href="business.html#consult">Get my free China-numbers plan →</a>
    </div>
    <div class="card"><h3>⏳ Next Singles’ Day (11.11)</h3><div class="countdown" data-countdown="11-11"></div><p class="small muted" style="margin-top:10px">Brands start planning 6–8 weeks ahead. <a href="learn/singles-day-11-11.html">Read the guide →</a></p></div>
  </div>
</section>
<section>
  <div class="container">
    <div class="section-head"><span class="eyebrow">Watch</span><h2>Learn number culture in 5 minutes</h2></div>
    <div class="grid g3">{video_cards(r, VIDEOS[:3])}</div>
    <p class="center" style="margin-top:18px"><a class="btn btn-ghost" href="videos.html">More videos</a></p>
  </div>
</section>
<section class="section-alt">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Guides</span><h2>Popular reads</h2></div>
    <div class="grid g3">
      <a class="card" href="learn/why-8-is-lucky.html"><span class="badge gold">Culture</span><h3 style="margin-top:8px">Why 8 is the luckiest number</h3><p class="muted small">From the 08/08/08 Olympics to ¥-million phone numbers.</p></a>
      <a class="card" href="learn/chinese-number-slang.html"><span class="badge gold">Slang</span><h3 style="margin-top:8px">520, 666, 88: Chinese number slang</h3><p class="muted small">How to read the codes Chinese speakers text every day.</p></a>
      <a class="card" href="learn/meaning-of-111176.html"><span class="badge gold">Decoded</span><h3 style="margin-top:8px">What does 111176 mean?</h3><p class="muted small">An honest, digit-by-digit breakdown of our name.</p></a>
    </div>
  </div>
</section>
<section><div class="container">{report_form(r)}</div></section>
<section class="section-alt">
  <div class="container grid g3">
    <a class="card" href="contests.html"><div class="ico">🏆</div><h3>Win prizes</h3><p class="muted">Enter the “My Lucky Number Story” contest — cash and gift prizes.</p></a>
    <a class="card" href="support.html"><div class="ico">🧧</div><h3>Support 111176</h3><p class="muted">Keep the tools free. Give a lucky $8, $18 or $88.</p></a>
    <a class="card" href="support.html#careers"><div class="ico">💼</div><h3>Work with us</h3><p class="muted">We hire writers, translators, video creators and developers.</p></a>
  </div>
</section>
<section>
  <div class="container" style="max-width:820px">
    <div class="section-head"><h2>FAQ</h2></div>
    {faq_html(home_faq)}
  </div>
</section>'''
    P.append(dict(path="index.html", title="111176 — Chinese Number Meanings, Lucky Number Decoder & Tools",
                  desc="Free Chinese number decoder: find the meaning and luck score of any phone number, plate, price, date or domain. Number slang dictionary, zodiac lucky numbers, lucky dates and guides.",
                  body=body, schema=[faq_schema(home_faq)]))

    # ---------------- DECODER ----------------
    dfaq = [
        ("How is the luck score calculated?", "Each digit gets a weight based on its traditional sound association (8, 6, 9 up; 4 down). We then add bonuses or penalties for known phrases (520, 168, 748…), repeating runs and the ending digit. The result is scaled to 1–99."),
        ("Can I check a Chinese licence plate?", "Yes. Choose Plate and type the plate. Letters are ignored and the digits are analysed."),
        ("Why is 1 read as “yāo”?", "In phone, room and bus numbers Chinese speakers say “yāo” (幺) for 1 so it isn’t confused with 7 (qī)."),
        ("Is this scientific?", "No. It is a cultural reading of how numbers sound in Chinese — useful for marketing, gifting and etiquette, not for predicting the future."),
    ]
    body = f'''
<section class="hero"><div class="container">
  {breadcrumb(r, [("decoder.html", "Number Decoder")])}
  <div class="with-side">
    <div>
      <h1>Chinese Number Decoder</h1>
      <p class="lead">Paste any number. See its meaning in Chinese culture, the hidden phrases inside it, a 1–99 luck score and luckier alternatives.</p>
      <div class="hero-tool">{decoder("main", "data-autoload")}</div>
      {ad()}
      <h2>How to read your result</h2>
      <p><strong>Green digits</strong> sound like good words (8 = prosper, 6 = smooth, 9 = lasting). <strong>Red digits</strong> sound like bad ones (4 = death). <strong>Amber</strong> means mixed or neutral. “Hidden phrases” are well-known number codes found inside your number, like <a href="meanings.html#n-168">168</a> (prosperity all the way) or <a href="meanings.html#n-748">748</a> (a rude insult).</p>
      <h3>Best uses</h3>
      <div class="grid g2">
        <div class="card"><h4>📱 Choosing a phone number</h4><p class="small muted">End on 8, 6 or 9. Avoid 4 and 14. Numbers with 168/518/888 are premium in China.</p></div>
        <div class="card"><h4>🏷️ Pricing for Chinese buyers</h4><p class="small muted">Prices ending in 8 or 88 read as “prosperous”. Avoid prices containing 4.</p></div>
        <div class="card"><h4>📅 Picking a date</h4><p class="small muted">Use Date mode to flag Ghost Month (lunar month 7) and find the lunar date.</p></div>
        <div class="card"><h4>🌐 Buying numeric domains</h4><p class="small muted">Domain mode shows pattern codes (AAAABC) and 无4 status used by Chinese investors.</p></div>
      </div>
      <h2>FAQ</h2>{faq_html(dfaq)}
    </div>
    <aside>
      <div class="card"><h3>🔥 Try these</h3><ul class="pill-list"><li><a href="?n=111176">111176</a></li><li><a href="?n=5201314">5201314</a></li><li><a href="?n=168">168</a></li><li><a href="?n=8888">8888</a></li><li><a href="?n=1314">1314</a></li><li><a href="?n=748">748</a></li><li><a href="?n=13888886666">13888886666</a></li></ul></div>
      {ad(cls="side")}
      <div class="card" style="margin-top:20px"><h3>📬 Weekly lucky number</h3>{newsletter_inline(r, "newsletter")}</div>
    </aside>
  </div>
</div></section>
<section><div class="container">{report_form(r)}</div></section>'''
    app = {"@context": "https://schema.org", "@type": "WebApplication", "name": "Chinese Number Decoder", "applicationCategory": "UtilitiesApplication", "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}}
    P.append(dict(path="decoder.html", title="Chinese Number Decoder — Meaning & Luck Score of Any Number",
                  desc="Decode any phone number, licence plate, price, address, date or domain using Chinese number meanings. Free luck score, hidden phrases and luckier alternatives.",
                  body=body, schema=[app, faq_schema(dfaq)]))

    # ---------------- TOOLS HUB ----------------
    body = f'''
<section class="hero"><div class="container">
  {breadcrumb(r, [("tools.html", "Number Tools")])}
  <h1>Chinese Number Tools</h1>
  <p class="lead">Six free tools. No sign-up. They work on your phone.</p>
  <ul class="pill-list"><li><a href="decoder.html">Decoder</a></li><li><a href="#generator">Lucky Generator</a></li><li><a href="#compat">Compatibility</a></li><li><a href="#converter">Numeral Converter</a></li><li><a href="#domain">Domain Scorer</a></li><li><a href="zodiac.html">Zodiac</a></li><li><a href="lucky-dates.html">Lucky Dates</a></li></ul>
</div></section>
<section id="generator"><div class="container split" style="align-items:start">
  <div><span class="eyebrow">Tool 1</span><h2>Lucky Number Generator</h2><p>Creates personal lucky numbers from your name and birth date. It uses your zodiac sign’s lucky digits, skips its unlucky ones and never uses 4. The same inputs always give the same numbers.</p></div>
  <div class="card"><form id="gen-form"><div class="field"><label for="gen-name">Your name</label><input id="gen-name" required placeholder="e.g. Li Wei"></div><div class="row"><div class="field"><label for="gen-dob">Birth date</label><input id="gen-dob" type="date"></div><div class="field"><label for="gen-len">Length</label><select id="gen-len"><option>3</option><option>4</option><option selected>6</option><option>8</option><option>11</option></select></div></div><button class="btn btn-primary btn-block">Generate</button></form><div id="gen-out" class="result"></div></div>
</div></section>
{ad()}
<section id="compat" class="section-alt"><div class="container split" style="align-items:start">
  <div><span class="eyebrow">Tool 2</span><h2>Number Compatibility</h2><p>Compare two numbers — two phone numbers, two birthdays (as YYYYMMDD) or a couple’s anniversary against a house number. The harmony score combines individual luck, shared digits and root numbers.</p></div>
  <div class="card"><form id="comp-form"><div class="row"><div class="field"><label for="comp-a">Number A</label><input id="comp-a" required placeholder="19900808"></div><div class="field"><label for="comp-b">Number B</label><input id="comp-b" required placeholder="19920606"></div></div><button class="btn btn-primary btn-block">Check harmony</button></form><div id="comp-out" class="result"></div></div>
</div></section>
<section id="converter"><div class="container split" style="align-items:start">
  <div><span class="eyebrow">Tool 3</span><h2>Chinese Numeral Converter</h2><p>Convert Arabic numbers into standard Chinese (一二三), <strong>financial numerals</strong> (壹贰叁 — used on cheques and invoices so the figures can’t be altered), RMB cheque format and pinyin.</p></div>
  <div class="card"><form id="conv-form"><div class="field"><label for="conv-in">Number</label><input id="conv-in" required placeholder="111176 or 8888.88" inputmode="decimal"></div><button class="btn btn-primary btn-block">Convert</button></form><div id="conv-out" class="result"></div></div>
</div></section>
<section id="domain" class="section-alt"><div class="container split" style="align-items:start">
  <div><span class="eyebrow">Tool 4</span><h2>Numeric Domain Scorer</h2><p>Grades all-numeric domains the way Chinese investors look at them: length class (4N/5N/6N), pattern code (AABB, AAAABC), <em>无4</em> (no 4), no 0, lucky digits and extension.</p><p><a href="learn/numeric-domains-china.html">Why Chinese buyers love numeric domains →</a></p></div>
  <div class="card"><form id="dom-form"><div class="field"><label for="dom-in">Domain</label><input id="dom-in" required placeholder="111176.com"></div><button class="btn btn-primary btn-block">Score domain</button></form><div id="dom-out" class="result"></div></div>
</div></section>
<section><div class="container grid g2">
  <a class="card" href="zodiac.html"><div class="ico">🐉</div><h3>Tool 5 · Zodiac Finder</h3><p class="muted">Lunar-calendar accurate sign, element and lucky numbers.</p></a>
  <a class="card" href="lucky-dates.html"><div class="ico">📅</div><h3>Tool 6 · Lucky Dates Calendar</h3><p class="muted">Monthly calendar scored for weddings, moves and openings.</p></a>
</div></section>
{ad()}
<section><div class="container">{report_form(r)}</div></section>'''
    P.append(dict(path="tools.html", title="Free Chinese Number Tools — Generator, Converter, Domain Scorer",
                  desc="Lucky number generator, number compatibility checker, Chinese and financial numeral converter (大写) and numeric domain scorer. Free, no sign-up.", body=body))

    # ---------------- ZODIAC ----------------
    zfaq = [("Why does my zodiac sign differ from websites that use the year only?", "The Chinese zodiac year starts at Lunar New Year (between 21 January and 20 February), not 1 January. If you were born in January or early February you may belong to the previous year’s sign. Our finder uses the Chinese calendar built into your browser."),
            ("Are zodiac lucky numbers the same everywhere?", "No. Traditional sources differ slightly. We list the most commonly cited digits for each sign.")]
    body = f'''
<section class="hero"><div class="container">
  {breadcrumb(r, [("zodiac.html", "Zodiac & Lucky Numbers")])}
  <h1>Chinese Zodiac Lucky Numbers</h1>
  <p class="lead">Enter your birth date to find your true zodiac sign, element and lucky numbers. It is exact to the lunar calendar.</p>
  <div class="card" style="max-width:640px"><form id="zodiac-form" class="input-group"><label class="skip" for="z-dob">Birth date</label><input id="z-dob" type="date" required><button class="btn btn-primary">Find my sign</button></form></div>
</div></section>
<section><div class="container">
  <h2>Or pick a sign</h2>
  <div class="zodiac-grid" id="zodiac-grid"></div>
  <div id="zodiac-out" style="margin-top:20px"></div>
</div></section>
{ad()}
<section class="section-alt"><div class="container">
  <h2>Lucky &amp; unlucky numbers by sign</h2>
  <div class="table-wrap" data-zodiac-table></div>
  <p class="small muted" style="margin-top:10px">Compiled from commonly cited traditional Chinese astrology references. For entertainment.</p>
</div></section>
<section><div class="container" style="max-width:820px"><h2>FAQ</h2>{faq_html(zfaq)}</div></section>
<section><div class="container">{report_form(r, "Get your zodiac lucky-number report", "Your sign’s best phone-number endings, dates for the next 90 days and colours — free by email.")}</div></section>'''
    P.append(dict(path="zodiac.html", title="Chinese Zodiac Lucky Numbers — Accurate Sign Finder",
                  desc="Find your Chinese zodiac sign by exact birth date (lunar-calendar accurate), plus lucky and unlucky numbers for all 12 animals.", body=body, schema=[faq_schema(zfaq)]))

    # ---------------- LUCKY DATES ----------------
    body = f'''
<section class="hero"><div class="container">
  {breadcrumb(r, [("lucky-dates.html", "Lucky Dates Calendar")])}
  <h1>Lucky Dates Calendar</h1>
  <p class="lead">Pick a month and a purpose. Every day is scored by its digits and lunar date. Ghost Month is penalised, and Qixi, Mid-Autumn, 520 and 11.11 are marked.</p>
  <div class="card"><div class="row"><div class="field"><label for="cal-month">Month</label><input id="cal-month" type="month"></div><div class="field"><label for="cal-purpose">Purpose</label><select id="cal-purpose"><option value="general">General</option><option value="wedding">Wedding / engagement</option><option value="business">Business opening / launch</option><option value="move">Moving house</option></select></div></div>
  <p id="cal-best"></p>
  <div class="cal" id="cal" aria-live="polite"></div>
  <p class="small muted" style="margin-top:12px"><span class="badge good">green</span> auspicious · <span class="badge mid">amber</span> neutral · <span class="badge bad">red</span> avoid. “L7/15” = lunar month 7, day 15. Traditional almanacs (黄历) use extra factors. For big events, request a personal reading.</p></div>
</div></section>
{ad()}
<section><div class="container">{report_form(r, "Get 3 hand-picked lucky dates", "Tell us the event and your birth dates. We’ll email the three best dates in your window, free.")}</div></section>'''
    P.append(dict(path="lucky-dates.html", title="Lucky Dates Calendar — Auspicious Days for Weddings, Moves & Launches",
                  desc="Free Chinese lucky dates calendar. Scores every day by number meaning and lunar date, flags Ghost Month and festivals. For weddings, moving and business openings.", body=body))

    # ---------------- MEANINGS ----------------
    mfaq = [("What does 1314 mean in Chinese?", "1314 (yī sān yī sì) sounds like 一生一世 (yì shēng yí shì), “one life, one world” — forever. 5201314 means “I love you forever”."),
            ("What does 666 mean?", "666 (liù liù liù) is internet slang for “awesome” or “skilful”. It comes from 溜 (liù), meaning smooth or slick. Unlike in the West, it is positive."),
            ("What does 88 mean in Chinese texting?", "88 (bā bā) sounds like “bye-bye”. It also means double prosperity."),
            ("What does 250 mean?", "二百五 (èr bǎi wǔ) is an insult meaning idiot or fool. Avoid it in prices and gifts.")]
    body = f'''
<section class="hero"><div class="container">
  {breadcrumb(r, [("meanings.html", "Number Meanings")])}
  <h1>Chinese Number Meanings Dictionary</h1>
  <p class="lead">Every digit plus 65+ number codes Chinese speakers use for love, luck, money and online slang. Search or filter.</p>
</div></section>
<section style="padding-top:0"><div class="container with-side" id="dict">
  <div>
    <div class="dict-controls"><label class="skip" for="dict-q">Search</label><input id="dict-q" type="search" placeholder="Search a number or word (e.g. 520, love, money)"></div>
    <div class="seg" role="group" aria-label="Filter"><button type="button" data-cat="all" aria-pressed="true">All</button><button type="button" data-cat="digit" aria-pressed="false">Digits 0–9</button><button type="button" data-cat="love" aria-pressed="false">❤️ Love</button><button type="button" data-cat="prosperity" aria-pressed="false">💰 Prosperity</button><button type="button" data-cat="internet" aria-pressed="false">💬 Internet slang</button><button type="button" data-cat="warning" aria-pressed="false">⚠️ Avoid</button><button type="button" data-cat="festival" aria-pressed="false">🎉 Festivals</button></div>
    <p class="small muted" id="dict-count"></p>
    <div class="grid" id="dict-list"></div>
    <h2 style="margin-top:36px">FAQ</h2>{faq_html(mfaq)}
  </div>
  <aside>
    <div class="card"><h3>Decode your own</h3>{decoder("side")}</div>
    {ad(cls="side")}
    <div class="card"><h3>Suggest a number code</h3><form class="js-form" id="suggest" data-subject="Dictionary suggestion" data-next="stay"><input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true"><div class="field"><label for="sg-n">Number</label><input id="sg-n" name="number" required></div><div class="field"><label for="sg-m">Meaning</label><input id="sg-m" name="meaning" required></div><div class="field"><label for="sg-e">Your email (optional, for credit)</label><input id="sg-e" name="email" type="email"></div><button class="btn btn-ghost btn-block">Submit</button></form></div>
  </aside>
</div></section>
{ad()}'''
    P.append(dict(path="meanings.html", title="Chinese Number Meanings — 520, 1314, 666, 88 & 65+ Codes",
                  desc="Searchable dictionary of Chinese number meanings and slang: 520 (I love you), 1314 (forever), 666 (awesome), 88 (bye), 250 (idiot) and every digit 0–9.", body=body, schema=[faq_schema(mfaq)]))

    # ---------------- VIDEOS ----------------
    body = f'''
<section class="hero"><div class="container">
  {breadcrumb(r, [("videos.html", "Videos")])}
  <h1>Videos: Chinese Numbers, Luck &amp; 11.11</h1>
  <p class="lead">Hand-picked explainers. Videos load only when you press play, so the page stays fast and private.</p>
  <div class="seg"><a class="btn btn-primary btn-sm" href="#numbers">Numbers &amp; luck</a> <a class="btn btn-ghost btn-sm" href="#commerce">Singles’ Day &amp; commerce</a> <a class="btn btn-ghost btn-sm" href="#submit">Submit a video</a></div>
</div></section>
<section id="numbers"><div class="container"><h2>Numbers &amp; luck</h2><div class="grid g3">{video_cards(r, [v for v in VIDEOS if v[3]=="numbers"])}</div></div></section>
{ad()}
<section id="commerce" class="section-alt"><div class="container"><h2>Singles’ Day &amp; China commerce</h2><div class="grid g3">{video_cards(r, [v for v in VIDEOS if v[3]=="commerce"])}</div></div></section>
<section id="submit"><div class="container split">
  <div><span class="eyebrow">Creators</span><h2>Get your video featured</h2><p>Made a great video about Chinese numbers, lucky culture or China e-commerce? Submit it. Featured creators get a backlink and a spot in our newsletter. Sponsored placements are available.</p><p><a href="{INQUIRY}" target="_blank" rel="noopener">Sponsor the video hub →</a></p></div>
  <form class="card js-form" id="video-submit" data-subject="Video submission"><input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
    <div class="field"><label for="vs-url">YouTube URL</label><input id="vs-url" name="video_url" type="url" required placeholder="https://www.youtube.com/watch?v=…"></div>
    <div class="row"><div class="field"><label for="vs-name">Channel name</label><input id="vs-name" name="channel" required></div><div class="field"><label for="vs-email">Email</label><input id="vs-email" name="email" type="email" required></div></div>
    <div class="field"><label for="vs-why">Why it’s a fit</label><textarea id="vs-why" name="notes"></textarea></div>
    <label class="check"><input type="checkbox" name="interested_in_sponsored" value="yes"> I’m interested in a sponsored placement</label>
    <button class="btn btn-primary btn-block" style="margin-top:10px">Submit video</button></form>
</div></section>'''
    vschema = [{"@context": "https://schema.org", "@type": "VideoObject", "name": t, "description": t, "thumbnailUrl": f"https://i.ytimg.com/vi/{i}/hqdefault.jpg", "embedUrl": f"https://www.youtube.com/embed/{i}", "uploadDate": "2020-01-01"} for i, t, c, _ in VIDEOS[:3]]
    P.append(dict(path="videos.html", title="Videos — Chinese Lucky Numbers & Singles’ Day Explained",
                  desc="Watch the best short explainers on Chinese lucky and unlucky numbers, number slang and Singles’ Day (11.11). Submit your own video.", body=body))

    # ---------------- LEARN HUB ----------------
    from articles import ARTICLES
    cards = "".join(f'<a class="card" href="learn/{a["slug"]}.html"><span class="badge gold">{a["tag"]}</span><h3 style="margin-top:8px">{a["h1"]}</h3><p class="muted small">{a["desc"]}</p><span class="small">{a["mins"]} min read →</span></a>' for a in ARTICLES)
    body = f'''
<section class="hero"><div class="container">
  {breadcrumb(r, [("learn.html", "Guides")])}
  <h1>Guides to Chinese Number Culture</h1>
  <p class="lead">Researched, sourced and written in plain English. New guides every week. <a href="#newsletter-learn">Get them by email</a>.</p>
</div></section>
<section style="padding-top:0"><div class="container"><div class="grid g3">{cards}</div></div></section>
{ad()}
<section class="section-alt" id="newsletter-learn"><div class="container" style="max-width:720px;text-align:center"><h2>New guide every week</h2><p class="muted">Plus your weekly lucky number. Free.</p>{newsletter_inline(r, "newsletter-learn-f")}</div></section>'''
    P.append(dict(path="learn.html", title="Chinese Number Culture Guides — Lucky Numbers, Slang & 11.11",
                  desc="In-depth guides on why 8 is lucky, why 4 is avoided, Chinese number slang, Singles' Day and numeric domains.", body=body))

    from pages_b import build as build_b
    return P + build_b()
