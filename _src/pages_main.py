from build import page, ad, newsletter_inline, lead_box, sidebar, cta_band, page_hero, hp, status, SITE

LUCKY_CODES = ["00008", "00088", "00168", "00388", "00888", "01688", "01810", "01888", "02388", "06088", "08888", "00004"]

# ======================= HOME =======================
home = f'''
<section class="hero">
  <div class="container grid">
    <div>
      <span class="eyebrow">✦ Hong Kong &amp; China markets · Lucky-number culture</span>
      <h1 class="mt-1">Where markets meet the <span class="accent">meaning of numbers</span>.</h1>
      <p class="lead">01810 is your free hub for Hong Kong &amp; China investing, with live charts, calculators and plain-English guides. It also decodes the lucky numbers behind billion-dollar decisions, from 8888 phone numbers to HK$16M licence plates.</p>
      <form class="hero-search tool-input mt-2" data-mode="decode" role="search" style="max-width:560px">
        <input aria-label="Enter any number" placeholder="Enter any number: phone, plate, stock code…" inputmode="numeric" style="background:#fff;color:#111">
        <button class="btn btn-gold" type="submit">Decode it ✦</button>
      </form>
      <div class="hero-actions"><a class="btn btn-primary" href="get-started.html">Get my free investor plan →</a><a class="btn btn-ghost" href="markets.html">Explore markets</a></div>
      <div class="hero-stats"><div><b>5</b><span>free calculators</span></div><div><b>12</b><span>zodiac signs decoded</span></div><div><b>00001–09999</b><span>HK codes, decoded</span></div><div><b>$0</b><span>always free</span></div></div>
    </div>
    <div class="center">
      <div class="bignum">01810</div>
      <p class="zh" style="font-size:1.6rem;color:#ffd978;margin:.2em 0">你 · 要 · 发 · 要 · 圆</p>
      <p style="color:#c9d0e2">“You will prosper — the whole circle.”<br><small>Our house reading of 0-1-8-1-0. <a href="meaning-of-01810.html" style="color:#ffd978">Why this number matters →</a></small></p>
    </div>
  </div>
</section>
<div class="container">{ad("leader")}</div>

<section class="block"><div class="container">
  <div class="section-head"><div><span class="tag">Two pillars, one site</span><h2 class="mt-1">Everything you need, free</h2></div><p>Market tools for investors on one side, number-culture tools for everyone on the other. Both are free.</p></div>
  <div class="grid-4">
    <a class="card link" href="markets.html"><div class="ico">📈</div><h3>Markets</h3><p>Live charts for any HK stock code, index snapshot, hot lists, news and a watchlist saved in your browser.</p><span class="tag">Open →</span></a>
    <a class="card link" href="decoder.html"><div class="ico">✦</div><h3>Number Decoder</h3><p>Luck score, hidden phrases and a digit-by-digit reading for any phone number, plate, address or price.</p><span class="tag gold">Try it →</span></a>
    <a class="card link" href="zodiac.html"><div class="ico">🐉</div><h3>Zodiac &amp; Feng Shui</h3><p>Lunar-calendar-accurate zodiac, element, compatibility and your personal Kua directions.</p><span class="tag gold">Discover →</span></a>
    <a class="card link" href="tools.html"><div class="ico">🧮</div><h3>Investor Calculators</h3><p>HK stamp duty &amp; fees, compound growth, dividend/DRIP and board-lot position sizing.</p><span class="tag">Calculate →</span></a>
  </div>
</div></section>

<section class="block alt"><div class="container">
  <div class="section-head"><div><span class="tag">Market snapshot</span><h2 class="mt-1">Hong Kong &amp; China today</h2></div><a class="btn btn-jade btn-sm" href="markets.html">Full markets dashboard →</a></div>
  <div class="grid-2">
    <div class="tv-box"><div id="tvHome"></div></div>
    <div class="card">
      <h3>🀄 Lucky Ticker Board</h3>
      <p class="small">HK stock codes ranked by our Number Decoder luck score. This is for fun, not a buy list. Tap a code to decode it, or open its chart.</p>
      <div class="table-wrap"><table id="luckyBoard"><tr><th>Code</th><th>Luck</th><th></th></tr></table></div>
      <p class="form-note mt-1">Not every code is currently listed. The chart will tell you. Not investment advice.</p>
    </div>
  </div>
</div></section>

<section class="block"><div class="container">{lead_box(src="home")}</div></section>

<section class="block alt"><div class="container">
  <div class="section-head"><div><span class="tag">Learn</span><h2 class="mt-1">Guides investors actually finish</h2></div><a href="learn.html">All guides →</a></div>
  <div class="grid-3">
    <a class="card link" href="hk-stock-codes-explained.html"><span class="tag">Markets</span><h3 class="mt-1">How Hong Kong stock codes work</h3><p>Why codes are five digits, what 08xxx and 8xxxx mean, and how to read a ticker in seconds.</p></a>
    <a class="card link" href="why-8-is-lucky.html"><span class="tag gold">Culture</span><h3 class="mt-1">Why 8 is lucky, and what it's worth</h3><p>HK$16.5M for a plate, ¥2.33M for a phone number and an Olympics that opened at 8:08:08 pm.</p></a>
    <a class="card link" href="meaning-of-01810.html"><span class="tag red">Deep dive</span><h3 class="mt-1">The meaning of 01810</h3><p>The number as a stock code, as a sound-alike phrase and as a year in Qing history.</p></a>
  </div>
</div></section>

<section class="block"><div class="container">
  <div class="section-head"><div><span class="tag red">Watch</span><h2 class="mt-1">Videos worth your time</h2></div><a href="videos.html">All videos →</a></div>
  <div class="grid-3" data-videos="all" data-limit="3"></div>
  <p class="center mt-2"><a class="btn btn-primary" data-yt-channel href="#" target="_blank" rel="noopener">▶ Subscribe on YouTube</a></p>
</div></section>

<section class="block alt"><div class="container grid-2" style="align-items:center">
  <div class="card" style="background:var(--ink);color:#fff;border:0">
    <span class="tag gold">Monthly contest</span>
    <h2 class="mt-1">Pick-3 HK Stock Challenge</h2>
    <p style="color:#c9d0e2">Pick three Hong Kong stocks. The best 30-day return wins the top prize. It's free to enter, and you earn bonus entries for referrals.</p>
    <div class="countdown" data-countdown><div><b>00</b><small>days</small></div><div><b>00</b><small>hrs</small></div><div><b>00</b><small>min</small></div><div><b>00</b><small>sec</small></div></div>
    <a class="btn btn-gold mt-2" href="contests.html">Enter free →</a>
  </div>
  <div>
    <span class="tag red">Community-funded</span>
    <h2 class="mt-1">Send us a red packet 🧧</h2>
    <p class="muted">01810 is free and independent. Your support pays for servers, new tools, video production, contest prizes and new team members. Lucky amounts are $8, $18 and $88.</p>
    <div class="hero-actions"><a class="btn btn-primary" href="support.html">Support 01810</a><a class="btn btn-ghost" href="advertise.html">Sponsor a section</a></div>
  </div>
</div></section>

<section class="block"><div class="container">{cta_band()}</div></section>

<section class="block alt"><div class="container">
  <h2>Frequently asked</h2>
  <details><summary>What is 01810?</summary><p>01810 is an independent, free website combining Hong Kong &amp; China market tools and education with Chinese lucky-number culture. The name is a number. We are not affiliated with any listed company or exchange.</p></details>
  <details><summary>Is the market data real-time?</summary><p>Charts and quotes come from free TradingView widgets and may be delayed. Always confirm with your broker or HKEX before trading.</p></details>
  <details><summary>Is the Number Decoder scientific?</summary><p>No. It is a cultural and entertainment tool based on traditional Chinese homophones (for example, 8 sounds like “prosper”). It's fun and useful for choosing phone numbers or dates, but it is not a prediction.</p></details>
  <details><summary>How do you make money?</summary><p>Through advertising, sponsorships, partner referrals and reader support. Our editorial content and tools stay free. Sponsored content is always labelled.</p></details>
</div></section>
<script>
document.addEventListener("DOMContentLoaded",function(){{
  var codes={LUCKY_CODES!r}.map(function(c){{return {{c:c,r:Decoder.decode(c)}}}}).sort(function(a,b){{return b.r.score-a.r.score}}).slice(0,8);
  document.getElementById("luckyBoard").insertAdjacentHTML("beforeend",codes.map(function(x){{return "<tr><td><b>"+x.c+"</b></td><td><span class='tag "+(x.r.score>=70?"gold":"")+"'>"+x.r.score+"</span></td><td class='small'><a href='decoder.html?n="+x.c+"'>Decode</a> · <a href='markets.html?s="+x.c+"'>Chart</a></td></tr>"}}).join(""));
}});
</script>'''

page("index", "01810 — Hong Kong & China Markets, Lucky Numbers & Free Tools",
     "Free Hong Kong & China market tools, HK stock code lookup, calculators and a Chinese lucky Number Decoder, zodiac and feng shui. Where markets meet the meaning of numbers.",
     home, scripts=("tools.js",),
     schema=[{"@context": "https://schema.org", "@type": "Organization", "name": "01810", "url": SITE, "logo": SITE + "/assets/img/logo.svg"},
             {"@context": "https://schema.org", "@type": "WebSite", "name": "01810 — Markets & Fortune", "url": SITE,
              "potentialAction": {"@type": "SearchAction", "target": SITE + "/decoder.html?n={search_term_string}", "query-input": "required name=search_term_string"}}])

# ======================= MARKETS =======================
markets = page_hero("Markets", "Hong Kong &amp; China Markets", "Look up any HK stock code, track your watchlist and follow indices, hot lists, news and the economic calendar in one place.") + f'''
<div class="container">{ad("leader")}</div>
<section class="block" style="padding-top:20px"><div class="container layout">
  <div>
    <div class="card">
      <form id="symForm" class="tool-input"><input id="symInput" aria-label="HK stock code" placeholder="Enter HK code, e.g. 00700" inputmode="numeric" maxlength="5"><button class="btn btn-jade" type="submit">Load chart</button><button class="btn btn-ghost" type="button" id="wlAdd">＋ Watchlist</button></form>
      <div class="chips mt-1"><span class="small muted">Popular:</span><button class="chip" data-sym="00700">00700</button><button class="chip" data-sym="09988">09988</button><button class="chip" data-sym="01810">01810</button><button class="chip" data-sym="03690">03690</button><button class="chip" data-sym="01211">01211</button><button class="chip" data-sym="00005">00005</button><button class="chip" data-sym="00388">00388</button><button class="chip" data-sym="02800">02800</button></div>
    </div>
    <div class="section-head mt-2"><h2 id="symTitle" style="margin:0">HK 01810</h2><div class="small" id="symLinks"></div></div>
    <div class="tv-box" style="height:520px"><div id="tvChart" style="height:100%"></div></div>
    <div class="tv-box short mt-1" style="min-height:0"><div id="tvProfile"></div></div>
    <div class="card mt-2" id="watchlist-card"><h3 id="watchlist-h">⭐ Your watchlist</h3><p class="small muted">Saved in this browser only. No account needed.</p><div class="chips" id="watchlist"></div></div>
    {ad("inart")}
    <h2 class="mt-2">Market overview</h2>
    <div class="grid-2"><div class="tv-box"><div id="tvOverview"></div></div><div class="tv-box"><div id="tvHot"></div></div></div>
    <div class="grid-2 mt-2"><div><h3>Top stories</h3><div class="tv-box"><div id="tvNews"></div></div></div><div><h3>Economic calendar (HK · CN · US)</h3><div class="tv-box"><div id="tvCal"></div></div></div></div>
    <div class="card mt-2">
      <h3>Trading Hong Kong: the essentials</h3>
      <div class="table-wrap"><table>
        <tr><th>Item</th><th>Detail</th></tr>
        <tr><td>Trading hours (HKT)</td><td>Pre-open 09:00–09:30 · Morning 09:30–12:00 · Afternoon 13:00–16:00 · Closing auction to ~16:10</td></tr>
        <tr><td>Settlement</td><td>T+2</td></tr>
        <tr><td>Stamp duty</td><td>0.1% of trade value, charged to both buyer and seller</td></tr>
        <tr><td>Levies &amp; fees</td><td>SFC levy 0.0027% · AFRC levy 0.00015% · HKEX trading fee 0.00565%</td></tr>
        <tr><td>Board lots</td><td>Each stock trades in its own lot size (e.g. 100, 200, 500, 1,000 shares). Odd lots trade separately.</td></tr>
        <tr><td>Currency</td><td>Mostly HKD. Some stocks have RMB counters (code 8xxxx) under the dual-counter model</td></tr>
        <tr><td>Access for mainland investors</td><td>Southbound Stock Connect for eligible stocks</td></tr>
      </table></div>
      <p class="form-note mt-1">Figures reflect published HK rates at time of writing. Confirm with your broker. <a href="hk-stock-codes-explained.html">Learn how HK codes work →</a></p>
    </div>
    <div class="mt-2">{cta_band("Not sure where to start with HK stocks?", "Answer 4 quick questions and get a starter plan plus broker checklist.")}</div>
  </div>
  {sidebar()}
</div></section>
<div class="container"><p class="notice">📊 Market data is provided by free TradingView widgets and may be delayed. 01810 does not provide investment advice. Do your own research.</p></div>'''

page("markets", "HK Stock Code Lookup, Charts & Watchlist — Hong Kong & China Markets",
     "Look up any Hong Kong stock code with live charts, a free watchlist, Hang Seng and HS TECH indices, hot lists, market news and an HK/China economic calendar.",
     markets, scripts=("tools.js",), active="markets")

# ======================= TOOLS =======================
tools = page_hero("Tools", "Free Investor Calculators", "Work out the real cost of a Hong Kong trade, see compound growth, model dividend income and size positions by board lot. Everything runs in your browser.") + f'''
<div class="container">{ad("leader")}</div>
<section class="block" style="padding-top:20px"><div class="container layout"><div>
  <div class="chips"><a class="chip" href="#cost">HK trading cost</a><a class="chip" href="#growth">Compound growth</a><a class="chip" href="#dividend">Dividend / DRIP</a><a class="chip" href="#position">Position size</a><a class="chip" href="decoder.html">Number Decoder</a><a class="chip" href="zodiac.html#kua">Kua number</a></div>

  <div class="tool mt-2" id="cost"><span class="tag">Hong Kong</span><h2 class="mt-1">HK Trading Cost Calculator</h2><p class="muted">See every fee on a Hong Kong stock trade: stamp duty, levies, exchange fee, settlement and broker commission.</p>
    <form id="costForm" class="form"><div class="row"><div><label for="cPrice">Share price (HK$)</label><input id="cPrice" type="number" step="0.001" value="28.50" min="0"></div><div><label for="cQty">Quantity (shares)</label><input id="cQty" type="number" value="1000" min="0"></div></div>
    <div class="row"><div><label for="cComm">Broker commission (%)</label><input id="cComm" type="number" step="0.001" value="0.03" min="0"></div><div><label for="cMin">Minimum commission (HK$)</label><input id="cMin" type="number" value="3" min="0"></div></div>
    <div><label for="cSide">Side</label><select id="cSide"><option>buy</option><option>sell</option></select></div><button class="btn btn-jade" type="submit">Calculate</button></form>
    <div class="result" id="costResult"></div>
  </div>
  {ad("rect")}

  <div class="tool mt-2" id="growth"><span class="tag">Any market</span><h2 class="mt-1">Compound Growth Calculator</h2>
    <form id="growthForm" class="form"><div class="row"><div><label for="gP">Starting amount ($)</label><input id="gP" type="number" value="8888"></div><div><label for="gM">Monthly contribution ($)</label><input id="gM" type="number" value="500"></div></div>
    <div class="row"><div><label for="gR">Expected annual return (%)</label><input id="gR" type="number" step="0.1" value="7"></div><div><label for="gY">Years</label><input id="gY" type="number" value="18" min="1" max="60"></div></div><button class="btn btn-jade" type="submit">Calculate</button></form>
    <div class="result" id="growthResult"></div>
  </div>

  <div class="tool mt-2" id="dividend"><span class="tag">Income</span><h2 class="mt-1">Dividend &amp; DRIP Calculator</h2>
    <form id="divForm" class="form"><div class="row"><div><label for="dInv">Investment ($)</label><input id="dInv" type="number" value="50000"></div><div><label for="dY">Dividend yield (%)</label><input id="dY" type="number" step="0.1" value="5.5"></div></div>
    <div class="row"><div><label for="dG">Dividend growth / yr (%)</label><input id="dG" type="number" step="0.1" value="3"></div><div><label for="dYrs">Years</label><input id="dYrs" type="number" value="10"></div></div>
    <div><label for="dTax">Withholding tax (%)</label><input id="dTax" type="number" value="0" step="1"></div><button class="btn btn-jade" type="submit">Calculate</button></form>
    <div class="result" id="divResult"></div>
  </div>
  {ad("inart")}

  <div class="tool mt-2" id="position"><span class="tag">Risk</span><h2 class="mt-1">Position Size by Board Lot</h2><p class="muted">Size a position from your risk budget, rounded down to whole HK board lots, with the HKD and USD value.</p>
    <form id="posForm" class="form"><div class="row"><div><label for="pAcct">Account size (HK$)</label><input id="pAcct" type="number" value="200000"></div><div><label for="pRisk">Risk per trade (%)</label><input id="pRisk" type="number" step="0.1" value="1"></div></div>
    <div class="row"><div><label for="pEntry">Entry price (HK$)</label><input id="pEntry" type="number" step="0.001" value="28.5"></div><div><label for="pStop">Stop price (HK$)</label><input id="pStop" type="number" step="0.001" value="26.8"></div></div>
    <div class="row"><div><label for="pLot">Board lot (shares)</label><input id="pLot" type="number" value="200"></div><div><label for="pFx">USD/HKD rate</label><input id="pFx" type="number" step="0.0001" value="7.80"></div></div><button class="btn btn-jade" type="submit">Calculate</button></form>
    <div class="result" id="posResult"></div>
  </div>
  <div class="mt-3">{lead_box("Want these numbers applied to <em>your</em> goals?", "Get a free personalised starter plan: your goal, your timeline, the fees to watch and a broker checklist. It takes 60 seconds.", "tools")}</div>
  <p class="form-note mt-2">Calculators are for education only and use simplified assumptions. Fee rates reflect published HK rates at time of writing and can change.</p>
</div>{sidebar()}</div></section>'''

page("tools", "Free HK Stamp Duty, Compound Growth, Dividend & Position Size Calculators",
     "Free Hong Kong trading cost calculator (stamp duty, SFC levy, HKEX fees), compound growth, dividend DRIP and board-lot position size calculators.",
     tools, scripts=("tools.js",), active="tools",
     schema={"@context": "https://schema.org", "@type": "WebApplication", "name": "01810 Investor Calculators", "applicationCategory": "FinanceApplication", "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}})

# ======================= VIDEOS =======================
videos = page_hero("Videos", "Videos: Markets, Numbers &amp; Feng Shui", "Hand-picked explainers on the Hang Seng, Chinese lucky numbers, the zodiac and feng shui. Our own channel is on the way, so subscribe to be first.") + f'''
<div class="container">{ad("leader")}</div>
<section class="block" style="padding-top:20px"><div class="container">
  <div class="section-head"><h2>📈 Markets &amp; investing</h2></div><div class="grid-3" data-videos="markets"></div>
  {ad("inart")}
  <div class="section-head mt-3"><h2>✦ Lucky numbers</h2></div><div class="grid-3" data-videos="numbers"></div>
  <div class="section-head mt-3"><h2>🐉 Zodiac &amp; feng shui</h2></div><div class="grid-3" data-videos="fengshui"></div>
  <div class="card mt-3 center"><h2>Create with us 🎬</h2><p class="muted">Are you a finance or culture creator? We feature partner videos, co-produce explainers and pay for great work.</p><div class="hero-actions" style="justify-content:center"><a class="btn btn-primary" data-yt-channel href="#" target="_blank" rel="noopener">▶ Subscribe</a><a class="btn btn-ghost" href="careers.html">Apply as a creator</a><a class="btn btn-ghost" href="advertise.html">Sponsor a video</a></div></div>
  <p class="form-note mt-2">Videos are embedded from YouTube in privacy-enhanced mode and belong to their creators. Their inclusion does not imply endorsement either way.</p>
</div></section>'''
page("videos", "Videos — Hang Seng Explained, Chinese Lucky Numbers & Feng Shui",
     "Watch curated videos explaining the Hang Seng Index, Hong Kong investing, Chinese lucky numbers, the zodiac and Kua numbers.", videos, active="videos")

# ======================= GET STARTED (LEAD GEN) =======================
gs = page_hero("Get Started", "Your free Hong Kong &amp; China investor plan", "Answer 4 quick questions and get a personalised starter plan, a broker checklist and our 2027 guide. It takes about 60 seconds.",
               '<div class="trust" style="color:#c9d0e2"><span>✓ 100% free</span><span>✓ No obligation</span><span>✓ Your data is never sold</span><span>✓ Unsubscribe anytime</span></div>') + f'''
<section class="block"><div class="container">
<div class="quiz tool" id="quiz">
  <div class="progress"><span id="qBar"></span></div>
  <div class="small muted" id="qStepLabel">Step 1 of 5</div>
  <div class="step active" data-step="1"><h2>What's your main goal?</h2>
    <div class="options" data-group="goal">
      <button type="button" class="option" data-value="Long-term wealth"><b>🌱 Grow long-term wealth</b><small>Retirement, family, compounding</small></button>
      <button type="button" class="option" data-value="Dividend income"><b>💰 Dividend income</b><small>Cash flow from HK blue chips</small></button>
      <button type="button" class="option" data-value="China tech growth"><b>🚀 China tech growth</b><small>HS TECH, EVs, AI, platforms</small></button>
      <button type="button" class="option" data-value="Active trading"><b>⚡ Active trading</b><small>Short-term moves, IPOs</small></button>
    </div></div>
  <div class="step" data-step="2"><h2>How experienced are you?</h2>
    <div class="options" data-group="experience">
      <button type="button" class="option" data-value="Beginner"><b>Beginner</b><small>Never bought a stock</small></button>
      <button type="button" class="option" data-value="Some experience"><b>Some experience</b><small>A few trades or funds</small></button>
      <button type="button" class="option" data-value="Experienced"><b>Experienced</b><small>Active in US/other markets</small></button>
      <button type="button" class="option" data-value="Professional"><b>Professional</b><small>Advisor, trader, analyst</small></button>
    </div></div>
  <div class="step" data-step="3"><h2>Roughly how much would you start with?</h2>
    <div class="options" data-group="capital">
      <button type="button" class="option" data-value="Under $1,000"><b>Under $1,000</b></button>
      <button type="button" class="option" data-value="$1,000–$10,000"><b>$1,000 – $10,000</b></button>
      <button type="button" class="option" data-value="$10,000–$100,000"><b>$10,000 – $100,000</b></button>
      <button type="button" class="option" data-value="$100,000+"><b>$100,000+</b></button>
    </div></div>
  <div class="step" data-step="4"><h2>Which markets interest you?</h2>
    <div class="options" data-group="markets">
      <button type="button" class="option" data-value="Hong Kong stocks"><b>🇭🇰 Hong Kong stocks</b></button>
      <button type="button" class="option" data-value="Mainland China A-shares"><b>🇨🇳 Mainland A-shares</b></button>
      <button type="button" class="option" data-value="China ADRs in the US"><b>🇺🇸 China ADRs (US-listed)</b></button>
      <button type="button" class="option" data-value="All of the above"><b>🌏 All of the above</b></button>
    </div></div>
  <div class="step" data-step="5"><h2>Where should we send your plan?</h2>
    <form class="form" id="quizForm" data-form="Investor profile lead (Get Started)" data-custom data-success="🎉 Your plan is ready below, and a copy is on its way to your inbox.">
      <div class="row"><div><label for="qName">Full name</label><input id="qName" name="name" required autocomplete="name"></div><div><label for="qEmail">Email</label><input id="qEmail" type="email" name="email" required autocomplete="email"></div></div>
      <div class="row"><div><label for="qCountry">Country</label><select id="qCountry" name="country" required><option value="">Select…</option><option>Hong Kong</option><option>Mainland China</option><option>Singapore</option><option>Malaysia</option><option>Taiwan</option><option>United States</option><option>Canada</option><option>United Kingdom</option><option>Australia</option><option>India</option><option>Other</option></select></div>
      <div><label for="qPhone">Phone / WhatsApp <span class="muted">(optional)</span></label><input id="qPhone" name="phone" type="tel" autocomplete="tel"></div></div>
      <div><label for="qWhen">When do you plan to start?</label><select id="qWhen" name="timeline"><option>This month</option><option>In 1–3 months</option><option>Just researching</option></select></div>
      <label class="check"><input type="checkbox" name="partner_offers" value="yes"> Send me vetted partner offers (e.g. broker sign-up bonuses)</label>
      <label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to the <a href="privacy.html">Privacy Policy</a> and to be contacted about my plan.</label>
      {hp()}
      <button class="btn btn-primary btn-block" type="submit">Get my free plan →</button>{status()}
      <p class="form-note">🔒 Encrypted submission. We never sell your data. Not financial advice.</p>
    </form></div>
  <div class="hero-actions" id="qNav"><button class="btn btn-ghost" type="button" id="qBack" style="visibility:hidden">← Back</button></div>
  <div class="result" id="planResult"></div>
</div>
</div></section>

<section class="block alt"><div class="container grid-3">
  <div class="card"><div class="ico">🧭</div><h3>Personal starter plan</h3><p>A step-by-step path matched to your goal, experience and budget.</p></div>
  <div class="card"><div class="ico">✅</div><h3>Broker checklist</h3><p>What to compare: HK access, fees, minimums, FX spreads, regulation and Stock Connect.</p></div>
  <div class="card"><div class="ico">📘</div><h3>2027 Wealth &amp; Luck Guide</h3><p>Our annual guide to markets and lucky numbers, free with your plan.</p></div>
</div></section>

<section class="block" id="reading"><div class="container grid-2" style="align-items:start">
  <div><span class="tag gold">Personal service</span><h2 class="mt-1">Request a personal Number &amp; Fortune reading</h2>
    <p class="muted">Choosing a business phone number, a plate, an opening date or a wedding date? Our team will prepare a personal reading with number analysis, zodiac compatibility and auspicious dates.</p>
    <ul class="list-check"><li>Business names, phone numbers &amp; plates</li><li>Auspicious dates for openings, moves &amp; weddings</li><li>Zodiac &amp; Kua compatibility for partners or teams</li><li>Delivered by email as a PDF</li></ul>
    <p class="small muted">Readings are cultural guidance for entertainment and are not professional advice.</p></div>
  <div class="card"><form class="form" data-form="Personal reading request" data-success="Request received. We'll email you within 2 business days with next steps.">
    <div class="row"><div><label for="rName">Name</label><input id="rName" name="name" required></div><div><label for="rEmail">Email</label><input id="rEmail" type="email" name="email" required></div></div>
    <div class="row"><div><label for="rDob">Birth date</label><input id="rDob" type="date" name="birth_date"></div><div><label for="rTime">Birth time <span class="muted">(optional)</span></label><input id="rTime" type="time" name="birth_time"></div></div>
    <div><label for="rType">Reading type</label><select id="rType" name="reading_type"><option>Number / phone / plate analysis</option><option>Business name &amp; opening date</option><option>Wedding / move date</option><option>Full personal reading</option></select></div>
    <div><label for="rQ">Your question</label><textarea id="rQ" name="question" placeholder="Tell us the numbers, dates or decision you're weighing…"></textarea></div>
    {hp()}<button class="btn btn-gold btn-block" type="submit">Request my reading</button>{status()}
  </form></div>
</div></section>
<script>
document.addEventListener("DOMContentLoaded",function(){{
  var step=1,ans={{}},total=5,$=Site.$,$$=Site.$$;
  function show(n){{step=n;$$("#quiz .step").forEach(function(s){{s.classList.toggle("active",+s.dataset.step===n)}});$("#qBar").style.width=(n/total*100)+"%";$("#qStepLabel").textContent="Step "+n+" of "+total;$("#qBack").style.visibility=n>1?"visible":"hidden";}}
  $$("#quiz [data-group]").forEach(function(g){{g.addEventListener("pick",function(e){{ans[g.dataset.group]=e.detail;setTimeout(function(){{show(step+1)}},220);}});}});
  $("#qBack").addEventListener("click",function(){{if(step>1)show(step-1)}});
  var f=$("#quizForm");f._extra=function(){{return {{goal:ans.goal||"",experience:ans.experience||"",capital:ans.capital||"",markets:ans.markets||""}}}};
  f.addEventListener("submit",function(e){{e.preventDefault();Site.submitForm(f);}});
  document.addEventListener("lead:success",function(ev){{
    if(ev.detail.form.indexOf("Investor profile")<0)return;
    var g=ans.goal||"Long-term wealth",x=ans.experience||"Beginner";
    var plans={{"Long-term wealth":["Start with a low-cost Hang Seng or broad-China index ETF","Automate a monthly contribution (see our compound calculator)","Add 2–3 quality blue chips once you understand board lots and fees"],
      "Dividend income":["Screen HK blue chips for dividend history and payout ratio","Check withholding tax for H-shares vs local companies","Use our DRIP calculator to model reinvestment"],
      "China tech growth":["Learn the HS TECH index and its top constituents","Size positions by board lot with a strict risk budget","Follow earnings dates on our Markets calendar"],
      "Active trading":["Master HK trading hours, auctions and T+2 settlement","Calculate real round-trip costs (stamp duty applies both ways)","Use position sizing and stop levels on every trade"]}};
    $("#qNav").style.display="none";
    $("#planResult").innerHTML="<h2>Your starter plan: "+g+"</h2><p class='muted'>Level: "+x+" · Budget: "+(ans.capital||"—")+" · Markets: "+(ans.markets||"—")+"</p><ol>"+plans[g].map(function(s){{return "<li>"+s+"</li>"}}).join("")+"</ol>"+
      "<h3>Broker checklist</h3><div class='table-wrap'><table><tr><th>Check</th><th>Why it matters</th></tr><tr><td>HKEX market access</td><td>Direct HK trading and not only US ADRs</td></tr><tr><td>Commission &amp; platform fees</td><td>Small trades are hit hard by minimum fees</td></tr><tr><td>FX conversion spread</td><td>HKD/USD conversion can cost more than commission</td></tr><tr><td>Regulation</td><td>SFC (HK), SEC/FINRA (US), MAS (SG) and similar regulators</td></tr><tr><td>Odd-lot &amp; IPO support</td><td>Needed for small budgets and new listings</td></tr></table></div>"+
      "<div class='hero-actions'><a class='btn btn-jade' href='tools.html#cost'>Calculate your trade costs</a><a class='btn btn-ghost' href='markets.html'>Build your watchlist</a></div>";
    $("#planResult").classList.add("show");
  }});
  show(1);
}});
</script>'''
page("get-started", "Free Hong Kong & China Investor Plan — Get Started",
     "Take the 60-second investor profile and get a free personalised Hong Kong & China starter plan, broker checklist and 2027 Wealth & Luck Guide.", gs, active="")
