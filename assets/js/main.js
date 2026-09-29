/* 111176.com — core site script (vanilla JS, no dependencies) */
(function () {
  "use strict";
  var C = window.SITE_CONFIG || {};
  var ROOT = document.body.getAttribute("data-root") || "";
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  };

  /* ---------- shared overlays (newsletter, pledge, cookie, back-to-top) ---------- */
  var HP = '<input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">';
  var nl = function (id) { return '<form class="js-form" id="' + id + '" data-subject="Newsletter signup" data-next="stay">' + HP + '<input type="hidden" name="form" value="Newsletter"><div class="input-group"><label class="skip" for="' + id + '-e">Email</label><input id="' + id + '-e" type="email" name="email" required placeholder="Your email for the weekly lucky number"><button class="btn btn-gold" type="submit">Subscribe</button></div></form>'; };
  var shell = document.createElement("div");
  shell.innerHTML =
    '<div class="modal" id="newsletter-modal" role="dialog" aria-modal="true" aria-labelledby="nl-title"><div class="modal-box"><button class="icon-btn modal-close" type="button" aria-label="Close">✕</button><p class="eyebrow">Free weekly email</p><h3 id="nl-title">Get a lucky number every week 🧧</h3><p class="muted">Your weekly number, the best upcoming dates and one number-slang lesson. 30 seconds a week.</p>' + nl("newsletter-pop") + '</div></div>' +
    '<div class="modal" id="pledge-modal" role="dialog" aria-modal="true" aria-labelledby="pl-title"><div class="modal-box"><button class="icon-btn modal-close" type="button" aria-label="Close">✕</button><p class="eyebrow">Support 111176</p><h3 id="pl-title">Pledge your support</h3><p class="muted small">Leave your details and we’ll email you a secure payment link (PayPal, card or bank transfer) within 24 hours.</p>' +
    '<form class="js-form" id="pledge" data-subject="Donation pledge">' + HP +
    '<div class="field"><label for="pl-amt">Amount (USD)</label><input id="pl-amt" name="amount" type="number" min="1" value="18" required></div>' +
    '<div class="field"><label for="pl-name">Name</label><input id="pl-name" name="name" required></div>' +
    '<div class="field"><label for="pl-email">Email</label><input id="pl-email" name="email" type="email" required></div>' +
    '<div class="field"><label for="pl-note">Purpose (optional)</label><select id="pl-note" name="purpose"><option>General operations</option><option>Contest prizes</option><option>Content &amp; video production</option><option>Hiring writers / translators</option><option>Marketing &amp; promotion</option></select></div>' +
    '<label class="check"><input type="checkbox" name="public_thanks" value="yes"> List my name on the supporters wall</label>' +
    '<button class="btn btn-gold btn-block" type="submit" style="margin-top:10px">Send pledge</button></form></div></div>' +
    '<div class="cookie" role="dialog" aria-label="Cookie notice"><strong>Cookies &amp; ads.</strong> We use cookies for preferences, analytics and (with Google AdSense) personalised ads. See our <a href="' + ROOT + 'privacy.html">Privacy Policy</a>.<div class="btns"><button class="btn btn-primary btn-sm" data-cookie="1">Accept</button><button class="btn btn-ghost btn-sm" data-cookie="0">Essential only</button></div></div>' +
    '<button class="icon-btn to-top" type="button" aria-label="Back to top">↑</button>';
  while (shell.firstChild) document.body.appendChild(shell.firstChild);

  /* ---------- hidden owner inbox ---------- */
  function inbox() {
    var m = C._m || [], k = C._k || 0, s = "";
    for (var i = m.length - 1; i >= 0; i--) s += String.fromCharCode(m[i] ^ k);
    return s;
  }
  function endpoint() {
    return "https://formsubmit.co/ajax/" + (C.FORM_ALIAS || inbox());
  }
  $$("[data-mail]").forEach(function (a) {
    a.setAttribute("href", "#");
    a.setAttribute("rel", "nofollow");
    a.addEventListener("click", function (e) {
      e.preventDefault();
      var subj = a.getAttribute("data-mail") || "Inquiry from 111176.com";
      window.location.href = "mailto:" + inbox() + "?subject=" + encodeURIComponent(subj);
    });
  });
  window.__site = { endpoint: endpoint, toast: toast, openModal: openModal };

  /* ---------- theme ---------- */
  var saved = store.get("theme");
  if (saved) document.documentElement.setAttribute("data-theme", saved);
  $$(".theme-toggle").forEach(function (b) {
    b.addEventListener("click", function () {
      var cur = document.documentElement.getAttribute("data-theme");
      if (!cur) cur = matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
      var next = cur === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", next);
      store.set("theme", next);
    });
  });

  /* ---------- nav ---------- */
  var burger = $(".burger"), menu = $(".menu");
  if (burger && menu) burger.addEventListener("click", function () {
    var o = menu.classList.toggle("open");
    burger.setAttribute("aria-expanded", o ? "true" : "false");
    document.body.style.overflow = o ? "hidden" : "";
  });
  var here = location.pathname.split("/").pop() || "index.html";
  $$(".menu a").forEach(function (a) {
    if ((a.getAttribute("href") || "").split("/").pop() === here) a.setAttribute("aria-current", "page");
  });

  /* ---------- toast ---------- */
  var toastEl;
  function toast(msg) {
    if (!toastEl) { toastEl = document.createElement("div"); toastEl.className = "toast"; toastEl.setAttribute("role", "status"); document.body.appendChild(toastEl); }
    toastEl.textContent = msg; toastEl.classList.add("show");
    clearTimeout(toastEl._t); toastEl._t = setTimeout(function () { toastEl.classList.remove("show"); }, 3800);
  }

  /* ---------- modal ---------- */
  function openModal(id) { var m = document.getElementById(id); if (m) { m.classList.add("open"); var f = m.querySelector("input,button"); if (f) f.focus(); } }
  $$("[data-open]").forEach(function (b) { b.addEventListener("click", function (e) { e.preventDefault(); openModal(b.getAttribute("data-open")); }); });
  $$(".modal").forEach(function (m) {
    m.addEventListener("click", function (e) { if (e.target === m || e.target.closest(".modal-close")) m.classList.remove("open"); });
  });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") $$(".modal.open").forEach(function (m) { m.classList.remove("open"); }); });

  /* ---------- forms (FormSubmit AJAX) ---------- */
  $$("form.js-form").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var hp = form.querySelector("[name=_honey]");
      if (hp && hp.value) return;
      var data = {};
      new FormData(form).forEach(function (v, k) {
        if (k === "_honey") return;
        data[k] = data[k] ? data[k] + ", " + v : v;
      });
      data._subject = "[111176.com] " + (form.getAttribute("data-subject") || "Website form");
      data._template = "table";
      data._captcha = "false";
      data.page = location.href;
      data.submitted_at = new Date().toISOString();
      var btn = form.querySelector("[type=submit]");
      var label = btn ? btn.innerHTML : "";
      if (btn) { btn.disabled = true; btn.textContent = "Sending…"; }
      fetch(endpoint(), {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify(data)
      }).then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (res) {
          if (res.ok && String(res.j.success) !== "false") {
            store.set("lead_" + (form.id || "form"), "1");
            form.reset();
            var next = form.getAttribute("data-next");
            if (next === "stay") { toast("Thank you! We received your submission."); }
            else { location.href = ROOT + "thank-you.html?f=" + encodeURIComponent(form.getAttribute("data-subject") || ""); }
          } else { throw new Error("send failed"); }
        })
        .catch(function () {
          toast("Network issue — opening your email app instead.");
          var body = Object.keys(data).map(function (k) { return k + ": " + data[k]; }).join("\n");
          location.href = "mailto:" + inbox() + "?subject=" + encodeURIComponent(data._subject) + "&body=" + encodeURIComponent(body);
        })
        .then(function () { if (btn) { btn.disabled = false; btn.innerHTML = label; } });
    });
  });

  /* ---------- multi-step forms ---------- */
  $$("[data-steps]").forEach(function (wrap) {
    var steps = $$(".step", wrap), bars = $$(".steps span", wrap), i = 0;
    function show(n) {
      steps.forEach(function (s, k) { s.classList.toggle("active", k === n); });
      bars.forEach(function (b, k) { b.classList.toggle("on", k <= n); });
      i = n;
    }
    $$("[data-next-step]", wrap).forEach(function (b) {
      b.addEventListener("click", function () {
        var fields = $$("input,select,textarea", steps[i]);
        for (var k = 0; k < fields.length; k++) { if (!fields[k].checkValidity()) { fields[k].reportValidity(); return; } }
        show(Math.min(i + 1, steps.length - 1));
      });
    });
    $$("[data-prev-step]", wrap).forEach(function (b) { b.addEventListener("click", function () { show(Math.max(i - 1, 0)); }); });
    show(0);
  });

  /* ---------- ads ---------- */
  var slots = $$(".ad-slot");
  if (C.ADSENSE_CLIENT) {
    var s = document.createElement("script");
    s.async = true; s.crossOrigin = "anonymous";
    s.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + C.ADSENSE_CLIENT;
    document.head.appendChild(s);
    slots.forEach(function (el) {
      el.innerHTML = "";
      var ins = document.createElement("ins");
      ins.className = "adsbygoogle"; ins.style.display = "block"; ins.style.width = "100%";
      ins.setAttribute("data-ad-client", C.ADSENSE_CLIENT);
      var slot = el.getAttribute("data-slot") || (C.ADSENSE_SLOTS && C.ADSENSE_SLOTS["default"]);
      if (slot) ins.setAttribute("data-ad-slot", slot);
      ins.setAttribute("data-ad-format", "auto");
      ins.setAttribute("data-full-width-responsive", "true");
      el.appendChild(ins);
      try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
    });
  } else {
    slots.forEach(function (el) {
      el.innerHTML = '<div class="house-ad"><strong>Your brand here.</strong> Reach readers who care about numbers, luck &amp; China commerce. <a href="' + (C.INQUIRY_URL || "#") + '" target="_blank" rel="noopener">Advertise / Sponsor →</a></div>';
    });
  }

  /* ---------- analytics (optional) ---------- */
  if (C.GA_ID && store.get("cookie_ok") === "1") {
    var g = document.createElement("script"); g.async = true; g.src = "https://www.googletagmanager.com/gtag/js?id=" + C.GA_ID; document.head.appendChild(g);
    window.dataLayer = window.dataLayer || []; window.gtag = function () { dataLayer.push(arguments); }; gtag("js", new Date()); gtag("config", C.GA_ID);
  }

  /* ---------- lazy YouTube ---------- */
  $$(".video[data-id]").forEach(function (v) {
    var id = v.getAttribute("data-id");
    v.innerHTML = '<img loading="lazy" alt="' + (v.getAttribute("data-title") || "Video") + '" src="https://i.ytimg.com/vi/' + id + '/hqdefault.jpg"><div class="play"><span aria-hidden="true">▶</span></div>';
    v.setAttribute("role", "button"); v.setAttribute("tabindex", "0");
    v.setAttribute("aria-label", "Play video: " + (v.getAttribute("data-title") || ""));
    function play() { v.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0" title="' + (v.getAttribute("data-title") || "YouTube video") + '" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'; }
    v.addEventListener("click", play, { once: true });
    v.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); play(); } });
  });

  /* ---------- countdowns ---------- */
  function nextDate(md) { // "11-11"
    var p = md.split("-"), now = new Date(), y = now.getFullYear();
    var d = new Date(y, +p[0] - 1, +p[1]);
    if (d - now < -86400000) d = new Date(y + 1, +p[0] - 1, +p[1]);
    return d;
  }
  $$("[data-countdown]").forEach(function (el) {
    var v = el.getAttribute("data-countdown");
    var target = /^\d{2}-\d{2}$/.test(v) ? nextDate(v) : new Date(v);
    function tick() {
      var ms = Math.max(0, target - new Date());
      var d = Math.floor(ms / 864e5), h = Math.floor(ms / 36e5) % 24, m = Math.floor(ms / 6e4) % 60, s = Math.floor(ms / 1e3) % 60;
      el.innerHTML = "<div><b>" + d + "</b><span>days</span></div><div><b>" + h + "</b><span>hours</span></div><div><b>" + m + "</b><span>min</span></div><div><b>" + s + "</b><span>sec</span></div>";
    }
    tick(); setInterval(tick, 1000);
  });

  /* ---------- share ---------- */
  $$("[data-share]").forEach(function (b) {
    b.addEventListener("click", function () {
      var text = b.getAttribute("data-share-text") || document.title;
      var url = location.href;
      var net = b.getAttribute("data-share");
      if (net === "native" && navigator.share) { navigator.share({ title: document.title, text: text, url: url }).catch(function () {}); return; }
      var map = {
        x: "https://twitter.com/intent/tweet?text=" + encodeURIComponent(text) + "&url=" + encodeURIComponent(url),
        facebook: "https://www.facebook.com/sharer/sharer.php?u=" + encodeURIComponent(url),
        whatsapp: "https://wa.me/?text=" + encodeURIComponent(text + " " + url),
        linkedin: "https://www.linkedin.com/sharing/share-offsite/?url=" + encodeURIComponent(url),
        pinterest: "https://pinterest.com/pin/create/button/?url=" + encodeURIComponent(url) + "&description=" + encodeURIComponent(text)
      };
      if (map[net]) window.open(map[net], "_blank", "noopener,width=640,height=560");
      else if (navigator.clipboard) navigator.clipboard.writeText(text + " " + url).then(function () { toast("Copied to clipboard"); });
    });
  });

  /* ---------- donation tiers ---------- */
  $$(".tiers").forEach(function (group) {
    var target = document.getElementById(group.getAttribute("data-target"));
    $$(".tier", group).forEach(function (t) {
      t.addEventListener("click", function () {
        $$(".tier", group).forEach(function (x) { x.setAttribute("aria-pressed", "false"); });
        t.setAttribute("aria-pressed", "true");
        if (target) target.value = t.getAttribute("data-amount");
      });
    });
  });
  $$("[data-donate]").forEach(function (b) {
    var key = b.getAttribute("data-donate"), url = C.DONATE && C.DONATE[key];
    b.addEventListener("click", function (e) {
      if (url) { b.setAttribute("href", url); b.setAttribute("target", "_blank"); b.setAttribute("rel", "noopener"); }
      else { e.preventDefault(); openModal("pledge-modal"); }
    });
  });

  /* ---------- cookie consent ---------- */
  var ck = $(".cookie");
  if (ck && !store.get("cookie_ok")) {
    ck.classList.add("show");
    $$("[data-cookie]", ck).forEach(function (b) {
      b.addEventListener("click", function () { store.set("cookie_ok", b.getAttribute("data-cookie")); ck.classList.remove("show"); });
    });
  }

  /* ---------- newsletter popup (max once / 7 days, never after signup) ---------- */
  var nm = document.getElementById("newsletter-modal");
  if (nm && !store.get("lead_newsletter-pop") && !store.get("lead_newsletter") && !store.get("lead_newsletter-foot")) {
    var last = +store.get("nl_seen") || 0;
    if (Date.now() - last > 7 * 864e5) {
      var fired = false;
      var fire = function () { if (fired) return; fired = true; store.set("nl_seen", String(Date.now())); nm.classList.add("open"); };
      setTimeout(fire, 45000);
      document.addEventListener("mouseout", function (e) { if (!e.relatedTarget && e.clientY < 5) fire(); });
    }
  }

  /* ---------- back to top ---------- */
  var tt = $(".to-top");
  if (tt) {
    addEventListener("scroll", function () { tt.classList.toggle("show", scrollY > 700); }, { passive: true });
    tt.addEventListener("click", function () { scrollTo({ top: 0, behavior: "smooth" }); });
  }

  /* ---------- year ---------- */
  $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
