/* 01810.com — interactive tools: Number Decoder, Zodiac, Compatibility, Kua, investor calculators, markets */
(function () {
  "use strict";
  var $ = Site.$, $$ = Site.$$;
  var fmt = function (n, d) { return Number(n).toLocaleString("en-US", { minimumFractionDigits: d || 0, maximumFractionDigits: d == null ? 2 : d }); };
  var qs = new URLSearchParams(location.search);

  /* =================== NUMBER DECODER =================== */
  var DIGITS = {
    "0": { zh: "零", py: "líng", sound: "sounds like 你 “you” in net slang; also 良 “good”", mean: "Wholeness, beginnings, the infinite", pts: 2, cls: "good" },
    "1": { zh: "一 / 幺", py: "yī / yāo", sound: "read “yāo” in numbers ≈ 要 “will / want”", mean: "Unity, leadership, first place", pts: 3, cls: "good" },
    "2": { zh: "二", py: "èr", sound: "“good things come in pairs” (好事成双)", mean: "Harmony, partnership, balance", pts: 5, cls: "good" },
    "3": { zh: "三", py: "sān", sound: "near 生 shēng “birth / life”", mean: "Growth, vitality", pts: 4, cls: "good" },
    "4": { zh: "四", py: "sì", sound: "sounds like 死 sǐ “death”", mean: "The most avoided digit — floors & plates skip it", pts: -14, cls: "bad" },
    "5": { zh: "五", py: "wǔ", sound: "五行 — the five elements; also 无 “not / none”", mean: "Balance of elements; neutral", pts: 0, cls: "" },
    "6": { zh: "六", py: "liù", sound: "≈ 流 liú “flow” — 六六大顺 “everything goes smoothly”", mean: "Smooth progress, success", pts: 9, cls: "great" },
    "7": { zh: "七", py: "qī", sound: "≈ 起 qǐ “rise”, but also 气 “anger”; Ghost Month is the 7th", mean: "Mixed — togetherness or rising energy", pts: -1, cls: "" },
    "8": { zh: "八", py: "bā", sound: "≈ 發 fā “prosper / get rich”", mean: "Wealth, fortune — the luckiest digit", pts: 14, cls: "great" },
    "9": { zh: "九", py: "jiǔ", sound: "≈ 久 jiǔ “long-lasting”", mean: "Longevity, eternity — the emperor's number", pts: 8, cls: "great" }
  };
  var COMBOS = [
    { k: "01810", t: "“You will prosper — the whole circle.” Our house reading: 0 (you) · 1 (will) · 8 (prosper) · 1 (will) · 0 (whole). A modern play on sounds, framed by two zeros of completeness.", p: 12 },
    { k: "0181", t: "你要发 (nǐ yào fā) — “you will prosper”, modern net-slang style reading.", p: 10 },
    { k: "1314", t: "一生一世 — “one life, one lifetime” (forever). Popular in love & wedding numbers.", p: 8 },
    { k: "520", t: "我爱你 — “I love you”. 20 May is the unofficial Chinese Valentine's Day.", p: 7 },
    { k: "521", t: "我愿意 — “I'm willing / I do”.", p: 5 },
    { k: "168", t: "一路发 — “prosper all the way”. A favourite for shops and phone numbers.", p: 12 },
    { k: "518", t: "我要发 — “I will prosper”.", p: 11 },
    { k: "888", t: "發發發 — triple prosperity.", p: 15 },
    { k: "88", t: "發發 — double prosperity (also “bye-bye” in chat).", p: 8 },
    { k: "666", t: "六六六 — “everything goes smoothly”; also slang for “awesome”.", p: 10 },
    { k: "999", t: "久久久 — lasting forever.", p: 8 },
    { k: "189", t: "一八九 ≈ 要发久 — “will prosper for long”.", p: 7 },
    { k: "18", t: "实发 / 要发 — “sure / will prosper”. HK plate “18” sold for HK$16.5M in 2008.", p: 8 },
    { k: "28", t: "易发 — “easy prosperity”. HK plate “28” fetched HK$18.1M in 2016.", p: 8 },
    { k: "38", t: "生发 — “growing wealth”.", p: 6 },
    { k: "68", t: "路发 — “the road to riches”.", p: 7 },
    { k: "98", t: "久发 — “lasting wealth”.", p: 7 },
    { k: "1688", t: "一路发发 — “prosperity all the way, doubled”.", p: 12 },
    { k: "5201314", t: "我爱你一生一世 — “I love you for a lifetime”.", p: 10 },
    { k: "14", t: "要死 — “want to die” (1 as yāo + 4). Strongly avoided.", p: -12 },
    { k: "74", t: "气死 — “furious / angered to death”.", p: -8 },
    { k: "514", t: "我要死 — “I'll die”. Avoided.", p: -10 },
    { k: "250", t: "二百五 — slang for “idiot”. Avoid for gifts!", p: -8 },
    { k: "4444", t: "Quadruple 4 — the least-wanted combination.", p: -10 },
    { k: "13", t: "一生 — “a lifetime” (neutral-positive in Chinese, unlike the West).", p: 2 }
  ];
  function decode(num) {
    num = String(num).replace(/\D/g, "").slice(0, 20);
    if (!num) return null;
    var score = 50, found = [], sum = 0, bonus = 0;
    num.split("").forEach(function (d) { sum += DIGITS[d].pts; });
    score += (sum / num.length) * 3;
    COMBOS.forEach(function (c) { if (num.indexOf(c.k) > -1) { found.push(c); bonus += c.p; } });
    score += Math.max(-25, Math.min(20, bonus));
    var eights = (num.match(/8/g) || []).length, fours = (num.match(/4/g) || []).length;
    if (!fours) score += 6;
    if (/(\d)\1\1/.test(num)) score += 4; // repeating triples feel "premium"
    if (num[num.length - 1] === "8" || num[num.length - 1] === "9") score += 4;
    score = Math.max(1, Math.min(99, Math.round(score)));
    var verdict = score >= 85 ? "Exceptionally auspicious" : score >= 70 ? "Very lucky" : score >= 55 ? "Favourable" : score >= 40 ? "Neutral" : score >= 25 ? "Mixed — use with care" : "Considered unlucky";
    return { num: num, score: score, verdict: verdict, combos: found, eights: eights, fours: fours };
  }
  window.Decoder = { decode: decode, DIGITS: DIGITS };

  function renderDecoder() {
    var form = $("#decoderForm"); if (!form) return;
    var input = $("#decoderInput"), out = $("#decoderResult");
    function run(v) {
      var r = decode(v); if (!r) return;
      input.value = r.num;
      var h = '<div class="score"><div class="gauge" style="--p:' + r.score + '"><span>' + r.score + '</span></div>' +
        '<div><span class="tag ' + (r.score >= 55 ? "" : r.score >= 40 ? "gold" : "red") + '">' + r.verdict + '</span>' +
        '<h3 class="mt-1" style="font-size:1.8rem;letter-spacing:.08em">' + r.num + '</h3>' +
        '<div class="muted small">Luck score out of 99 · ' + r.eights + '× “8” · ' + r.fours + '× “4”</div></div></div>';
      h += '<div class="digits">' + r.num.split("").map(function (d) {
        var x = DIGITS[d];
        return '<div class="digit ' + x.cls + '"><div class="n">' + d + '</div><div class="zh">' + x.zh + '</div><small>' + x.py + '</small></div>';
      }).join("") + "</div>";
      if (r.combos.length) {
        h += "<h3>Hidden phrases found</h3><ul class='list-check'>" + r.combos.map(function (c) { return "<li><b>" + c.k + "</b> — " + c.t + "</li>"; }).join("") + "</ul>";
      }
      var uniq = r.num.split("").filter(function (d, i, a) { return a.indexOf(d) === i; });
      h += "<h3>Digit by digit</h3><div class='table-wrap'><table><tr><th>Digit</th><th>Sound-alike</th><th>Meaning</th></tr>" +
        uniq.map(function (d) { var x = DIGITS[d]; return "<tr><td><b>" + d + "</b> <span class='zh'>" + x.zh + "</span></td><td>" + x.sound + "</td><td>" + x.mean + "</td></tr>"; }).join("") + "</table></div>";
      if (r.num.length <= 5) {
        var code = r.num.padStart(5, "0");
        h += "<div class='notice mt-2'>📈 <b>Lucky ticker:</b> <b>" + code + "</b> is also a possible Hong Kong stock code format. <a href='markets.html?s=" + code + "'>Look up " + code + " on our Markets page →</a></div>";
      }
      h += "<div class='hero-actions'><button class='btn btn-gold' data-share='" + location.origin + location.pathname + "?n=" + r.num + "' data-text='My number " + r.num + " scored " + r.score + "/99 on 01810.com'>Share my result</button>" +
        "<a class='btn btn-primary' href='#report'>Email me the full report</a></div>";
      out.innerHTML = h; out.classList.add("show");
      var rep = $("#reportNumber"); if (rep) rep.value = r.num;
      history.replaceState(null, "", "?n=" + r.num);
    }
    form.addEventListener("submit", function (e) { e.preventDefault(); run(input.value); });
    $$("[data-try]").forEach(function (b) { b.addEventListener("click", function () { run(b.getAttribute("data-try")); out.scrollIntoView({ behavior: "smooth", block: "start" }); }); });
    run(qs.get("n") || "01810");
  }

  /* =================== ZODIAC =================== */
  var ANIMALS = [
    { n: "Rat", zh: "鼠", e: "🐀", t: "Quick-witted, resourceful, versatile", lucky: "2, 3", col: "Blue, gold, green" },
    { n: "Ox", zh: "牛", e: "🐂", t: "Diligent, dependable, strong, determined", lucky: "1, 4", col: "White, yellow, green" },
    { n: "Tiger", zh: "虎", e: "🐅", t: "Brave, confident, competitive", lucky: "1, 3, 4", col: "Blue, grey, orange" },
    { n: "Rabbit", zh: "兔", e: "🐇", t: "Gentle, elegant, alert, responsible", lucky: "3, 4, 6", col: "Red, pink, purple, blue" },
    { n: "Dragon", zh: "龙", e: "🐉", t: "Confident, intelligent, enthusiastic", lucky: "1, 6, 7", col: "Gold, silver, grey-white" },
    { n: "Snake", zh: "蛇", e: "🐍", t: "Enigmatic, intelligent, wise", lucky: "2, 8, 9", col: "Black, red, yellow" },
    { n: "Horse", zh: "马", e: "🐎", t: "Animated, active, energetic", lucky: "2, 3, 7", col: "Yellow, green" },
    { n: "Goat", zh: "羊", e: "🐐", t: "Calm, gentle, sympathetic", lucky: "2, 7", col: "Brown, red, purple" },
    { n: "Monkey", zh: "猴", e: "🐒", t: "Sharp, smart, curious", lucky: "4, 9", col: "White, blue, gold" },
    { n: "Rooster", zh: "鸡", e: "🐓", t: "Observant, hardworking, courageous", lucky: "5, 7, 8", col: "Gold, brown, yellow" },
    { n: "Dog", zh: "狗", e: "🐕", t: "Loyal, honest, prudent", lucky: "3, 4, 9", col: "Red, green, purple" },
    { n: "Pig", zh: "猪", e: "🐖", t: "Compassionate, generous, diligent", lucky: "2, 5, 8", col: "Yellow, grey, brown, gold" }
  ];
  var ELEMENTS = ["Wood", "Wood", "Fire", "Fire", "Earth", "Earth", "Metal", "Metal", "Water", "Water"];
  function chineseYear(date) {
    try {
      var parts = new Intl.DateTimeFormat("en-u-ca-chinese", { year: "numeric", timeZone: "UTC" }).formatToParts(date);
      var ry = parts.filter(function (p) { return p.type === "relatedYear"; })[0];
      if (ry) return +ry.value;
    } catch (e) {}
    // Fallback: approximate Lunar New Year boundary at 4 Feb
    var y = date.getUTCFullYear();
    return (date.getUTCMonth() === 0 || (date.getUTCMonth() === 1 && date.getUTCDate() < 4)) ? y - 1 : y;
  }
  function zodiacOf(date) {
    var y = chineseYear(date);
    var a = ANIMALS[((y - 4) % 12 + 12) % 12];
    return { year: y, animal: a, idx: ((y - 4) % 12 + 12) % 12, element: ELEMENTS[((y - 4) % 10 + 10) % 10], yin: (y % 2) ? "Yin" : "Yang" };
  }
  window.Zodiac = { zodiacOf: zodiacOf, ANIMALS: ANIMALS };
  var TRINES = [[0, 4, 8], [1, 5, 9], [2, 6, 10], [3, 7, 11]];
  var FRIENDS = [[0, 1], [2, 11], [3, 10], [4, 9], [5, 8], [6, 7]];
  var HARMS = [[0, 7], [1, 6], [2, 5], [3, 4], [8, 11], [9, 10]];
  function compat(a, b) {
    var inTrine = TRINES.some(function (t) { return t.indexOf(a) > -1 && t.indexOf(b) > -1; }) && a !== b;
    var friend = FRIENDS.some(function (f) { return (f[0] === a && f[1] === b) || (f[0] === b && f[1] === a); });
    var clash = Math.abs(a - b) === 6;
    var harm = HARMS.some(function (f) { return (f[0] === a && f[1] === b) || (f[0] === b && f[1] === a); });
    if (friend) return { s: 95, t: "Secret friends (六合) — a natural, deeply supportive match." };
    if (inTrine) return { s: 88, t: "Triple harmony (三合) — shared values and easy teamwork." };
    if (a === b) return { s: 70, t: "Same sign — you understand each other, but may compete." };
    if (clash) return { s: 28, t: "Direct clash (六冲) — opposite energies; needs patience and compromise." };
    if (harm) return { s: 40, t: "Harm pairing (六害) — small misunderstandings can grow; communicate openly." };
    return { s: 62, t: "Neutral pairing — success depends on effort and shared goals." };
  }
  function renderZodiac() {
    var f = $("#zodiacForm"); if (!f) return;
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var v = $("#zDob").value; if (!v) return;
      var z = zodiacOf(new Date(v + "T12:00:00Z")), a = z.animal;
      $("#zodiacResult").innerHTML =
        '<div class="score"><div style="font-size:4rem">' + a.e + '</div><div><span class="tag gold">' + z.element + " " + a.n + " · " + z.yin + '</span>' +
        '<h3 class="mt-1" style="font-size:1.8rem">' + a.n + ' <span class="zh">' + a.zh + '</span></h3><div class="muted">Chinese year ' + z.year + ' (Lunar New Year aware)</div></div></div>' +
        '<div class="kv"><div><small>Personality</small><b style="font-size:1rem">' + a.t + '</b></div><div><small>Lucky numbers</small><b>' + a.lucky + '</b></div><div><small>Lucky colours</small><b style="font-size:1rem">' + a.col + '</b></div><div><small>Element</small><b>' + z.element + '</b></div></div>' +
        '<div class="hero-actions"><button class="btn btn-gold" data-share data-text="I\'m a ' + z.element + " " + a.n + ' — find yours on 01810.com">Share</button><a class="btn btn-primary" href="get-started.html#reading">Get a personal reading</a></div>';
      $("#zodiacResult").classList.add("show");
    });
    var sa = $("#cA"), sb = $("#cB");
    if (sa && sb) {
      var opts = ANIMALS.map(function (a, i) { return '<option value="' + i + '">' + a.e + " " + a.n + "</option>"; }).join("");
      sa.innerHTML = opts; sb.innerHTML = opts; sb.value = 4;
      $("#compatForm").addEventListener("submit", function (e) {
        e.preventDefault();
        var r = compat(+sa.value, +sb.value);
        $("#compatResult").innerHTML = '<div class="score"><div class="gauge" style="--p:' + r.s + '"><span>' + r.s + '</span></div><div><h3>' + ANIMALS[sa.value].n + " + " + ANIMALS[sb.value].n + '</h3><p class="muted mt-0">' + r.t + "</p></div></div>";
        $("#compatResult").classList.add("show");
      });
    }
    var grid = $("#animalGrid");
    if (grid) {
      var now = zodiacOf(new Date()).year;
      grid.innerHTML = ANIMALS.map(function (a, i) {
        var yrs = []; for (var y = 1936; y <= 2043; y++) if (((y - 4) % 12 + 12) % 12 === i) yrs.push(y);
        return '<div class="card"><div style="font-size:2rem">' + a.e + '</div><h3>' + a.n + ' <span class="zh">' + a.zh + '</span></h3><p class="small">' + a.t + '</p><div class="small muted">Years: ' + yrs.map(function (y) { return y === now ? "<b>" + y + "</b>" : y; }).join(", ") + '</div></div>';
      }).join("");
    }
  }

  /* =================== KUA NUMBER =================== */
  var KUA = {
    1: ["SE", "E", "S", "N"], 2: ["NE", "W", "NW", "SW"], 3: ["S", "N", "SE", "E"], 4: ["N", "S", "E", "SE"],
    6: ["W", "NE", "SW", "NW"], 7: ["NW", "SW", "NE", "W"], 8: ["SW", "NW", "W", "NE"], 9: ["E", "SE", "N", "S"]
  };
  var DIRN = { N: "North", S: "South", E: "East", W: "West", NE: "North-East", NW: "North-West", SE: "South-East", SW: "South-West" };
  function reduce(n) { while (n > 9) n = String(n).split("").reduce(function (a, b) { return a + +b; }, 0); return n; }
  function kua(dateStr, gender) {
    var d = new Date(dateStr + "T12:00:00Z"), y = d.getUTCFullYear();
    if (d.getUTCMonth() === 0 || (d.getUTCMonth() === 1 && d.getUTCDate() < 4)) y--; // solar year starts ~4 Feb
    var r = reduce(y % 100), k;
    if (gender === "m") { k = y < 2000 ? 10 - r : 9 - r; if (k === 0) k = 9; k = reduce(k); if (k === 5) k = 2; }
    else { k = y < 2000 ? 5 + r : 6 + r; k = reduce(k); if (k === 5) k = 8; }
    return k;
  }
  function renderKua() {
    var f = $("#kuaForm"); if (!f) return;
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var k = kua($("#kDob").value, $("#kGender").value), d = KUA[k];
      var group = [1, 3, 4, 9].indexOf(k) > -1 ? "East group" : "West group";
      var labels = ["Wealth & success (生气)", "Health (天医)", "Love & relationships (延年)", "Personal growth (伏位)"];
      $("#kuaResult").innerHTML = '<div class="score"><div class="gauge" style="--p:' + k * 11 + '"><span>' + k + '</span></div><div><span class="tag">' + group + '</span><h3 class="mt-1">Your Kua number is ' + k + '</h3><p class="muted mt-0">Face or sleep toward these directions to align with your favourable energy.</p></div></div>' +
        '<div class="kv">' + d.map(function (x, i) { return "<div><small>" + labels[i] + "</small><b>" + DIRN[x] + "</b></div>"; }).join("") + "</div>";
      $("#kuaResult").classList.add("show");
    });
  }

  /* =================== INVESTOR CALCULATORS =================== */
  function renderCalcs() {
    var t = $("#costForm");
    if (t) {
      var calc = function (e) {
        if (e) e.preventDefault();
        var px = +$("#cPrice").value, qty = +$("#cQty").value, comm = +$("#cComm").value / 100, min = +$("#cMin").value, side = $("#cSide").value;
        var v = px * qty;
        var stamp = Math.ceil(v * 0.001); // 0.1% per side, rounded up to whole HK$
        var sfc = v * 0.000027, afrc = v * 0.0000015, trade = v * 0.0000565, brk = Math.max(v * comm, min), settle = Math.min(Math.max(v * 0.00002, 2), 100);
        var total = stamp + sfc + afrc + trade + brk + settle;
        $("#costResult").innerHTML = '<div class="kv"><div><small>Trade value</small><b>HK$' + fmt(v) + '</b></div><div><small>Stamp duty (0.1%)</small><b>HK$' + fmt(stamp) + '</b></div><div><small>SFC levy (0.0027%)</small><b>HK$' + fmt(sfc) + '</b></div><div><small>AFRC levy (0.00015%)</small><b>HK$' + fmt(afrc) + '</b></div><div><small>HKEX trading fee (0.00565%)</small><b>HK$' + fmt(trade) + '</b></div><div><small>Settlement (est.)</small><b>HK$' + fmt(settle) + '</b></div><div><small>Broker commission</small><b>HK$' + fmt(brk) + '</b></div><div style="background:rgba(226,61,61,.1)"><small>Total ' + side + ' cost</small><b>HK$' + fmt(total) + ' <small>(' + fmt(total / v * 100, 3) + '%)</small></b></div></div>';
        $("#costResult").classList.add("show");
      };
      t.addEventListener("submit", calc); calc();
    }
    var g = $("#growthForm");
    if (g) {
      var gc = function (e) {
        if (e) e.preventDefault();
        var p = +$("#gP").value, m = +$("#gM").value, r = +$("#gR").value / 100, y = +$("#gY").value;
        var bal = p, contrib = p, rows = [];
        for (var i = 1; i <= y; i++) { for (var k = 0; k < 12; k++) { bal = bal * (1 + r / 12) + m; contrib += m; } if (i % Math.max(1, Math.round(y / 8)) === 0 || i === y) rows.push([i, contrib, bal]); }
        $("#growthResult").innerHTML = '<div class="kv"><div><small>Final balance</small><b class="pos">$' + fmt(bal, 0) + '</b></div><div><small>Total contributed</small><b>$' + fmt(contrib, 0) + '</b></div><div><small>Growth earned</small><b>$' + fmt(bal - contrib, 0) + '</b></div></div>' +
          '<div class="table-wrap mt-1"><table><tr><th>Year</th><th>Contributed</th><th>Balance</th></tr>' + rows.map(function (x) { return "<tr><td>" + x[0] + "</td><td>$" + fmt(x[1], 0) + "</td><td>$" + fmt(x[2], 0) + "</td></tr>"; }).join("") + "</table></div>";
        $("#growthResult").classList.add("show");
      };
      g.addEventListener("submit", gc); gc();
    }
    var dv = $("#divForm");
    if (dv) {
      var dc = function (e) {
        if (e) e.preventDefault();
        var inv = +$("#dInv").value, yld = +$("#dY").value / 100, gr = +$("#dG").value / 100, yrs = +$("#dYrs").value, tax = +$("#dTax").value / 100;
        var shares = inv, income = 0, first = inv * yld * (1 - tax), last = 0, dps = yld;
        for (var i = 0; i < yrs; i++) { var d = shares * dps * (1 - tax); income += d; last = d; shares += d; dps *= (1 + gr); }
        $("#divResult").innerHTML = '<div class="kv"><div><small>Year-1 income</small><b>$' + fmt(first, 0) + '</b></div><div><small>Final-year income (DRIP)</small><b class="pos">$' + fmt(last, 0) + '</b></div><div><small>Total dividends</small><b>$' + fmt(income, 0) + '</b></div><div><small>Portfolio value*</small><b>$' + fmt(shares, 0) + '</b></div></div><p class="small muted mt-1">*Assumes flat share price; dividends reinvested. HK does not tax dividends locally; mainland-company H-shares may withhold 10–20%.</p>';
        $("#divResult").classList.add("show");
      };
      dv.addEventListener("submit", dc); dc();
    }
    var ps = $("#posForm");
    if (ps) {
      var pc = function (e) {
        if (e) e.preventDefault();
        var acct = +$("#pAcct").value, risk = +$("#pRisk").value / 100, entry = +$("#pEntry").value, stop = +$("#pStop").value, lot = +$("#pLot").value, fx = +$("#pFx").value;
        var riskAmt = acct * risk, per = Math.abs(entry - stop);
        var shares = per > 0 ? Math.floor(riskAmt / per) : 0, lots = Math.floor(shares / lot), realShares = lots * lot;
        $("#posResult").innerHTML = '<div class="kv"><div><small>Max risk</small><b>HK$' + fmt(riskAmt, 0) + '</b></div><div><small>Board lots</small><b>' + fmt(lots, 0) + '</b></div><div><small>Shares</small><b>' + fmt(realShares, 0) + '</b></div><div><small>Position (HKD)</small><b>HK$' + fmt(realShares * entry, 0) + '</b></div><div><small>Position (USD)</small><b>US$' + fmt(realShares * entry / fx, 0) + '</b></div><div><small>Risk if stopped</small><b class="neg">HK$' + fmt(realShares * per, 0) + '</b></div></div>';
        $("#posResult").classList.add("show");
      };
      ps.addEventListener("submit", pc); pc();
    }
  }

  /* =================== MARKETS =================== */
  function tvSymbol(code) { return "HKEX:" + String(parseInt(code, 10)); }
  function renderMarkets() {
    var chart = $("#tvChart"); if (!chart) return;
    var input = $("#symInput");
    function load(code) {
      code = String(code).replace(/\D/g, "").slice(0, 5); if (!code) return;
      var padded = code.padStart(5, "0");
      input.value = padded; $("#symTitle").textContent = "HK " + padded;
      $("#symLinks").innerHTML = '<a href="https://www.hkexnews.hk/" target="_blank" rel="noopener">HKEXnews filings ↗</a> · <a href="https://www.tradingview.com/symbols/HKEX-' + parseInt(code, 10) + '/" target="_blank" rel="noopener">Full chart ↗</a> · <a href="decoder.html?n=' + padded + '">Decode ' + padded + ' ✦</a>';
      Site.tv(chart, "advanced-chart", { autosize: true, symbol: tvSymbol(code), interval: "D", timezone: "Asia/Hong_Kong", style: "1", allow_symbol_change: true, hide_side_toolbar: false, calendar: false, support_host: "https://www.tradingview.com" });
      Site.tv($("#tvProfile"), "symbol-info", { symbol: tvSymbol(code), width: "100%", isTransparent: true });
      history.replaceState(null, "", "?s=" + padded);
    }
    $("#symForm").addEventListener("submit", function (e) { e.preventDefault(); load(input.value); });
    $$("[data-sym]").forEach(function (b) { b.addEventListener("click", function () { load(b.getAttribute("data-sym")); chart.scrollIntoView({ behavior: "smooth" }); }); });
    load(qs.get("s") || "01810");
    // watchlist
    var wl = Site.store.get("watchlist", ["00700", "09988", "01810", "03690", "01211"]);
    function drawWL() {
      $("#watchlist").innerHTML = wl.length ? wl.map(function (c) { return '<span class="chip"><a href="#" data-load="' + c + '">' + c + '</a> <button aria-label="Remove ' + c + '" data-rm="' + c + '" style="border:0;background:none;cursor:pointer;color:var(--soft)">×</button></span>'; }).join("") : '<span class="muted small">Your watchlist is empty.</span>';
    }
    drawWL();
    $("#watchlist").addEventListener("click", function (e) {
      var l = e.target.closest("[data-load]"), r = e.target.closest("[data-rm]");
      if (l) { e.preventDefault(); load(l.getAttribute("data-load")); chart.scrollIntoView({ behavior: "smooth" }); }
      if (r) { wl = wl.filter(function (x) { return x !== r.getAttribute("data-rm"); }); Site.store.set("watchlist", wl); drawWL(); }
    });
    $("#wlAdd").addEventListener("click", function () {
      var c = input.value.replace(/\D/g, "").padStart(5, "0");
      if (wl.indexOf(c) < 0) { wl.push(c); Site.store.set("watchlist", wl); drawWL(); Site.toast(c + " added to your watchlist"); }
    });
    // overview widgets
    Site.tv($("#tvOverview"), "market-overview", {
      width: "100%", height: 460, isTransparent: true, showChart: true, dateRange: "12M", showSymbolLogo: true,
      tabs: [
        { title: "Indices", symbols: [{ s: "HSI:HSI", d: "Hang Seng" }, { s: "HSI:HSTECH", d: "Hang Seng TECH" }, { s: "HSI:HSCEI", d: "HS China Enterprises" }, { s: "SSE:000300", d: "CSI 300" }, { s: "SSE:000001", d: "Shanghai Composite" }, { s: "SZSE:399001", d: "Shenzhen Component" }] },
        { title: "HK Tech", symbols: [{ s: "HKEX:700" }, { s: "HKEX:9988" }, { s: "HKEX:1810" }, { s: "HKEX:3690" }, { s: "HKEX:9618" }, { s: "HKEX:1024" }] },
        { title: "HK Finance", symbols: [{ s: "HKEX:5" }, { s: "HKEX:1299" }, { s: "HKEX:388" }, { s: "HKEX:939" }, { s: "HKEX:1398" }, { s: "HKEX:2318" }] },
        { title: "FX", symbols: [{ s: "FX_IDC:USDHKD", d: "USD/HKD" }, { s: "FX_IDC:USDCNH", d: "USD/CNH" }, { s: "FX_IDC:HKDCNY", d: "HKD/CNY" }] }
      ]
    });
    Site.tv($("#tvHot"), "hotlists", { exchange: "HKEX", dateRange: "12M", showChart: true, width: "100%", height: 460, isTransparent: true, showSymbolLogo: true });
    Site.tv($("#tvNews"), "timeline", { feedMode: "market", market: "stock", displayMode: "regular", width: "100%", height: 480, isTransparent: true });
    Site.tv($("#tvCal"), "events", { width: "100%", height: 480, isTransparent: true, importanceFilter: "0,1", countryFilter: "hk,cn,us" });
  }
  function renderHomeTV() {
    var el = $("#tvHome"); if (!el) return;
    Site.tv(el, "market-overview", {
      width: "100%", height: 420, isTransparent: true, showChart: true, dateRange: "3M", showSymbolLogo: true,
      tabs: [{ title: "Hong Kong & China", symbols: [{ s: "HSI:HSI", d: "Hang Seng" }, { s: "HSI:HSTECH", d: "HS TECH" }, { s: "SSE:000300", d: "CSI 300" }, { s: "HKEX:1810", d: "HK 01810" }, { s: "HKEX:700", d: "HK 00700" }] }]
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    renderDecoder(); renderZodiac(); renderKua(); renderCalcs(); renderMarkets(); renderHomeTV();
  });
})();
