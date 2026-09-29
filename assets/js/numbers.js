/* 111176.com — number engine: data, decoder, tools. Original work. */
(function () {
  "use strict";
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }

  /* ---------------- DATA ---------------- */
  var DIGITS = {
    "0": { zh: "零", py: "líng", w: 0, tone: "mid", sound: "灵 líng — spirit, cleverness", meaning: "Wholeness, a clean start, the infinite. Neutral on its own; amplifies neighbours." },
    "1": { zh: "一 / 幺", py: "yī / yāo", w: 1, tone: "good", sound: "幺 yāo ≈ 要 yào — “want / will”", meaning: "Unity, first place, leadership, independence. In phone and room numbers it is read “yāo”." },
    "2": { zh: "二", py: "èr", w: 2, tone: "good", sound: "好事成双 — good things come in pairs", meaning: "Harmony, partnership, balance. Doubling a lucky digit strengthens it." },
    "3": { zh: "三", py: "sān", w: 1, tone: "mid", sound: "生 shēng (Cantonese) — life; 散 sàn — scatter", meaning: "Growth and life (southern China); some Mandarin speakers hear “scatter”. Mostly positive." },
    "4": { zh: "四", py: "sì", w: -6, tone: "bad", sound: "死 sǐ — death", meaning: "The most avoided digit. Many buildings skip the 4th, 14th and 24th floors (tetraphobia)." },
    "5": { zh: "五", py: "wǔ", w: 0, tone: "mid", sound: "我 wǒ — “me”; 无 wú — “without”", meaning: "The Five Elements (五行) and balance. Neutral; meaning depends on neighbours (5-2-0 = I love you)." },
    "6": { zh: "六", py: "liù", w: 4, tone: "good", sound: "溜 / 流 liū — smooth, flowing", meaning: "Smooth progress: 六六大顺 “everything goes smoothly”. Online, 666 = “awesome”." },
    "7": { zh: "七", py: "qī", w: -1, tone: "mid", sound: "起 qǐ — rise; 气 qì — energy / anger; 欺 qī — cheat", meaning: "Mixed. Linked to togetherness and Qixi (Chinese Valentine’s Day), but lunar month 7 is Ghost Month." },
    "8": { zh: "八", py: "bā", w: 6, tone: "good", sound: "发 fā — prosper, get rich", meaning: "The luckiest number. The Beijing Olympics opened 08/08/08 at 8:08:08 pm." },
    "9": { zh: "九", py: "jiǔ", w: 4, tone: "good", sound: "久 jiǔ — long-lasting", meaning: "Longevity and eternity; historically associated with the emperor. Popular for weddings." }
  };
  var COMBOS = [
    ["5201314", "我爱你一生一世", "I love you for a lifetime", "love", 8],
    ["1314", "一生一世", "Forever / one life, one world", "love", 6],
    ["520", "我爱你", "I love you (May 20 is “Internet Valentine’s Day”)", "love", 6],
    ["521", "我愿意 / 我爱你", "I’m willing / I love you", "love", 5],
    ["530", "我想你", "I miss you", "love", 3],
    ["360", "想念你", "Missing you", "love", 2],
    ["770", "亲亲你", "Kiss you", "love", 2],
    ["7758", "亲亲我吧", "Kiss me", "love", 2],
    ["880", "抱抱你", "Hug you", "love", 2],
    ["9420", "就是爱你", "It’s you I love", "love", 4],
    ["8013", "伴你一生", "By your side for life", "love", 4],
    ["3344", "生生世世", "Life after life, forever", "love", 3],
    ["1573", "一往情深", "Deeply in love", "love", 3],
    ["25", "爱我", "Love me", "love", 2],
    ["57", "我妻", "My wife", "love", 2],
    ["04551", "你是我唯一", "You are my one and only", "love", 3],
    ["564335", "无聊时想想我", "Think of me when you’re bored", "love", 2],
    ["168", "一路发", "Prosperity all the way", "prosperity", 8],
    ["1688", "一路发发", "Prosperity all the way, doubled", "prosperity", 8],
    ["518", "我要发", "I will prosper", "prosperity", 7],
    ["5188", "我要发发", "I will prosper greatly", "prosperity", 7],
    ["888", "发发发", "Triple prosperity", "prosperity", 9],
    ["88", "发发 / 拜拜", "Double prosperity; online also “bye-bye”", "prosperity", 6],
    ["28", "易发 (Cantonese)", "Easy prosperity — a record HK$18.1M plate", "prosperity", 5],
    ["68", "路发", "Prosper along the way", "prosperity", 4],
    ["98", "久发", "Lasting wealth", "prosperity", 4],
    ["666", "溜溜溜", "Awesome, well played (internet slang)", "internet", 6],
    ["66", "顺顺", "Smooth, smooth — everything goes well", "prosperity", 4],
    ["99", "久久", "Forever and ever", "love", 5],
    ["999", "久久久", "Eternal", "love", 5],
    ["886", "拜拜了", "Bye then (chat sign-off)", "internet", 0],
    ["233", "(laughing)", "LOL — from a Mop.com laughing emoticon code", "internet", 0],
    ["555", "呜呜呜", "Crying sound, boo-hoo", "internet", -1],
    ["9494", "就是就是", "Exactly, exactly!", "internet", 0],
    ["4242", "是啊是啊", "Yes, yes", "internet", 0],
    ["456", "是我啦", "It’s me!", "internet", 0],
    ["918", "加油吧", "Go for it! You can do it", "internet", 2],
    ["995", "救救我", "Save me / help", "internet", -1],
    ["526", "我饿了", "I’m hungry", "internet", 0],
    ["246", "饿死了", "Starving", "internet", -1],
    ["584", "我发誓", "I swear", "internet", 0],
    ["587", "我抱歉", "I’m sorry", "internet", 0],
    ["596", "我走了", "I’m leaving", "internet", 0],
    ["847", "别生气", "Don’t be angry", "internet", 0],
    ["8006", "不理你了", "Not talking to you any more", "internet", -1],
    ["7086", "七零八落", "In a total mess", "internet", -1],
    ["7456", "气死我了", "I’m furious", "warning", -3],
    ["740", "气死你", "Make you furious", "warning", -3],
    ["748", "去死吧", "Go die (rude)", "warning", -6],
    ["0748", "你去死吧", "You go die (very rude)", "warning", -6],
    ["514", "我要死", "I’m going to die (dramatic)", "warning", -5],
    ["14", "要死 / 一死", "“Want death” — avoided on floors and plates", "warning", -5],
    ["44", "死死", "Double death", "warning", -7],
    ["54", "我死 / 无事", "“I die” — avoided", "warning", -4],
    ["74", "气死", "Angry to death", "warning", -4],
    ["250", "二百五", "Idiot, fool (insult)", "warning", -5],
    ["38", "三八", "Busybody, gossip (insult)", "warning", -3],
    ["0487", "你是白痴", "You’re an idiot", "warning", -4],
    ["1111", "光棍节", "Singles’ Day / Double 11 — the world’s largest shopping festival", "festival", 3],
    ["618", "六一八", "JD.com’s mid-year shopping festival (June 18)", "festival", 3],
    ["214", "情人节", "Valentine’s Day (Feb 14)", "festival", 1],
    ["77", "七夕", "Qixi — Chinese Valentine’s Day (7th day, 7th lunar month)", "festival", 2],
    ["11", "光棍", "“Bare sticks” — single people", "festival", 0],
    ["2468", "双双对对", "Even ascending pairs — harmony (numerology)", "prosperity", 3],
    ["6688", "顺顺发发", "Smooth and prosperous", "prosperity", 8],
    ["8888", "发发发发", "Ultimate prosperity — record-priced phone numbers", "prosperity", 10]
  ];
  var ANIMALS = [
    { k: "rat", zh: "鼠", e: "🐀", lucky: [2, 3], unlucky: [5, 9], trait: "Quick-witted, resourceful, versatile" },
    { k: "ox", zh: "牛", e: "🐂", lucky: [1, 4], unlucky: [5, 6], trait: "Diligent, dependable, strong" },
    { k: "tiger", zh: "虎", e: "🐅", lucky: [1, 3, 4], unlucky: [6, 7, 8], trait: "Brave, confident, competitive" },
    { k: "rabbit", zh: "兔", e: "🐇", lucky: [3, 4, 6], unlucky: [1, 7, 8], trait: "Gentle, elegant, responsible" },
    { k: "dragon", zh: "龙", e: "🐉", lucky: [1, 6, 7], unlucky: [3, 8], trait: "Confident, ambitious, charismatic" },
    { k: "snake", zh: "蛇", e: "🐍", lucky: [2, 8, 9], unlucky: [1, 6, 7], trait: "Wise, enigmatic, intuitive" },
    { k: "horse", zh: "马", e: "🐎", lucky: [2, 3, 7], unlucky: [1, 5, 6], trait: "Energetic, independent, warm" },
    { k: "goat", zh: "羊", e: "🐐", lucky: [2, 7], unlucky: [4, 9], trait: "Calm, creative, kind" },
    { k: "monkey", zh: "猴", e: "🐒", lucky: [4, 9], unlucky: [2, 7], trait: "Clever, curious, playful" },
    { k: "rooster", zh: "鸡", e: "🐓", lucky: [5, 7, 8], unlucky: [1, 3, 9], trait: "Observant, hardworking, courageous" },
    { k: "dog", zh: "狗", e: "🐕", lucky: [3, 4, 9], unlucky: [1, 6, 7], trait: "Loyal, honest, prudent" },
    { k: "pig", zh: "猪", e: "🐖", lucky: [2, 5, 8], unlucky: [1, 7], trait: "Generous, compassionate, diligent" }
  ];
  var BRANCH = "子丑寅卯辰巳午未申酉戌亥", STEM = "甲乙丙丁戊己庚辛壬癸";
  var ELEMENT = ["Wood", "Wood", "Fire", "Fire", "Earth", "Earth", "Metal", "Metal", "Water", "Water"];
  window.NUM_DATA = { DIGITS: DIGITS, COMBOS: COMBOS, ANIMALS: ANIMALS };

  /* ---------------- ENGINE ---------------- */
  function onlyDigits(s) { return String(s || "").replace(/\D/g, ""); }
  function findCombos(d) {
    var hits = [], used = {};
    COMBOS.slice().sort(function (a, b) { return b[0].length - a[0].length; }).forEach(function (c) {
      if (c[0].length < 2) return;
      var i = d.indexOf(c[0]);
      if (i > -1 && !used[c[0]]) {
        // skip if fully covered by a longer hit already
        var covered = hits.some(function (h) { return h.idx <= i && h.idx + h.code.length >= i + c[0].length; });
        if (!covered) { hits.push({ code: c[0], zh: c[1], en: c[2], cat: c[3], w: c[4], idx: i }); used[c[0]] = 1; }
      }
    });
    return hits.sort(function (a, b) { return a.idx - b.idx; });
  }
  function patternInfo(d) {
    var out = [], n = d.length;
    if (!n) return out;
    var counts = {}; for (var i = 0; i < n; i++) counts[d[i]] = (counts[d[i]] || 0) + 1;
    var maxRun = 1, run = 1;
    for (i = 1; i < n; i++) { run = d[i] === d[i - 1] ? run + 1 : 1; if (run > maxRun) maxRun = run; }
    if (Object.keys(counts).length === 1) out.push("All-same digits (" + d[0] + "×" + n + ") — top-tier pattern");
    else if (maxRun >= 3) out.push("Repeating run of " + maxRun + " identical digits — strong, memorable pattern");
    if (n > 2 && d === d.split("").reverse().join("")) out.push("Palindrome — reads the same both ways");
    var asc = true, dsc = true;
    for (i = 1; i < n; i++) { if (+d[i] !== +d[i - 1] + 1) asc = false; if (+d[i] !== +d[i - 1] - 1) dsc = false; }
    if (n > 2 && asc) out.push("Ascending sequence — symbolises rising fortune (步步高)");
    if (n > 2 && dsc) out.push("Descending sequence");
    if (n >= 4 && n % 2 === 0 && /^(\d\d)\1+$/.test(d)) out.push("ABAB repeating pairs");
    if (n >= 4 && /^(\d)\1(\d)\2/.test(d) && d[0] !== d[2]) out.push("AABB pairs — very popular in China");
    if (d.indexOf("4") === -1) out.push("No 4 (无4) — preferred by Chinese buyers");
    else out.push("Contains 4 (" + counts["4"] + "×) — reduces appeal in Chinese markets");
    if (d.indexOf("0") === -1 && d.indexOf("4") === -1) out.push("No 0 and no 4 — qualifies as a “premium chip” (筹码) in numeric-domain trading");
    if (d.indexOf("8") > -1) out.push("Contains 8 (发) — prosperity signal");
    return out;
  }
  function patternCode(d) {
    var map = {}, next = 65, s = "";
    for (var i = 0; i < d.length; i++) { if (!(d[i] in map)) map[d[i]] = String.fromCharCode(next++); s += map[d[i]]; }
    return s;
  }
  function score(d) {
    if (!d) return 0;
    var n = d.length, sum = 0;
    for (var i = 0; i < n; i++) sum += DIGITS[d[i]].w;
    var avg = sum / n;                 // -6..6
    var base = 50 + avg * 6;           // ~14..86
    findCombos(d).forEach(function (c) { base += c.w * 2.2; });
    if (d[n - 1] === "8" || d[n - 1] === "6" || d[n - 1] === "9") base += 5;
    if (d[n - 1] === "4") base -= 8;
    var runs = d.match(/(\d)\1+/g) || [];
    runs.forEach(function (r) { base += DIGITS[r[0]].w >= 0 ? r.length * 1.5 : -r.length * 2; });
    return Math.max(1, Math.min(99, Math.round(base)));
  }
  function verdict(s) {
    if (s >= 80) return { t: "Very auspicious", c: "good" };
    if (s >= 62) return { t: "Auspicious", c: "good" };
    if (s >= 45) return { t: "Neutral / balanced", c: "mid" };
    if (s >= 30) return { t: "Mixed — some caution", c: "mid" };
    return { t: "Inauspicious", c: "bad" };
  }
  function improve(d) {
    if (d.indexOf("4") === -1) return null;
    var alt = d.replace(/4/g, "8");
    return { alt: alt, s: score(alt) };
  }
  function lunarInfo(date) {
    try {
      var en = new Intl.DateTimeFormat("en-u-ca-chinese", { year: "numeric", month: "numeric", day: "numeric" }).formatToParts(date);
      var zh = new Intl.DateTimeFormat("zh-CN-u-ca-chinese", { year: "numeric", month: "long", day: "numeric" }).formatToParts(date);
      var get = function (p, t) { var x = p.filter(function (q) { return q.type === t; })[0]; return x ? x.value : ""; };
      var m = get(en, "month"), yn = get(zh, "yearName");
      var leap = /bis/.test(m);
      var month = parseInt(m, 10), day = parseInt(get(en, "day"), 10);
      var b = BRANCH.indexOf(yn.charAt(1)), st = STEM.indexOf(yn.charAt(0));
      return { month: month, day: day, leap: leap, yearName: yn, animal: b > -1 ? ANIMALS[b] : null, element: st > -1 ? ELEMENT[st] : "", zhMonth: get(zh, "month"), ok: true };
    } catch (e) { return { ok: false }; }
  }
  function animalByYear(y) { return ANIMALS[((y - 4) % 12 + 12) % 12]; }
  window.NUM = { onlyDigits: onlyDigits, score: score, verdict: verdict, findCombos: findCombos, patternInfo: patternInfo, patternCode: patternCode, lunarInfo: lunarInfo, animalByYear: animalByYear };

  /* ---------------- RENDER: DECODER ---------------- */
  function renderDecode(raw, mode, box) {
    var d = onlyDigits(raw), extra = "";
    if (mode === "date" && raw) {
      var dt = new Date(raw + "T12:00:00");
      if (!isNaN(dt)) {
        d = raw.replace(/\D/g, "");
        var L = lunarInfo(dt);
        if (L.ok) {
          extra += '<p><strong>Lunar date:</strong> ' + esc(L.yearName) + ' year (' + (L.animal ? L.animal.e + " " + L.animal.k : "") + '), ' + esc(L.zhMonth) + ' day ' + L.day + '.</p>';
          if (L.month === 7 && !L.leap) extra += '<p class="notice"><strong>Ghost Month:</strong> this date falls in the 7th lunar month. Traditionally avoided for weddings, moving and openings.</p>';
          if (L.month === 7 && L.day === 7) extra += '<p class="notice">This is <strong>Qixi (七夕)</strong> — Chinese Valentine’s Day.</p>';
        }
      }
    }
    if (!d) { box.innerHTML = '<p class="muted">Enter at least one digit.</p>'; box.classList.add("show"); return; }
    if (d.length > 40) d = d.slice(0, 40);
    var s = score(d), v = verdict(s), combos = findCombos(d), pats = patternInfo(d), imp = improve(d);
    var color = v.c === "good" ? "var(--good)" : v.c === "bad" ? "var(--bad)" : "var(--mid)";
    var html = '<div class="grid g2" style="align-items:center">';
    html += '<div class="center"><div class="gauge" style="--v:' + s + ';--c:' + color + '"><b>' + s + '</b></div><p style="margin-top:10px"><span class="badge ' + v.c + '">' + v.t + '</span></p><p class="small muted">Luck score out of 100</p></div>';
    html += '<div><h3 style="margin-bottom:4px">' + esc(d) + '</h3><p class="small muted">Pattern ' + patternCode(d) + ' · ' + d.length + ' digits · read aloud: ' + d.split("").map(function (x) { return x === "1" ? "yāo" : DIGITS[x].py; }).join(" ") + '</p>' + extra + '</div></div>';
    html += '<div class="digits">' + d.split("").map(function (x) { var D = DIGITS[x]; return '<div class="digit ' + D.tone + '" title="' + esc(D.sound) + '"><b>' + x + '</b><small class="zh">' + D.zh.split(" ")[0] + '</small><small>' + D.py.split(" ")[0] + '</small></div>'; }).join("") + '</div>';
    if (combos.length) {
      html += '<h4>Hidden phrases found</h4><ul class="pairs">' + combos.map(function (c) {
        var t = c.w > 1 ? "good" : c.w < 0 ? "bad" : "mid";
        return '<li><span class="badge ' + t + '">' + c.code + '</span> <span class="zh">' + esc(c.zh) + '</span> — ' + esc(c.en) + '</li>';
      }).join("") + '</ul>';
    }
    var uniq = d.split("").filter(function (x, i, a) { return a.indexOf(x) === i; });
    html += '<h4 style="margin-top:14px">Digit meanings</h4><ul class="pairs">' + uniq.map(function (x) { return '<li><strong>' + x + ' <span class="zh">' + DIGITS[x].zh + '</span></strong> — ' + esc(DIGITS[x].sound) + '. ' + esc(DIGITS[x].meaning) + '</li>'; }).join("") + '</ul>';
    if (pats.length) html += '<h4 style="margin-top:14px">Pattern notes</h4><ul class="pairs">' + pats.map(function (p) { return "<li>" + esc(p) + "</li>"; }).join("") + "</ul>";
    if (mode === "price") {
      var p = parseFloat(String(raw).replace(/[^\d.]/g, ""));
      if (!isNaN(p)) {
        var cands = [Math.floor(p) + 0.88, Math.floor(p) + 0.68, Math.floor(p / 10) * 10 + 8, Math.floor(p / 100) * 100 + 88, Math.floor(p / 1000) * 1000 + 888, Math.floor(p) + 0.99, Math.floor(p / 10) * 10 + 6]
          .filter(function (x) { return x > 0 && Math.abs(x - p) / p < 0.2; })
          .map(function (x) { return +x.toFixed(2); })
          .filter(function (x, i, a) { return a.indexOf(x) === i && String(x).indexOf("4") === -1; });
        if (cands.length) html += '<h4 style="margin-top:14px">Luckier price points near ' + esc(p) + '</h4><p>' + cands.map(function (x) { return '<span class="badge good" style="margin:2px">' + x + '</span>'; }).join(" ") + '</p>';
      }
    }
    if (imp) html += '<p class="notice" style="margin-top:14px">Swap every 4 for an 8 → <strong>' + imp.alt + '</strong> scores <strong>' + imp.s + '</strong>/100.</p>';
    html += '<div class="grid g2" style="margin-top:18px"><div><button class="btn btn-ghost btn-sm" data-copy>Copy result</button> <button class="btn btn-ghost btn-sm" data-sharethis>Share</button></div><div style="text-align:right"><a class="btn btn-primary btn-sm" href="#full-report">Get my full report →</a></div></div>';
    html += '<p class="form-note">For culture &amp; entertainment. Not financial, legal or religious advice.</p>';
    box.innerHTML = html;
    box.classList.add("show");
    var txt = "My number " + d + " scored " + s + "/100 (" + v.t + ") on 111176.com";
    var cp = box.querySelector("[data-copy]"); if (cp) cp.addEventListener("click", function () { if (navigator.clipboard) navigator.clipboard.writeText(txt + " " + location.href).then(function () { window.__site && __site.toast("Result copied"); }); });
    var sh = box.querySelector("[data-sharethis]"); if (sh) sh.addEventListener("click", function () { if (navigator.share) navigator.share({ title: "My lucky number", text: txt, url: location.href }).catch(function () {}); else window.open("https://twitter.com/intent/tweet?text=" + encodeURIComponent(txt) + "&url=" + encodeURIComponent(location.href), "_blank", "noopener"); });
    var hidden = document.getElementById("report-number"); if (hidden) hidden.value = d + " (score " + s + ")";
    try { var u = new URL(location.href); u.searchParams.set("n", d); history.replaceState(null, "", u); } catch (e) {}
  }
  $$("[data-decoder]").forEach(function (wrap) {
    var input = $("input", wrap), box = $(".result", wrap), mode = "any";
    var modes = $$(".seg button", wrap);
    var ph = { any: "e.g. 111176, 5201314", phone: "e.g. +86 138 8888 1688", plate: "e.g. 粤B 88A66 / ABC 1234", address: "e.g. Unit 1608, 88 King St", price: "e.g. 99.95", date: "", domain: "e.g. 111176.com" };
    modes.forEach(function (b) {
      b.addEventListener("click", function () {
        modes.forEach(function (x) { x.setAttribute("aria-pressed", "false"); });
        b.setAttribute("aria-pressed", "true"); mode = b.getAttribute("data-mode");
        input.type = mode === "date" ? "date" : "text"; input.placeholder = ph[mode] || ""; input.value = ""; input.focus();
      });
    });
    $("form", wrap).addEventListener("submit", function (e) { e.preventDefault(); renderDecode(input.value, mode, box); });
    var q = new URLSearchParams(location.search).get("n");
    if (q && wrap.hasAttribute("data-autoload")) { input.value = q; renderDecode(q, "any", box); }
    else if (wrap.hasAttribute("data-demo")) { input.value = wrap.getAttribute("data-demo"); renderDecode(input.value, "any", box); }
  });

  /* ---------------- DICTIONARY ---------------- */
  var dict = document.getElementById("dict");
  if (dict) {
    var list = $("#dict-list"), q = $("#dict-q"), cats = $$("[data-cat]");
    var cat = "all";
    var all = Object.keys(DIGITS).map(function (k) { var D = DIGITS[k]; return { code: k, zh: D.zh, en: D.sound + ". " + D.meaning, cat: "digit", w: D.w }; })
      .concat(COMBOS.map(function (c) { return { code: c[0], zh: c[1], en: c[2], cat: c[3], w: c[4] }; }));
    function draw() {
      var term = (q.value || "").toLowerCase().trim();
      var rows = all.filter(function (r) { return (cat === "all" || r.cat === cat) && (!term || (r.code + " " + r.zh + " " + r.en + " " + r.cat).toLowerCase().indexOf(term) > -1); });
      list.innerHTML = rows.map(function (r) {
        var t = r.w > 1 ? "good" : r.w < 0 ? "bad" : "mid";
        return '<div class="card dict-item" id="n-' + r.code + '"><div class="dict-num">' + r.code + '</div><div><p style="margin:0 0 4px"><span class="zh" style="font-size:1.1rem">' + esc(r.zh) + '</span> <span class="badge ' + t + '">' + (t === "good" ? "lucky" : t === "bad" ? "avoid" : "neutral") + '</span> <span class="badge gold">' + r.cat + '</span></p><p style="margin:0">' + esc(r.en) + '</p><p style="margin:6px 0 0" class="small"><a href="decoder.html?n=' + r.code + '">Decode ' + r.code + ' →</a></p></div></div>';
      }).join("") || '<p class="muted">No match. Try the <a href="decoder.html">Number Decoder</a>.</p>';
      $("#dict-count").textContent = rows.length + " entries";
    }
    q.addEventListener("input", draw);
    cats.forEach(function (b) { b.addEventListener("click", function () { cats.forEach(function (x) { x.setAttribute("aria-pressed", "false"); }); b.setAttribute("aria-pressed", "true"); cat = b.getAttribute("data-cat"); draw(); }); });
    draw();
  }

  /* ---------------- ZODIAC ---------------- */
  var zg = document.getElementById("zodiac-grid");
  if (zg) {
    var zout = document.getElementById("zodiac-out");
    function showAnimal(a, extra) {
      $$("button", zg).forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-k") === a.k ? "true" : "false"); });
      var years = []; var y0 = new Date().getFullYear() - 96; for (var y = y0; y <= y0 + 108; y++) if (animalByYear(y) === a) years.push(y);
      zout.innerHTML = '<div class="card"><div class="split" style="gap:20px"><div><p class="eyebrow">Your sign</p><h2 style="text-transform:capitalize">' + a.e + ' ' + a.k + ' <span class="zh">' + a.zh + '</span></h2>' + (extra || "") + '<p>' + a.trait + '.</p><p><strong>Lucky numbers:</strong> ' + a.lucky.map(function (n) { return '<span class="badge good">' + n + '</span>'; }).join(" ") + '</p><p><strong>Unlucky numbers:</strong> ' + a.unlucky.map(function (n) { return '<span class="badge bad">' + n + '</span>'; }).join(" ") + '</p><p class="small muted">Years (approx. — the sign changes at Lunar New Year, not Jan 1): ' + years.join(", ") + '</p></div><div class="center"><div class="big-number">' + a.lucky.join("") + a.lucky[0] + '</div><p class="muted small">A personal lucky combo built from your sign’s lucky digits</p><a class="btn btn-primary" href="decoder.html?n=' + a.lucky.join("") + a.lucky[0] + '">Decode it</a></div></div></div>';
    }
    zg.innerHTML = ANIMALS.map(function (a) { return '<button type="button" data-k="' + a.k + '" aria-pressed="false"><b>' + a.e + '</b><span style="text-transform:capitalize">' + a.k + '</span> <span class="zh">' + a.zh + '</span></button>'; }).join("");
    $$("button", zg).forEach(function (b) { b.addEventListener("click", function () { showAnimal(ANIMALS.filter(function (a) { return a.k === b.getAttribute("data-k"); })[0]); }); });
    var zf = document.getElementById("zodiac-form");
    if (zf) zf.addEventListener("submit", function (e) {
      e.preventDefault();
      var v = $("input", zf).value; if (!v) return;
      var dt = new Date(v + "T12:00:00"), L = lunarInfo(dt), a, extra = "";
      if (L.ok && L.animal) { a = L.animal; extra = '<p><span class="badge red">' + L.element + " " + a.k + '</span> <span class="zh">' + L.yearName + '年</span> · lunar ' + L.zhMonth + ' day ' + L.day + '</p>'; }
      else { a = animalByYear(dt.getFullYear()); extra = '<p class="small muted">Approximation (your browser lacks the Chinese calendar).</p>'; }
      showAnimal(a, extra);
    });
    var cur = lunarInfo(new Date());
    if (cur.ok && cur.animal) showAnimal(cur.animal, '<p><span class="badge red">Current year: ' + cur.element + ' ' + cur.animal.k + '</span> <span class="zh">' + cur.yearName + '年</span></p>');
    $$("[data-zodiac-table]").forEach(function (t) {
      t.innerHTML = '<table><thead><tr><th>Sign</th><th>Lucky numbers</th><th>Unlucky numbers</th><th>Traits</th></tr></thead><tbody>' + ANIMALS.map(function (a) { return '<tr><td style="text-transform:capitalize">' + a.e + ' ' + a.k + ' <span class="zh">' + a.zh + '</span></td><td>' + a.lucky.join(", ") + '</td><td>' + a.unlucky.join(", ") + '</td><td>' + a.trait + '</td></tr>'; }).join("") + '</tbody></table>';
    });
  }

  /* ---------------- LUCKY DATES CALENDAR ---------------- */
  var cal = document.getElementById("cal");
  if (cal) {
    var mi = document.getElementById("cal-month"), purpose = document.getElementById("cal-purpose");
    var FEST = { "1-1": "New Year", "2-14": "Valentine’s", "5-20": "520 Love Day", "5-21": "521", "6-18": "618 Sale", "8-8": "8.8 Double Eight", "9-9": "Double Nine", "11-11": "Singles’ Day", "12-12": "Double 12" };
    var now = new Date(); mi.value = now.getFullYear() + "-" + String(now.getMonth() + 1).padStart(2, "0");
    function drawCal() {
      var p = mi.value.split("-"), y = +p[0], m = +p[1] - 1; if (!y) return;
      var first = new Date(y, m, 1), days = new Date(y, m + 1, 0).getDate(), html = "";
      ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"].forEach(function (d) { html += '<div class="dow">' + d + "</div>"; });
      for (var i = 0; i < first.getDay(); i++) html += "<div></div>";
      var best = [];
      for (var d = 1; d <= days; d++) {
        var dt = new Date(y, m, d, 12), L = lunarInfo(dt);
        var code = String(m + 1) + String(d), s = score(String(y) + code), dd = String(d);
        var sDay = score(code);
        var val = Math.round(s * 0.4 + sDay * 0.6);
        var fest = FEST[(m + 1) + "-" + d] || "";
        if (L.ok) {
          if (L.month === 7 && !L.leap) { val -= 25; if (L.day === 15) fest = "Ghost Festival"; }
          if (L.month === 1 && L.day === 1) fest = "Lunar New Year";
          if (L.month === 1 && L.day === 15) fest = "Lantern Festival";
          if (L.month === 5 && L.day === 5) fest = "Dragon Boat";
          if (L.month === 7 && L.day === 7 && !L.leap) { fest = "Qixi 七夕"; if (purpose.value === "wedding") val += 30; }
          if (L.month === 8 && L.day === 15) fest = "Mid-Autumn";
          if (L.month === 4 && L.day === 5) fest = fest || "";
        }
        if (/4/.test(dd)) val -= 12;
        if (/8/.test(dd)) val += 8;
        if (purpose.value === "business" && /8|6/.test(dd)) val += 6;
        if (purpose.value === "wedding" && /9|2/.test(dd)) val += 6;
        if (purpose.value === "move" && /6/.test(dd)) val += 6;
        var cls = val >= 64 ? "good" : val < 38 ? "bad" : "mid";
        if (cls === "good") best.push(d);
        html += '<div class="day ' + cls + '" title="Score ' + val + '"><b>' + d + '</b>' + (L.ok ? '<span class="lunar">' + (L.leap ? "leap " : "") + "L" + L.month + "/" + L.day + "</span>" : "") + (fest ? '<span class="fest">' + fest + "</span>" : "") + "</div>";
      }
      cal.innerHTML = html;
      var bl = document.getElementById("cal-best");
      if (bl) bl.innerHTML = best.length ? "<strong>Top picks this month:</strong> " + best.slice(0, 10).map(function (d) { return '<span class="badge good">' + d + "</span>"; }).join(" ") : "No strongly auspicious dates this month — consider the next month.";
    }
    mi.addEventListener("change", drawCal); purpose.addEventListener("change", drawCal); drawCal();
  }

  /* ---------------- TOOLS ---------------- */
  // lucky number generator
  var gen = document.getElementById("gen-form");
  if (gen) gen.addEventListener("submit", function (e) {
    e.preventDefault();
    var name = $("#gen-name").value.trim(), dob = $("#gen-dob").value, len = +$("#gen-len").value || 6;
    var seed = 2166136261; (name + dob).split("").forEach(function (c) { seed ^= c.charCodeAt(0); seed = Math.imul(seed, 16777619) >>> 0; });
    function rnd() { seed ^= seed << 13; seed >>>= 0; seed ^= seed >>> 17; seed ^= seed << 5; seed >>>= 0; return seed / 4294967296; }
    var a = dob ? (lunarInfo(new Date(dob + "T12:00:00")).animal || animalByYear(+dob.slice(0, 4))) : null;
    var pool = [8, 8, 6, 9, 2, 1].concat(a ? a.lucky : []).filter(function (n) { return n !== 4 && (!a || a.unlucky.indexOf(n) === -1); });
    var sets = [];
    for (var k = 0; k < 3; k++) { var s = ""; for (var i = 0; i < len; i++) s += pool[Math.floor(rnd() * pool.length)]; sets.push(s); }
    sets.sort(function (x, y) { return score(y) - score(x); });
    $("#gen-out").innerHTML = (a ? '<p>Zodiac: <strong style="text-transform:capitalize">' + a.e + " " + a.k + "</strong> — lucky " + a.lucky.join(", ") + "</p>" : "") + sets.map(function (s) { return '<div class="card" style="margin-bottom:10px;display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap"><span class="dict-num">' + s + '</span><span class="badge good">' + score(s) + '/100</span><a class="btn btn-ghost btn-sm" href="decoder.html?n=' + s + '">Decode</a></div>'; }).join("");
    $("#gen-out").classList.add("show");
  });
  // compatibility
  var comp = document.getElementById("comp-form");
  if (comp) comp.addEventListener("submit", function (e) {
    e.preventDefault();
    var a = onlyDigits($("#comp-a").value), b = onlyDigits($("#comp-b").value); if (!a || !b) return;
    var sa = score(a), sb = score(b), shared = a.split("").filter(function (x, i, arr) { return arr.indexOf(x) === i && b.indexOf(x) > -1; });
    var sumA = a.split("").reduce(function (t, x) { return t + +x; }, 0) % 9 || 9, sumB = b.split("").reduce(function (t, x) { return t + +x; }, 0) % 9 || 9;
    var harmony = Math.round((sa + sb) / 2 * 0.6 + shared.length * 6 + (sumA === sumB ? 12 : Math.abs(sumA - sumB) <= 2 ? 6 : 0) + 8);
    harmony = Math.max(1, Math.min(99, harmony)); var v = verdict(harmony);
    $("#comp-out").innerHTML = '<div class="grid g3"><div class="card center"><p class="muted small">Number A</p><b class="dict-num">' + sa + '</b></div><div class="card center"><p class="muted small">Harmony</p><div class="gauge" style="--v:' + harmony + ';width:110px"><b>' + harmony + '</b></div><span class="badge ' + v.c + '">' + v.t + '</span></div><div class="card center"><p class="muted small">Number B</p><b class="dict-num">' + sb + '</b></div></div><p style="margin-top:12px">Shared digits: ' + (shared.join(", ") || "none") + ' · Root numbers: ' + sumA + ' &amp; ' + sumB + '</p>';
    $("#comp-out").classList.add("show");
  });
  // numeral converter
  function toChinese(n, fin) {
    var D = fin ? "零壹贰叁肆伍陆柒捌玖" : "零一二三四五六七八九", U = fin ? ["", "拾", "佰", "仟"] : ["", "十", "百", "千"], B = ["", "万", "亿", "万亿"];
    if (n === 0) return D[0];
    function sec(x) { var s = "", z = false; for (var i = 3; i >= 0; i--) { var d = Math.floor(x / Math.pow(10, i)) % 10; if (d === 0) { if (s) z = true; } else { if (z) { s += D[0]; z = false; } s += D[d] + U[i]; } } return s; }
    var secs = []; while (n > 0) { secs.push(n % 10000); n = Math.floor(n / 10000); }
    var res = "", pend = false;
    for (var i = secs.length - 1; i >= 0; i--) {
      var s = secs[i];
      if (s === 0) { if (res) pend = true; continue; }
      if (res && (s < 1000 || pend)) res += D[0];
      res += sec(s) + B[i]; pend = false;
    }
    if (!fin && res.indexOf("一十") === 0) res = res.slice(1);
    return res;
  }
  var PY = { "零": "líng", "一": "yī", "二": "èr", "三": "sān", "四": "sì", "五": "wǔ", "六": "liù", "七": "qī", "八": "bā", "九": "jiǔ", "十": "shí", "百": "bǎi", "千": "qiān", "万": "wàn", "亿": "yì", "点": "diǎn" };
  window.NUM.toChinese = toChinese;
  var conv = document.getElementById("conv-form");
  if (conv) conv.addEventListener("submit", function (e) {
    e.preventDefault();
    var raw = $("#conv-in").value.replace(/[, ]/g, ""); if (!/^\d+(\.\d+)?$/.test(raw)) { $("#conv-out").innerHTML = '<p class="muted">Enter a number like 111176 or 8888.88</p>'; $("#conv-out").classList.add("show"); return; }
    var parts = raw.split("."), int = parseInt(parts[0], 10);
    if (int > 9999999999999) { $("#conv-out").innerHTML = '<p class="muted">Max 13 digits.</p>'; $("#conv-out").classList.add("show"); return; }
    var dec = parts[1] || "";
    var norm = toChinese(int, false) + (dec ? "点" + dec.split("").map(function (x) { return "零一二三四五六七八九"[x]; }).join("") : "");
    var finS = toChinese(int, true) + (dec ? "点" + dec.split("").map(function (x) { return "零壹贰叁肆伍陆柒捌玖"[x]; }).join("") : "");
    var money = toChinese(int, true) + "元" + (dec ? (dec[0] && dec[0] !== "0" ? "零壹贰叁肆伍陆柒捌玖"[dec[0]] + "角" : "") + (dec[1] && dec[1] !== "0" ? "零壹贰叁肆伍陆柒捌玖"[dec[1]] + "分" : "") : "整");
    var py = norm.split("").map(function (c) { return PY[c] || c; }).join(" ");
    var spoken = parts[0].split("").map(function (x) { return x === "1" ? "yāo" : DIGITS[x].py; }).join(" ");
    $("#conv-out").innerHTML = '<div class="table-wrap"><table><tbody><tr><th>Standard Chinese</th><td class="zh" style="font-size:1.3rem">' + norm + '</td></tr><tr><th>Pinyin</th><td>' + py + '</td></tr><tr><th>Financial (大写)</th><td class="zh" style="font-size:1.3rem">' + finS + '</td></tr><tr><th>Cheque / invoice (RMB)</th><td class="zh">' + money + '</td></tr><tr><th>Digit-by-digit (phone style)</th><td>' + spoken + '</td></tr></tbody></table></div>';
    $("#conv-out").classList.add("show");
  });
  // domain scorer
  var dom = document.getElementById("dom-form");
  if (dom) dom.addEventListener("submit", function (e) {
    e.preventDefault();
    var raw = $("#dom-in").value.trim().toLowerCase(), label = raw.replace(/^https?:\/\//, "").split("/")[0], name = label.split(".")[0], tld = label.split(".").slice(1).join(".") || "com";
    var d = onlyDigits(name); if (!d || d !== name) { $("#dom-out").innerHTML = '<p class="muted">Enter an all-numeric domain like 111176.com</p>'; $("#dom-out").classList.add("show"); return; }
    var s = score(d), pats = patternInfo(d), n = d.length;
    var tier = n <= 3 ? "Ultra-premium (1–3N) — elite, typically brokered privately" : n === 4 ? "Premium 4N — strong liquidity in Chinese markets" : n === 5 ? "5N — solid, pattern-driven value" : n === 6 ? "6N — liquid category; premium if it has no 0 and no 4 and a strong pattern" : "7N+ — low liquidity unless it spells a date or phrase";
    var points = 0; if (d.indexOf("4") === -1) points += 2; if (d.indexOf("0") === -1) points += 1; if (/(\d)\1\1/.test(d)) points += 2; if (/8/.test(d)) points += 1; if (tld === "com") points += 2; if (findCombos(d).length) points += 1;
    var grade = points >= 7 ? "A" : points >= 5 ? "B" : points >= 3 ? "C" : "D";
    $("#dom-out").innerHTML = '<div class="grid g3"><div class="card center"><p class="muted small">Pattern</p><b class="dict-num">' + patternCode(d) + '</b></div><div class="card center"><p class="muted small">Culture score</p><b class="dict-num">' + s + '</b></div><div class="card center"><p class="muted small">Grade</p><b class="dict-num">' + grade + '</b></div></div><p style="margin-top:12px"><strong>' + esc(label) + '</strong> · ' + tier + (tld !== "com" ? " · Non-.com extensions usually trade far below .com." : "") + '</p><ul class="pairs">' + pats.map(function (p) { return "<li>" + esc(p) + "</li>"; }).join("") + '</ul><p class="form-note">Pattern grade only — not a price appraisal. Check recent comparable sales before buying or selling. <a href="domains.html#appraisal">Request a human appraisal →</a></p>';
    $("#dom-out").classList.add("show");
  });
})();
