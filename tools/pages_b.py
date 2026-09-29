from build import ad, breadcrumb, report_form, newsletter_inline, faq_schema, faq_html, INQUIRY, UPDATED

HP = '<input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">'

def build():
    P = []
    r = ""
    # ---------------- BUSINESS (B2B lead gen) ----------------
    bfaq = [("Is the consultation really free?", "Yes. The first action plan is free. If you want us to run the work — pricing tests, launch calendars, campaign copy or partner introductions — we quote a fixed fee."),
            ("Who is this for?", "E-commerce sellers, DTC brands, marketplaces, real-estate developers, restaurants, auto dealers and agencies that sell to Chinese-speaking customers in China, Hong Kong, Taiwan, Singapore, Malaysia or the global diaspora."),
            ("How fast do you reply?", "Within 24 hours on business days.")]
    body = f'''
<section class="hero"><div class="container split">
  <div>
    {breadcrumb(r, [("business.html", "For Business")])}
    <span class="eyebrow">For brands, sellers &amp; agencies</span>
    <h1>Win Chinese customers with the <span style="color:var(--red)">right numbers</span>.</h1>
    <p class="lead">Chinese-speaking shoppers notice numbers: prices, dates, phone lines, unit numbers and promo codes. Double 11 alone generated an estimated ¥1.69 trillion (≈US$238B) in 2025. Getting the numbers right is cheap, and it pays.</p>
    <ul>
      <li>✅ <strong>Price-point audit:</strong> endings in 8/88/168, and no 4s in prices or SKUs</li>
      <li>✅ <strong>Launch &amp; campaign calendar:</strong> 520, 618, Qixi, 11.11, 12.12 and Lunar New Year</li>
      <li>✅ <strong>Number assets:</strong> hotline, WeChat ID, address and unit numbers, licence plates</li>
      <li>✅ <strong>Numeric domains and brand names</strong> for the Chinese market</li>
    </ul>
    <div class="trust" style="color:var(--muted)"><span>⏱ Reply within 24h</span><span>🔒 Confidential</span><span>🆓 Free first plan</span></div>
  </div>
  <div class="card" id="consult" data-steps>
    <h2 style="font-size:1.3rem">Get your free China-numbers plan</h2>
    <div class="steps"><span></span><span></span><span></span></div>
    <form class="js-form" id="b2b" data-subject="B2B lead — China numbers plan">
      {HP}<input type="hidden" name="form" value="Business consultation">
      <div class="step">
        <p><strong>1. What do you need?</strong></p>
        <div class="choice-grid">
          <label class="choice"><input type="checkbox" name="needs" value="Pricing"> 🏷️ Pricing</label>
          <label class="choice"><input type="checkbox" name="needs" value="Launch dates / 11.11"> 📅 Launch / 11.11</label>
          <label class="choice"><input type="checkbox" name="needs" value="Brand / domain"> 🌐 Brand / domain</label>
          <label class="choice"><input type="checkbox" name="needs" value="Phone / address numbers"> 📱 Phone / address</label>
          <label class="choice"><input type="checkbox" name="needs" value="Marketing campaign"> 📣 Campaign</label>
          <label class="choice"><input type="checkbox" name="needs" value="Other"> ✨ Other</label>
        </div>
        <div class="field"><label for="b-ind">Industry</label><select id="b-ind" name="industry" required><option value="">Choose…</option><option>E-commerce / DTC</option><option>Retail / restaurant</option><option>Real estate</option><option>Automotive</option><option>Finance / insurance</option><option>Travel / hospitality</option><option>Agency</option><option>Other</option></select></div>
        <button type="button" class="btn btn-primary btn-block" data-next-step>Next →</button>
      </div>
      <div class="step">
        <p><strong>2. Scope</strong></p>
        <div class="field"><label for="b-mkt">Target market</label><select id="b-mkt" name="market" required><option value="">Choose…</option><option>Mainland China</option><option>Hong Kong / Macau</option><option>Taiwan</option><option>Singapore / Malaysia</option><option>Chinese diaspora (US/CA/UK/AU)</option><option>Multiple</option></select></div>
        <div class="field"><label for="b-bud">Monthly marketing budget</label><select id="b-bud" name="budget" required><option value="">Choose…</option><option>Under $1k</option><option>$1k–$5k</option><option>$5k–$25k</option><option>$25k–$100k</option><option>$100k+</option></select></div>
        <div class="field"><label for="b-time">Timeline</label><select id="b-time" name="timeline"><option>This month</option><option>Before 11.11</option><option>Next quarter</option><option>Just exploring</option></select></div>
        <div class="row"><button type="button" class="btn btn-ghost" data-prev-step>← Back</button><button type="button" class="btn btn-primary" data-next-step>Next →</button></div>
      </div>
      <div class="step">
        <p><strong>3. Where should we send your plan?</strong></p>
        <div class="row"><div class="field"><label for="b-name">Name</label><input id="b-name" name="name" required autocomplete="name"></div><div class="field"><label for="b-co">Company</label><input id="b-co" name="company" required autocomplete="organization"></div></div>
        <div class="field"><label for="b-email">Work email</label><input id="b-email" name="email" type="email" required autocomplete="email"></div>
        <div class="row"><div class="field"><label for="b-phone">Phone / WhatsApp / WeChat</label><input id="b-phone" name="phone"></div><div class="field"><label for="b-web">Website</label><input id="b-web" name="website" type="url" placeholder="https://"></div></div>
        <div class="field"><label for="b-msg">Anything else?</label><textarea id="b-msg" name="message" style="min-height:80px"></textarea></div>
        <label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted about my request (see <a href="privacy.html">Privacy</a>).</label>
        <div class="row" style="margin-top:12px"><button type="button" class="btn btn-ghost" data-prev-step>← Back</button><button type="submit" class="btn btn-primary">Get my free plan</button></div>
      </div>
    </form>
  </div>
</div></section>
{ad()}
<section class="section-alt"><div class="container">
  <div class="section-head"><span class="eyebrow">Singles’ Day hub</span><h2>11.11 by the numbers</h2><div class="countdown" data-countdown="11-11" style="justify-content:center"></div></div>
  <div class="table-wrap"><table><thead><tr><th>Year</th><th>Figure</th><th>Source / note</th></tr></thead><tbody>
    <tr><td>2009</td><td>≈ US$10M</td><td>First Tmall Singles’ Day sale</td></tr>
    <tr><td>2021</td><td>¥540.3B (Alibaba) + ¥349.1B (JD)</td><td>Last year both companies disclosed GMV (CNBC)</td></tr>
    <tr><td>2024</td><td>¥1,441.8B</td><td>Industry-wide estimate, +26.6% (Syntun)</td></tr>
    <tr><td>2025</td><td>¥1,695B ≈ US$238B</td><td>Industry-wide estimate, 7 Oct–11 Nov, +14.2% (Syntun)</td></tr>
  </tbody></table></div>
  <p class="small muted" style="margin-top:10px">Company GMV hasn’t been disclosed since 2022. Third-party estimates use different methods and time windows. <a href="learn/singles-day-11-11.html">Full guide with sources →</a></p>
</div></section>
<section><div class="container">
  <div class="section-head"><h2>The China-numbers playbook</h2></div>
  <div class="grid g3">
    <div class="card"><h3>🏷️ Pricing</h3><p>Use endings of 8, 88, 168, 188 or 888. Never let 4 appear in a price, discount or bundle size. “Buy 2” and pairs work well because 好事成双 (“good things come in pairs”).</p></div>
    <div class="card"><h3>📅 Timing</h3><p>Plan around 520 (May 20), 618 (June 18), Qixi (lunar 7/7), 11.11 and 12.12. Avoid opening stores or launching in Ghost Month (lunar month 7).</p></div>
    <div class="card"><h3>☎️ Numbers you own</h3><p>Hotlines, WeChat IDs, unit numbers and plates are read aloud and remembered. Endings like 8888 or 6688 are status symbols; a 4 in them quietly costs trust.</p></div>
    <div class="card"><h3>🎁 Gifting</h3><p>Give red envelopes in even amounts, ideally with 8s (88, 168, 888). Avoid sets of 4. Don’t give clocks, because 送钟 sounds like attending a funeral.</p></div>
    <div class="card"><h3>🌐 Domains</h3><p>Numeric domains are easy to type on Chinese keyboards and cross the pinyin barrier. <a href="domains.html">See the numeric domain guide</a>.</p></div>
    <div class="card"><h3>📣 Copy</h3><p>Weave in number codes carefully: 520 for love campaigns, 666 for gaming and youth, 1314 for jewellery and weddings. Check every code against our <a href="meanings.html">dictionary</a> first.</p></div>
  </div>
</div></section>
<section class="section-alt"><div class="container" style="max-width:820px"><h2>FAQ</h2>{faq_html(bfaq)}<p style="margin-top:18px"><a class="btn btn-primary" href="#consult">Start my free plan</a> <a class="btn btn-ghost" href="{INQUIRY}" target="_blank" rel="noopener">Partnership inquiry</a></p></div></section>'''
    P.append(dict(path="business.html", title="China Market Numbers for Business — Pricing, Launch Dates & 11.11",
                  desc="Free China-numbers plan for brands: lucky price points, launch dates for 520, 618 and Singles' Day 11.11, hotline and domain audits. Reply within 24h.", body=body, schema=[faq_schema(bfaq)]))

    # ---------------- DOMAINS ----------------
    dfaq = [("What is a 6N domain?", "A domain made of six digits, such as 111176.com. All one million possible 6N .com domains were registered by November 2015, driven by Chinese demand."),
            ("What does “premium chip” mean?", "Chinese investors call numeric domains with no 0 and no 4 “chips” (筹码). 262,144 of the one million 6N .coms qualify."),
            ("Do you guarantee valuations?", "No. Our scorer grades patterns. For pricing, check recent comparable sales. Our human appraisal gives a range with the comparables it used.")]
    body = f'''
<section class="hero"><div class="container">
  {breadcrumb(r, [("domains.html", "Numeric Domains")])}
  <span class="eyebrow">Numeric domain intelligence</span>
  <h1>Numeric Domains for the Chinese Market</h1>
  <p class="lead">Why numbers beat words in China, how 4N/5N/6N domains are graded, and a free pattern scorer. Buy, sell, lease or get an appraisal.</p>
</div></section>
<section style="padding-top:0"><div class="container split" style="align-items:start">
  <div>
    <h2>Why Chinese buyers love numeric domains</h2>
    <p>Latin-letter brand names are hard to spell for many Chinese users, and pinyin spellings are ambiguous. Digits are universal, easy to type on any keyboard and carry homophone meanings. Some of China’s biggest sites are numeric: 163.com (NetEase), 360.cn, 58.com. Premium short numerics have sold for seven figures (11.com ≈ $2.3M in 2011; 114.com ≈ $2.1M in 2013, per Media Options).</p>
    <h3>How investors grade them</h3>
    <ul><li><strong>Length:</strong> 2N &gt; 3N &gt; 4N &gt; 5N &gt; 6N</li><li><strong>无4 / no 0:</strong> no 4 (and ideally no 0) — the “chip” standard</li><li><strong>Pattern:</strong> AAAA, AABB, ABAB, AAAABC, ascending runs</li><li><strong>Meaning:</strong> 168, 518, 520, 888 inside the number</li><li><strong>Extension:</strong> .com leads; .cn and .net follow</li></ul>
    <p><a href="learn/numeric-domains-china.html">Read the full guide →</a></p>
  </div>
  <div class="card"><h3>🌐 Score a numeric domain</h3><form id="dom-form"><div class="input-group"><label class="skip" for="dom-in">Domain</label><input id="dom-in" required placeholder="111176.com"><button class="btn btn-primary">Score</button></div></form><div id="dom-out" class="result"></div></div>
</div></section>
{ad()}
<section class="section-alt"><div class="container grid g2" style="align-items:start">
  <div class="card price-card featured"><span class="ribbon">Available</span><p class="eyebrow">This domain</p><h2 class="big-number" style="font-size:clamp(2rem,9vw,3rem);word-break:break-all">111176.com</h2><p>A 6N .com with a 1111 run (AAAABC pattern), no 4 and no 0, and a live content platform. Open to acquisition, joint venture, sponsorship or advertising partnerships.</p><a class="btn btn-gold" href="{INQUIRY}" target="_blank" rel="noopener">Make an offer / partner →</a></div>
  <div class="card" id="appraisal"><h3>Buy · Sell · Lease · Appraise</h3>
    <form class="js-form" id="domain-lead" data-subject="Domain lead (buy/sell/appraise)">{HP}
      <div class="field"><label for="dl-type">I want to…</label><select id="dl-type" name="request_type" required><option value="">Choose…</option><option>Get an appraisal</option><option>Sell a numeric domain</option><option>Buy a numeric domain</option><option>Lease-to-own</option><option>Acquire / partner on 111176.com</option></select></div>
      <div class="field"><label for="dl-dom">Domain(s)</label><textarea id="dl-dom" name="domains" required placeholder="One per line" style="min-height:70px"></textarea></div>
      <div class="row"><div class="field"><label for="dl-budget">Budget / asking price (USD)</label><input id="dl-budget" name="budget_or_price"></div><div class="field"><label for="dl-name">Name</label><input id="dl-name" name="name" required></div></div>
      <div class="field"><label for="dl-email">Email</label><input id="dl-email" name="email" type="email" required></div>
      <button class="btn btn-primary btn-block">Send request</button>
      <p class="form-note">We reply within 24h. We never share your domains or budget.</p>
    </form></div>
</div></section>
<section><div class="container" style="max-width:820px"><h2>FAQ</h2>{faq_html(dfaq)}</div></section>'''
    P.append(dict(path="domains.html", title="Numeric Domains in China — 6N Guide, Scorer & Appraisal",
                  desc="Why Chinese buyers value numeric domains, how 4N/5N/6N .com names are graded (无4, patterns), plus a free scorer and buy/sell/appraisal requests.", body=body, schema=[faq_schema(dfaq)]))

    # ---------------- CONTESTS ----------------
    body = f'''
<section class="hero"><div class="container split">
  <div>
    {breadcrumb(r, [("contests.html", "Contests & Prizes")])}
    <span class="eyebrow">Now open</span>
    <h1>🏆 “My Lucky Number Story” Contest</h1>
    <p class="lead">Tell us about a number that changed your luck: a phone number, a wedding date, a house number, a price that sold out. The best stories win prizes and get featured.</p>
    <div class="countdown" data-countdown="11-11"></div>
    <p class="small muted" style="margin-top:8px">Entries close on 11.11 (Singles’ Day) at 23:59 (UTC+8).</p>
  </div>
  <div class="grid g3" style="gap:10px">
    <div class="card center"><div style="font-size:2rem">🥇</div><b>$188</b><p class="small muted">+ featured story</p></div>
    <div class="card center"><div style="font-size:2rem">🥈</div><b>$88</b><p class="small muted">+ feature</p></div>
    <div class="card center"><div style="font-size:2rem">🥉</div><b>$28</b><p class="small muted">+ feature</p></div>
  </div>
</div></section>
<section style="padding-top:0"><div class="container split" style="align-items:start">
  <form class="card js-form" id="contest" data-subject="Contest entry — My Lucky Number Story">{HP}
    <h2 style="font-size:1.3rem">Enter now — it’s free</h2>
    <div class="row"><div class="field"><label for="ct-name">Name</label><input id="ct-name" name="name" required></div><div class="field"><label for="ct-email">Email</label><input id="ct-email" name="email" type="email" required></div></div>
    <div class="row"><div class="field"><label for="ct-num">Your number</label><input id="ct-num" name="lucky_number" required></div><div class="field"><label for="ct-country">Country</label><input id="ct-country" name="country" required></div></div>
    <div class="field"><label for="ct-story">Your story (50–500 words)</label><textarea id="ct-story" name="story" required minlength="200" maxlength="4000"></textarea></div>
    <div class="field"><label for="ct-link">Photo/video link (optional)</label><input id="ct-link" name="media_link" type="url" placeholder="https://"></div>
    <label class="check"><input type="checkbox" name="age_18" value="yes" required> I am 18 or older and accept the rules below.</label>
    <label class="check"><input type="checkbox" name="publish_ok" value="yes" required> I allow 111176.com to publish my story with my first name.</label>
    <button class="btn btn-primary btn-block" style="margin-top:12px">Submit my entry</button>
  </form>
  <div>
    <h2>Official rules (summary)</h2>
    <ol>
      <li>Free to enter; no purchase necessary. One entry per person per contest.</li>
      <li>Open to entrants aged 18+ where not prohibited by local law. Void where prohibited.</li>
      <li>Entries must be original and must not infringe anyone’s rights.</li>
      <li>Judging: originality (40%), storytelling (40%), usefulness to readers (20%), by the 111176 editorial panel.</li>
      <li>Prizes are paid in USD via PayPal or a gift card within 30 days of the winners being announced. Winners are responsible for any taxes.</li>
      <li>Winners are notified by email and must reply within 14 days, or an alternate winner is chosen.</li>
      <li>We may use entries (first name + story) on 111176.com and its social channels.</li>
      <li>Not sponsored, endorsed or administered by YouTube, Google, Alibaba, JD.com or any platform named on this site.</li>
    </ol>
    <div class="notice"><strong>Sponsor a prize:</strong> put your brand on the next contest. <a href="{INQUIRY}" target="_blank" rel="noopener">Contact us →</a></div>
    <h3 style="margin-top:20px">Coming next</h3>
    <ul><li>🧧 Lunar New Year “Lucky Red Envelope” photo contest</li><li>💘 520 Love Code story contest</li><li>🌐 Best numeric-domain pitch</li></ul>
    <h3>Past winners</h3><p class="muted">Our first contest is running now. Winners will be listed here.</p>
  </div>
</div></section>
{ad()}'''
    P.append(dict(path="contests.html", title="Contests & Prizes — My Lucky Number Story",
                  desc="Enter the free “My Lucky Number Story” contest at 111176.com. Win $188, $88 or $28 and get featured. Rules, prizes and entry form.", body=body))

    # ---------------- SUPPORT / DONATE / SPONSOR / ADVERTISE / CAREERS ----------------
    body = f'''
<section class="hero"><div class="container split">
  <div>
    {breadcrumb(r, [("support.html", "Support")])}
    <span class="eyebrow">Keep the tools free</span>
    <h1>🧧 Support 111176</h1>
    <p class="lead">Every tool on this site is free and ad-light. Your support pays for research, contest prizes, video production, translators and marketing, and keeps it independent.</p>
    <div class="grid g2" style="gap:10px"><div class="card"><b>40%</b> content &amp; research</div><div class="card"><b>20%</b> contest prizes</div><div class="card"><b>20%</b> hiring talent</div><div class="card"><b>20%</b> hosting &amp; marketing</div></div>
  </div>
  <div class="card">
    <h2 style="font-size:1.3rem">Give a lucky amount</h2>
    <div class="tiers" data-target="pl-amt"><button type="button" class="tier" data-amount="8" aria-pressed="false"><b>$8</b>发 prosper</button><button type="button" class="tier" data-amount="18" aria-pressed="true"><b>$18</b>要发 will prosper</button><button type="button" class="tier" data-amount="88" aria-pressed="false"><b>$88</b>double luck</button><button type="button" class="tier" data-amount="888" aria-pressed="false"><b>$888</b>patron</button></div>
    <div class="grid g2" style="margin-top:14px;gap:10px">
      <a class="btn btn-primary" href="#" data-donate="paypal">PayPal</a>
      <a class="btn btn-gold" href="#" data-donate="buymeacoffee">☕ Buy me a coffee</a>
      <a class="btn btn-ghost" href="#" data-donate="kofi">Ko-fi</a>
      <a class="btn btn-ghost" href="#" data-donate="github">GitHub Sponsors</a>
    </div>
    <p class="form-note">Prefer bank transfer, crypto or a custom amount? <a href="#" data-open="pledge-modal">Send a pledge</a> and we’ll email you a secure link. Donations are not tax-deductible.</p>
  </div>
</div></section>
<section id="sponsor"><div class="container">
  <div class="section-head"><span class="eyebrow">Sponsorship</span><h2>Sponsor a tool, a guide or a contest</h2><p class="lead">Put your brand in front of an audience of travellers, couples, sellers, marketers and investors who care about China.</p></div>
  <div class="grid g3">
    <div class="card price-card"><h3>Supporter</h3><div class="price">$88<small>/mo</small></div><ul><li>Logo on supporters wall</li><li>Newsletter thank-you</li><li>Dofollow link on About page</li></ul></div>
    <div class="card price-card featured"><span class="ribbon">Most popular</span><h3>Tool Sponsor</h3><div class="price">$888<small>/mo</small></div><ul><li>“Powered by” on one tool page</li><li>Banner below results</li><li>1 newsletter feature per month</li><li>Contest prize co-branding</li></ul></div>
    <div class="card price-card"><h3>Title Partner</h3><div class="price">Custom</div><ul><li>Sitewide presence</li><li>Co-branded 11.11 / 520 campaigns</li><li>Custom tools &amp; lead sharing</li><li>Domain partnership options</li></ul></div>
  </div>
  <p class="center" style="margin-top:18px"><a class="btn btn-primary" href="{INQUIRY}" target="_blank" rel="noopener">Discuss sponsorship</a></p>
</div></section>
<section id="advertise" class="section-alt"><div class="container split" style="align-items:start">
  <div><span class="eyebrow">Advertise</span><h2>Advertising options</h2>
    <div class="table-wrap"><table><thead><tr><th>Placement</th><th>Format</th><th>From</th></tr></thead><tbody>
      <tr><td>Homepage hero sponsor</td><td>Logo + link</td><td>$288/wk</td></tr>
      <tr><td>Decoder results banner</td><td>728×90 / responsive</td><td>$188/wk</td></tr>
      <tr><td>Guide sidebar</td><td>300×250</td><td>$88/wk</td></tr>
      <tr><td>Newsletter feature</td><td>Text + image</td><td>$128/send</td></tr>
      <tr><td>Sponsored guide</td><td>Labelled article</td><td>$588</td></tr>
    </tbody></table></div>
    <p class="small muted" style="margin-top:8px">All paid placements are clearly labelled. We reject ads for gambling, adult content, predatory lending and fake “fortune” scams.</p>
  </div>
  <form class="card js-form" id="advertise-form" data-subject="Advertising inquiry">{HP}
    <h3>Request the media kit</h3>
    <div class="row"><div class="field"><label for="ad-name">Name</label><input id="ad-name" name="name" required></div><div class="field"><label for="ad-co">Company</label><input id="ad-co" name="company" required></div></div>
    <div class="field"><label for="ad-email">Email</label><input id="ad-email" name="email" type="email" required></div>
    <div class="field"><label for="ad-type">Interested in</label><select id="ad-type" name="interest"><option>Display ads</option><option>Tool sponsorship</option><option>Newsletter</option><option>Sponsored guide</option><option>Contest prize</option><option>Title partnership</option></select></div>
    <div class="field"><label for="ad-bud">Budget</label><select id="ad-bud" name="budget"><option>Under $500</option><option>$500–$2,000</option><option>$2,000–$10,000</option><option>$10,000+</option></select></div>
    <button class="btn btn-primary btn-block">Send me the media kit</button>
  </form>
</div></section>
<section id="careers"><div class="container split" style="align-items:start">
  <div><span class="eyebrow">Careers &amp; talent</span><h2>Work with 111176</h2><p>We’re a remote-first team building the best number-culture resource online. Open roles (freelance / part-time):</p>
    <ul><li>✍️ <strong>Culture writers</strong> (English, Chinese or bilingual)</li><li>🌏 <strong>Translators</strong> — Simplified/Traditional Chinese, Spanish, Hindi, Vietnamese</li><li>🎬 <strong>Short-form video creators</strong> (YouTube Shorts, TikTok, Douyin)</li><li>💻 <strong>Front-end developers</strong> (vanilla JS, accessibility)</li><li>📈 <strong>Growth &amp; SEO marketers</strong></li><li>🤝 <strong>Partnership / ad sales</strong> (commission)</li></ul></div>
  <form class="card js-form" id="careers-form" data-subject="Talent application">{HP}
    <h3>Apply / join the talent pool</h3>
    <div class="row"><div class="field"><label for="cr-name">Name</label><input id="cr-name" name="name" required></div><div class="field"><label for="cr-email">Email</label><input id="cr-email" name="email" type="email" required></div></div>
    <div class="field"><label for="cr-role">Role</label><select id="cr-role" name="role" required><option value="">Choose…</option><option>Culture writer</option><option>Translator</option><option>Video creator</option><option>Front-end developer</option><option>Growth / SEO</option><option>Partnership / ad sales</option><option>Other</option></select></div>
    <div class="row"><div class="field"><label for="cr-port">Portfolio / LinkedIn</label><input id="cr-port" name="portfolio" type="url" placeholder="https://"></div><div class="field"><label for="cr-rate">Rate / availability</label><input id="cr-rate" name="rate"></div></div>
    <div class="field"><label for="cr-msg">Why you?</label><textarea id="cr-msg" name="message" required></textarea></div>
    <button class="btn btn-primary btn-block">Submit application</button>
  </form>
</div></section>
<section class="section-alt"><div class="container center"><h2>Supporters wall</h2><p class="muted">Be the first name here. <a href="#" data-open="pledge-modal">Become a supporter →</a></p></div></section>'''
    P.append(dict(path="support.html", title="Support, Sponsor, Advertise & Careers",
                  desc="Support 111176 with a lucky $8, $18 or $88 donation, sponsor a tool or contest, advertise, or join our team of writers, translators and creators.", body=body))

    # ---------------- ABOUT ----------------
    body = f'''
<section class="hero"><div class="container article">
  {breadcrumb(r, [("about.html", "About")])}
  <h1>About 111176</h1>
  <p class="lead">111176 is a free, independent resource that explains how numbers are read in Chinese culture and turns that knowledge into practical tools.</p>
  <h2>Why this site exists</h2>
  <p>Numbers carry meaning in Chinese: 8 means prosperity, 4 is avoided and 520 means “I love you”. People pay millions for lucky phone numbers and licence plates, and Singles’ Day (11.11) is the world’s largest shopping event. Yet most English explanations are scattered, shallow or written only to sell language lessons. We built one place that is free, fast and honest.</p>
  <h2>Our editorial standards</h2>
  <ul><li><strong>Sources on every guide.</strong> We cite news outlets, research firms and primary data.</li><li><strong>No invented “ancient meanings”.</strong> If a number has no established reading (like 111176 itself), we say so.</li><li><strong>Culture, not fortune-telling.</strong> Our scores describe how numbers sound and are perceived. They do not predict outcomes.</li><li><strong>Clearly labelled ads and sponsorships.</strong></li><li><strong>Updated regularly.</strong> Each guide shows its last-updated date.</li></ul>
  <h2>About the name</h2>
  <p>111176 is our domain name. We use it as a showcase: it opens with 1111 (Singles’ Day), has no 4 and ends on 6 (smooth flow). <a href="learn/meaning-of-111176.html">Read the full breakdown</a>.</p>
  <h2>Work with us</h2>
  <p>We welcome sponsors, advertisers, partners and contributors. <a href="support.html">Support options</a> · <a href="support.html#careers">Careers</a> · <a href="{INQUIRY}" target="_blank" rel="noopener">Domain / partnership inquiries</a> · <a href="contact.html">Contact</a></p>
</div></section>'''
    P.append(dict(path="about.html", title="About 111176 — Chinese Number Culture, Explained Honestly",
                  desc="111176 is a free, independent resource explaining Chinese number meanings with practical tools, sourced guides and clear editorial standards.", body=body))

    # ---------------- CONTACT ----------------
    body = f'''
<section class="hero"><div class="container split" style="align-items:start">
  <div>
    {breadcrumb(r, [("contact.html", "Contact")])}
    <h1>Contact us</h1>
    <p class="lead">Questions, corrections, partnerships or press — we reply within 1–2 business days.</p>
    <div class="grid" style="gap:12px">
      <a class="card" href="{INQUIRY}" target="_blank" rel="noopener"><h3>🌐 Domain / sponsorship / advertising / partnership</h3><p class="muted small">Interested in this website or domain name? Use our dedicated inquiry page.</p></a>
      <a class="card" href="business.html#consult"><h3>🏷️ Business consultation</h3><p class="muted small">Free China-numbers plan for your brand.</p></a>
      <a class="card" href="#" data-mail="Hello from 111176.com"><h3>✉️ Email us directly</h3><p class="muted small">Opens your email app. Our address stays private to limit spam.</p></a>
    </div>
  </div>
  <form class="card js-form" id="contact-form" data-subject="Contact form">{HP}
    <h2 style="font-size:1.3rem">Send a message</h2>
    <div class="row"><div class="field"><label for="c-name">Name</label><input id="c-name" name="name" required autocomplete="name"></div><div class="field"><label for="c-email">Email</label><input id="c-email" name="email" type="email" required autocomplete="email"></div></div>
    <div class="field"><label for="c-topic">Topic</label><select id="c-topic" name="topic" required><option value="">Choose…</option><option>General question</option><option>Correction / feedback</option><option>Website / domain purchase</option><option>Sponsorship</option><option>Advertising</option><option>Partnership</option><option>Press / media</option><option>Contest</option><option>Donation</option><option>Careers</option></select></div>
    <div class="field"><label for="c-msg">Message</label><textarea id="c-msg" name="message" required></textarea></div>
    <label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to the <a href="privacy.html">Privacy Policy</a>.</label>
    <button class="btn btn-primary btn-block" style="margin-top:12px">Send message</button>
  </form>
</div></section>'''
    P.append(dict(path="contact.html", title="Contact 111176", desc="Contact 111176 for questions, corrections, partnerships, sponsorship, advertising or domain inquiries.", body=body))

    # ---------------- LEGAL ----------------
    legal_wrap = lambda title, crumb, path, inner: f'<section><div class="container article">{breadcrumb(r, [(path, crumb)])}<h1>{title}</h1><p class="meta">Last updated: {UPDATED}</p>{inner}</div></section>'
    privacy = '''
<p>This policy explains what 111176.com (“we”, “us”) collects and why.</p>
<h2>1. Information you give us</h2><p>When you submit a form (report request, newsletter, contact, business, contest, careers, pledge), we receive the fields you fill in. Submissions are delivered to our inbox through FormSubmit (formsubmit.co), a third-party form-forwarding service. We use this information only to answer your request and, if you opt in, to send our newsletter. We do not sell personal data.</p>
<h2>2. Tools</h2><p>Numbers, dates and names you type into our tools are processed <strong>in your browser</strong>. They are not sent to us unless you submit a form.</p>
<h2>3. Cookies &amp; local storage</h2><p>We store small preferences (theme, cookie choice, popup timing) in your browser’s local storage. If enabled, Google Analytics sets cookies to measure traffic.</p>
<h2>4. Advertising (Google AdSense)</h2><p>Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this and other websites. Google’s advertising cookies enable it and its partners to serve ads based on your visits to our site and/or other sites on the Internet. You may opt out of personalised advertising at <a href="https://www.google.com/settings/ads" rel="noopener" target="_blank">Google Ads Settings</a> or <a href="https://www.aboutads.info/choices/" rel="noopener" target="_blank">aboutads.info</a>. See <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener">how Google uses data from partner sites</a>.</p>
<h2>5. Embedded content</h2><p>Videos are embedded from YouTube in privacy-enhanced mode (youtube-nocookie.com) and load only when you press play. YouTube’s own policies then apply.</p>
<h2>6. Hosting</h2><p>The site is hosted on GitHub Pages, which may log IP addresses for security and operations.</p>
<h2>7. Your rights</h2><p>You may request access to, correction of or deletion of your data, or unsubscribe at any time, via our <a href="contact.html">contact page</a>. Residents of the EU/UK (GDPR), California (CCPA/CPRA), Canada (PIPEDA/Law 25) and other jurisdictions have the rights their laws provide.</p>
<h2>8. Children</h2><p>This site is not directed to children under 13, and contests are open to adults (18+) only.</p>
<h2>9. Changes</h2><p>We will post updates on this page with a new date.</p>'''
    P.append(dict(path="privacy.html", title="Privacy Policy", desc="Privacy policy for 111176.com: forms, cookies, Google AdSense, analytics and your rights.", body=legal_wrap("Privacy Policy", "Privacy", "privacy.html", privacy)))
    terms = '''
<h2>1. Acceptance</h2><p>By using 111176.com you agree to these terms.</p>
<h2>2. Nature of content</h2><p>All content and tool outputs are provided for <strong>cultural education and entertainment</strong>. They are not financial, investment, legal, medical, religious or professional advice. Luck scores are editorial interpretations of how numbers sound in Chinese and do not predict outcomes.</p>
<h2>3. Domain information</h2><p>Domain pattern grades are not appraisals or offers. Always do your own due diligence, including trademark checks, before buying or selling any domain.</p>
<h2>4. User submissions</h2><p>By submitting content (stories, suggestions, videos) you confirm you have the right to do so, and you grant us a non-exclusive, worldwide, royalty-free licence to publish it with attribution.</p>
<h2>5. Contests</h2><p>Each contest is governed by its posted rules. Void where prohibited.</p>
<h2>6. Donations</h2><p>Donations are voluntary, non-refundable and not tax-deductible unless stated otherwise.</p>
<h2>7. Intellectual property</h2><p>See our <a href="disclaimer.html">Disclaimer &amp; Trademark/Copyright Notice</a>.</p>
<h2>8. Limitation of liability</h2><p>The site is provided “as is”. To the fullest extent permitted by law, we are not liable for any loss arising from its use.</p>
<h2>9. Links</h2><p>We are not responsible for third-party websites we link to.</p>
<h2>10. Changes</h2><p>We may update these terms at any time by posting a new version here.</p>'''
    P.append(dict(path="terms.html", title="Terms of Use", desc="Terms of use for 111176.com.", body=legal_wrap("Terms of Use", "Terms", "terms.html", terms)))
    disc = f'''
<div class="quick"><strong>In short:</strong> 111176.com claims no trademark in the number “111176”. Our content and code are original and copyrighted. Third-party names belong to their owners and are used only for identification and commentary.</div>
<h2>1. Trademark disclosure</h2>
<ul>
<li>“111176” is used on this website as a <strong>domain name and a descriptive number</strong>. We do <strong>not</strong> claim exclusive trademark rights in the numeral string 111176, and nothing on this site should be read as such a claim.</li>
<li>Numbers, number sequences and their cultural meanings (e.g. 8, 520, 1314, 11.11) are part of the public domain of language and culture. We describe them; we do not own them.</li>
<li>Any similarity between “111176” and any product code, part number, catalogue number, postal code or registered mark is coincidental. No affiliation is implied.</li>
<li>Third-party names such as Alibaba, Tmall, JD.com, Google, AdSense, YouTube, GitHub, PayPal, Ko-fi, Buy Me a Coffee, NetEase, Sedo and Afternic are trademarks of their respective owners. They are mentioned for identification, news reporting and commentary only (nominative fair use). No endorsement or sponsorship by them is implied.</li>
<li>“Singles’ Day”, “Double 11” and “11.11” are used descriptively to refer to the shopping festival. Where any party holds rights in a related mark in a given jurisdiction, those rights are acknowledged.</li>
</ul>
<h2>2. Copyright notice</h2>
<ul>
<li>© 2026 111176.com. All original text, tool logic, design, graphics and code on this site are protected by copyright. You may quote short excerpts with a link back. Republishing entire pages requires permission.</li>
<li>Embedded videos remain the property of their creators and are shown via YouTube’s official embed player under YouTube’s Terms of Service.</li>
<li>Data points (e.g. sales figures) are facts cited from the named sources and remain attributable to those sources.</li>
<li>Chinese characters, pinyin and traditional associations described here are cultural heritage. Our explanations of them are original writing.</li>
</ul>
<h2>3. Copyright / takedown requests</h2>
<p>If you believe content on this site infringes your rights, <a href="contact.html">contact us</a> with the URL, a description of the work and your contact details. We respond promptly and remove infringing material.</p>
<h2>4. Advice disclaimer</h2>
<p>All content is for cultural education and entertainment only. It is not financial, investment, legal, medical, religious or other professional advice. Luck scores do not predict outcomes.</p>
<h2>5. Advertising &amp; affiliate disclosure</h2>
<p>This site may display Google AdSense ads, sponsored placements and affiliate links. Paid placements are labelled. We may earn a commission when you buy through some links, at no extra cost to you. It never changes our editorial ratings.</p>
<h2>6. Domain / partnership inquiries</h2>
<p>Interested in this website, domain name, sponsorship, advertising or a partnership? <a href="{INQUIRY}" target="_blank" rel="noopener">Contact us here</a>.</p>'''
    P.append(dict(path="disclaimer.html", title="Disclaimer & Trademark / Copyright Notice", desc="Trademark and copyright disclosure, advice disclaimer and advertising disclosure for 111176.com.", body=legal_wrap("Disclaimer &amp; Trademark / Copyright Notice", "Disclaimer", "disclaimer.html", disc)))

    # ---------------- 404 & THANK YOU ----------------
    P.append(dict(path="404.html", title="Page not found", desc="Page not found.", noindex=True, body='''
<section class="hero"><div class="container center"><div class="big-number">404</div><h1>This page went missing</h1><p class="lead">In Chinese, 4 sounds like “death”, so maybe this page just avoided bad luck. Try these instead:</p>
<p><a class="btn btn-primary" href="index.html">Home</a> <a class="btn btn-ghost" href="decoder.html">Number Decoder</a> <a class="btn btn-ghost" href="meanings.html">Number Meanings</a></p></div></section>'''))
    P.append(dict(path="thank-you.html", title="Thank you", desc="Thank you for contacting 111176.", noindex=True, body=f'''
<section class="hero"><div class="container center" style="max-width:720px"><div style="font-size:4rem">🧧</div><h1>Thank you — we got it!</h1><p class="lead">We reply within 24 hours on business days. Check your inbox (and spam folder) for our reply.</p>
<div class="grid g3" style="margin-top:24px"><a class="card" href="decoder.html">🔢 Decode another number</a><a class="card" href="meanings.html">📖 Browse number meanings</a><a class="card" href="support.html">❤️ Support the site</a></div>
<div class="card" style="margin-top:24px"><p><strong>Share 111176 with a friend</strong></p><button class="btn btn-ghost btn-sm" data-share="x" data-share-text="Free Chinese number decoder — check what your number means">X</button> <button class="btn btn-ghost btn-sm" data-share="facebook">Facebook</button> <button class="btn btn-ghost btn-sm" data-share="whatsapp" data-share-text="Check what your number means in Chinese:">WhatsApp</button> <button class="btn btn-ghost btn-sm" data-share="copy">Copy link</button></div>
</div></section>'''))
    return P
