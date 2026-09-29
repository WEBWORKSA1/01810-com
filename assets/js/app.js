/* 01810.com — core site script (no dependencies) */
(function () {
  "use strict";
  var C = window.SITE_CONFIG || {};
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var store = {
    get: function (k, d) { try { var v = localStorage.getItem(k); return v === null ? d : JSON.parse(v); } catch (e) { return d; } },
    set: function (k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  };
  window.Site = { $: $, $$: $$, store: store };

  /* ---------- inbox (assembled at runtime, never in markup) ---------- */
  function inbox() {
    return (C._m || []).slice().reverse().map(function (n) { return String.fromCharCode(n ^ C._k); }).join("");
  }
  Site.inbox = inbox;

  /* ---------- toast ---------- */
  function toast(msg) {
    var t = $("#toast"); if (!t) return;
    t.textContent = msg; t.classList.add("show");
    clearTimeout(t._h); t._h = setTimeout(function () { t.classList.remove("show"); }, 2600);
  }
  Site.toast = toast;

  /* ---------- theme ---------- */
  var root = document.documentElement;
  var saved = store.get("theme", null);
  if (saved) root.setAttribute("data-theme", saved);
  function isDark() {
    var a = root.getAttribute("data-theme");
    return a ? a === "dark" : window.matchMedia("(prefers-color-scheme: dark)").matches;
  }
  Site.isDark = isDark;
  function syncThemeIcon() { var b = $("#themeBtn"); if (b) b.textContent = isDark() ? "☀" : "☾"; }
  document.addEventListener("click", function (e) {
    if (e.target.closest("#themeBtn")) {
      var next = isDark() ? "light" : "dark";
      root.setAttribute("data-theme", next); store.set("theme", next); syncThemeIcon();
    }
  });

  /* ---------- mobile menu ---------- */
  document.addEventListener("click", function (e) {
    var h = e.target.closest(".hamburger");
    if (h) { var m = $(".menu"); var o = m.classList.toggle("open"); h.setAttribute("aria-expanded", o); }
  });

  /* ---------- universal search: stock code -> markets, other number -> decoder ---------- */
  document.addEventListener("submit", function (e) {
    var f = e.target;
    if (!f.matches(".search, .hero-search")) return;
    e.preventDefault();
    var q = (f.querySelector("input").value || "").trim();
    if (!q) return;
    var digits = q.replace(/\D/g, "");
    if (/^(hk)?\s*\d{1,5}(\.hk)?$/i.test(q) && f.dataset.mode !== "decode" && /^0/.test(digits) && digits.length === 5) {
      location.href = "markets.html?s=" + digits;
    } else if (digits) {
      location.href = "decoder.html?n=" + encodeURIComponent(digits);
    } else {
      location.href = "learn.html?q=" + encodeURIComponent(q);
    }
  });

  /* ---------- hidden-email links: <a data-mail="Subject">text</a> ---------- */
  document.addEventListener("click", function (e) {
    var a = e.target.closest("[data-mail]");
    if (!a) return;
    e.preventDefault();
    var subj = a.getAttribute("data-mail") || "Inquiry from 01810.com";
    window.location.href = "mail" + "to:" + inbox() + "?subject=" + encodeURIComponent(subj);
  });

  /* ---------- UTM / source capture ---------- */
  (function () {
    var p = new URLSearchParams(location.search), u = store.get("utm", {});
    ["utm_source", "utm_medium", "utm_campaign", "ref"].forEach(function (k) { if (p.get(k)) u[k] = p.get(k); });
    if (!u.landing) u.landing = location.pathname;
    if (!u.referrer && document.referrer) u.referrer = document.referrer;
    store.set("utm", u);
  })();

  /* ---------- forms: AJAX to FormSubmit using runtime inbox ---------- */
  function endpoint() { return "https://formsubmit.co/ajax/" + inbox(); }
  function submitForm(form) {
    var status = form.querySelector(".form-status");
    var btn = form.querySelector("[type=submit]");
    var hp = form.querySelector(".hp input");
    if (hp && hp.value) return; // bot
    if (!form.checkValidity()) { form.reportValidity(); return; }
    var data = {};
    new FormData(form).forEach(function (v, k) {
      if (k === "_honey") return;
      data[k] = data[k] ? data[k] + ", " + v : v;
    });
    var name = form.getAttribute("data-form") || "Website form";
    data._subject = "[01810.com] " + name + (data.name ? " — " + data.name : "");
    data._template = "table";
    data._captcha = "false";
    data["Form"] = name;
    data["Page"] = location.href;
    var u = store.get("utm", {});
    Object.keys(u).forEach(function (k) { data["Source " + k] = u[k]; });
    if (form._extra) Object.assign(data, form._extra());
    if (data.email) data._replyto = data.email;
    if (btn) { btn.disabled = true; btn._t = btn.textContent; btn.textContent = "Sending…"; }
    fetch(endpoint(), { method: "POST", headers: { "Content-Type": "application/json", "Accept": "application/json" }, body: JSON.stringify(data) })
      .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { if (!r.ok || j.success === "false" || j.success === false) throw new Error(j.message || "Send failed"); return j; }); })
      .then(function () {
        if (status) { status.className = "form-status ok"; status.textContent = form.getAttribute("data-success") || "Thank you! We received your submission and will be in touch shortly."; }
        form.reset(); store.set("lead_done", true);
        document.dispatchEvent(new CustomEvent("lead:success", { detail: { form: name, data: data } }));
        if (window.gtag) window.gtag("event", "generate_lead", { form_name: name });
      })
      .catch(function () {
        // Fallback: open the visitor's mail app with the details (address stays hidden in markup)
        if (status) { status.className = "form-status err"; status.innerHTML = "Our form service is busy. <a href='#' class='fallback-mail'>Click here to send it by email instead</a>."; }
        var link = status && status.querySelector(".fallback-mail");
        if (link) link.addEventListener("click", function (ev) {
          ev.preventDefault();
          var body = Object.keys(data).filter(function (k) { return k.charAt(0) !== "_"; }).map(function (k) { return k + ": " + data[k]; }).join("\n");
          location.href = "mail" + "to:" + inbox() + "?subject=" + encodeURIComponent(data._subject) + "&body=" + encodeURIComponent(body);
        });
      })
      .then(function () { if (btn) { btn.disabled = false; btn.textContent = btn._t; } });
  }
  Site.submitForm = submitForm;
  document.addEventListener("submit", function (e) {
    var f = e.target.closest("form[data-form]");
    if (!f) return;
    e.preventDefault();
    if (f.hasAttribute("data-custom")) return; // handled by page script
    submitForm(f);
  });

  /* ---------- ads: AdSense when configured + consented, else house ads ---------- */
  var consent = store.get("consent", null);
  function houseAd(el) {
    el.innerHTML = '<div><b>Your brand here</b><br><span>Reach investors & culture lovers across Asia and the diaspora.</span><br><a href="advertise.html">Advertise on 01810 →</a></div>';
  }
  function loadAds() {
    var slots = $$(".ad");
    if (!C.adsenseClient || consent !== "all") { slots.forEach(houseAd); return; }
    var s = document.createElement("script");
    s.async = true; s.crossOrigin = "anonymous";
    s.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + C.adsenseClient;
    document.head.appendChild(s);
    slots.forEach(function (el) {
      var type = (el.className.match(/\b(leader|rect|inart|tall)\b/) || [])[1] || "rect";
      el.classList.add("filled");
      el.innerHTML = '<ins class="adsbygoogle" style="display:block;width:100%" data-ad-client="' + C.adsenseClient + '"' +
        (C.adsenseSlots && C.adsenseSlots[type] ? ' data-ad-slot="' + C.adsenseSlots[type] + '"' : "") +
        ' data-ad-format="auto" data-full-width-responsive="true"></ins>';
      try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
    });
  }
  function loadAnalytics() {
    if (!C.ga4 || consent !== "all") return;
    var s = document.createElement("script"); s.async = true; s.src = "https://www.googletagmanager.com/gtag/js?id=" + C.ga4;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { dataLayer.push(arguments); };
    gtag("js", new Date()); gtag("config", C.ga4);
  }

  /* ---------- cookie consent ---------- */
  function initConsent() {
    var box = $("#cookie");
    if (!box) return;
    if (consent === null) box.classList.add("show");
    box.addEventListener("click", function (e) {
      var b = e.target.closest("[data-consent]");
      if (!b) return;
      consent = b.getAttribute("data-consent"); store.set("consent", consent);
      box.classList.remove("show"); loadAds(); loadAnalytics();
    });
  }

  /* ---------- lazy YouTube (privacy-enhanced) ---------- */
  function videoHTML(v) {
    return '<div class="video-card"><div class="video" data-yt="' + v.id + '" role="button" tabindex="0" aria-label="Play: ' + v.title.replace(/"/g, "") + '">' +
      '<img loading="lazy" src="https://i.ytimg.com/vi/' + v.id + '/hqdefault.jpg" alt="">' +
      '<div class="play"><span>▶</span></div></div><h3>' + v.title + '</h3><div class="small muted">' + (v.by || "") + '</div></div>';
  }
  Site.videoHTML = videoHTML;
  function playVideo(el) {
    var id = el.getAttribute("data-yt");
    el.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0" title="YouTube video" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';
  }
  document.addEventListener("click", function (e) { var v = e.target.closest(".video[data-yt]"); if (v && !v.querySelector("iframe")) playVideo(v); });
  document.addEventListener("keydown", function (e) { if (e.key === "Enter") { var v = e.target.closest && e.target.closest(".video[data-yt]"); if (v && !v.querySelector("iframe")) playVideo(v); } });
  function renderVideoLists() {
    $$("[data-videos]").forEach(function (box) {
      var cat = box.getAttribute("data-videos"), n = +box.getAttribute("data-limit") || 99;
      var list = (C.videos || []).filter(function (v) { return cat === "all" || v.cat === cat; }).slice(0, n);
      box.innerHTML = list.map(videoHTML).join("");
    });
    $$("[data-yt-channel]").forEach(function (a) { a.href = C.youtubeChannel; });
  }

  /* ---------- TradingView widget helper (free embeds, delayed data) ---------- */
  Site.tv = function (container, type, cfg) {
    if (!container) return;
    container.innerHTML = "";
    var w = document.createElement("div"); w.className = "tradingview-widget-container";
    var inner = document.createElement("div"); inner.className = "tradingview-widget-container__widget"; w.appendChild(inner);
    var s = document.createElement("script"); s.type = "text/javascript"; s.async = true;
    s.src = "https://s3.tradingview.com/external-embedding/embed-widget-" + type + ".js";
    cfg.colorTheme = cfg.colorTheme || (isDark() ? "dark" : "light");
    cfg.locale = cfg.locale || "en";
    s.innerHTML = JSON.stringify(cfg);
    w.appendChild(s); container.appendChild(w);
  };
  function ticker() {
    var el = $("#ticker"); if (!el) return;
    Site.tv(el, "ticker-tape", {
      symbols: [
        { proName: "HSI:HSI", title: "Hang Seng" },
        { proName: "HSI:HSTECH", title: "HS TECH" },
        { proName: "HSI:HSCEI", title: "HS China Ent." },
        { proName: "SSE:000300", title: "CSI 300" },
        { proName: "SSE:000001", title: "Shanghai Comp." },
        { proName: "FX_IDC:USDCNH", title: "USD/CNH" },
        { proName: "FX_IDC:USDHKD", title: "USD/HKD" },
        { proName: "TVC:GOLD", title: "Gold" },
        { proName: "BITSTAMP:BTCUSD", title: "Bitcoin" }
      ],
      showSymbolLogo: true, isTransparent: true, displayMode: "adaptive", colorTheme: "dark"
    });
  }

  /* ---------- exit-intent / timed lead modal ---------- */
  function initModal() {
    var m = $("#leadModal"); if (!m) return;
    var shown = store.get("modal_seen", 0), done = store.get("lead_done", false);
    function open() { if (done || Date.now() - shown < 3 * 864e5 || m._o) return; m._o = true; m.classList.add("show"); store.set("modal_seen", Date.now()); }
    m.addEventListener("click", function (e) { if (e.target === m || e.target.closest(".close")) m.classList.remove("show"); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") m.classList.remove("show"); });
    document.addEventListener("mouseout", function (e) { if (!e.relatedTarget && e.clientY < 8) open(); });
    setTimeout(open, 45000);
  }

  /* ---------- countdown ---------- */
  function countdown() {
    var el = $("[data-countdown]"); if (!el) return;
    var end = new Date(C.contestEnds).getTime();
    function tick() {
      var d = Math.max(0, end - Date.now()), s = Math.floor(d / 1000);
      var parts = [Math.floor(s / 86400), Math.floor(s % 86400 / 3600), Math.floor(s % 3600 / 60), s % 60];
      $$("b", el).forEach(function (b, i) { b.textContent = String(parts[i]).padStart(2, "0"); });
    }
    tick(); setInterval(tick, 1000);
  }

  /* ---------- misc ---------- */
  function misc() {
    $$("[data-year]").forEach(function (e) { e.textContent = new Date().getFullYear(); });
    var bt = $("#backTop");
    if (bt) {
      window.addEventListener("scroll", function () { bt.classList.toggle("show", scrollY > 900); }, { passive: true });
      bt.addEventListener("click", function () { scrollTo({ top: 0 }); });
    }
    // chips / option groups (single select)
    document.addEventListener("click", function (e) {
      var c = e.target.closest("[data-group] .chip, [data-group] .option, [data-group] .amount");
      if (!c) return;
      var g = c.closest("[data-group]");
      $$(".chip, .option, .amount", g).forEach(function (x) { x.classList.remove("active", "selected"); });
      c.classList.add(c.classList.contains("chip") ? "active" : "selected");
      g.dispatchEvent(new CustomEvent("pick", { detail: c.getAttribute("data-value") }));
    });
    // share buttons
    document.addEventListener("click", function (e) {
      var s = e.target.closest("[data-share]"); if (!s) return;
      var url = s.getAttribute("data-share") || location.href, text = s.getAttribute("data-text") || document.title;
      if (navigator.share) navigator.share({ title: text, url: url }).catch(function () {});
      else if (navigator.clipboard) navigator.clipboard.writeText(url).then(function () { toast("Link copied!"); });
    });
    var yt = $$("[data-social-youtube]"); yt.forEach(function (a) { a.href = C.youtubeChannel; });
  }

  document.addEventListener("DOMContentLoaded", function () {
    syncThemeIcon(); ticker(); initConsent(); loadAds(); loadAnalytics();
    renderVideoLists(); initModal(); countdown(); misc();
  });
})();
