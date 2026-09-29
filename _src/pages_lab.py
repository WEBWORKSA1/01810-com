from build import page, ad, newsletter_inline, lead_box, sidebar, cta_band, page_hero, hp, status, SITE

def report_form(src):
    return f'''<div class="card mt-2" id="report"><span class="tag red">Free PDF</span><h3 class="mt-1">Email me the full report</h3>
<p class="small">Get the full reading: best and worst combinations, suggested alternatives, and matching lucky dates for your zodiac sign.</p>
<form class="form" data-form="Full report request ({src})" data-success="Your full report request is in. Check your inbox shortly.">
<div class="row"><div><label for="rpName-{src}">First name</label><input id="rpName-{src}" name="name" required></div><div><label for="rpEmail-{src}">Email</label><input id="rpEmail-{src}" type="email" name="email" required></div></div>
<div class="row"><div><label for="reportNumber">Number to analyse</label><input id="reportNumber" name="number" inputmode="numeric"></div><div><label for="rpUse-{src}">What is it for?</label><select id="rpUse-{src}" name="use"><option>Phone number</option><option>Car plate</option><option>Address / unit</option><option>Business / price</option><option>Stock code</option><option>Other</option></select></div></div>
<label class="check"><input type="checkbox" name="consent" value="yes" required> Send me the report and the weekly brief. I accept the <a href="privacy.html">Privacy Policy</a>.</label>
{hp()}<button class="btn btn-primary" type="submit">Send my report →</button>{status()}</form></div>'''

# ======================= DECODER =======================
dec = page_hero("Number Lab / Decoder", "Chinese Lucky Number Decoder", "Enter any phone number, licence plate, address, price or stock code. Get a luck score, the hidden phrases inside it and a digit-by-digit reading based on traditional Chinese homophones.") + f'''
<div class="container">{ad("leader")}</div>
<section class="block" style="padding-top:20px"><div class="container layout"><div>
  <div class="tool">
    <form id="decoderForm" class="tool-input"><input id="decoderInput" aria-label="Number to decode" placeholder="e.g. 01810" inputmode="numeric" maxlength="20"><button class="btn btn-gold" type="submit">Decode ✦</button></form>
    <div class="chips mt-1"><span class="small muted">Try:</span><button class="chip" data-try="01810">01810</button><button class="chip" data-try="888">888</button><button class="chip" data-try="1688">1688</button><button class="chip" data-try="5201314">5201314</button><button class="chip" data-try="518">518</button><button class="chip" data-try="4444">4444</button><button class="chip" data-try="88888888">88888888</button></div>
    <div class="result" id="decoderResult"></div>
  </div>
  {ad("rect")}
  {report_form("decoder")}
  <div class="article mt-2">
    <h2 class="mt-0">How the Decoder works</h2>
    <p>Chinese has many homophones, words that sound alike. Numbers pick up the meaning of the words they sound like. <b>8 (bā)</b> sounds like <b>發 (fā)</b>, “to prosper”. <b>4 (sì)</b> sounds like <b>死 (sǐ)</b>, “death”. In phone and room numbers, <b>1</b> is often read <b>yāo</b>, which sounds close to <b>要</b>, “will / want”. That is why 518 reads as 我要发, “I will prosper”.</p>
    <p>Our score starts at a neutral 50. Each digit adds or subtracts points: 8, 6 and 9 add the most and 4 subtracts the most. We then add bonuses for known lucky phrases (168, 518, 888, 1314…) and penalties for unlucky ones (14, 74, 250), and scale the result to 1–99.</p>
    <h3>Digit cheat-sheet</h3>
    <div class="table-wrap"><table><tr><th>Digit</th><th>Chinese</th><th>Sounds like</th><th>Feel</th></tr>
    <tr><td>0</td><td class="zh">零</td><td>你 “you” (slang) · 良 “good”</td><td class="pos">Positive</td></tr>
    <tr><td>1</td><td class="zh">一 / 幺</td><td>要 “will”</td><td class="pos">Positive</td></tr>
    <tr><td>2</td><td class="zh">二</td><td>“good things come in pairs”</td><td class="pos">Positive</td></tr>
    <tr><td>3</td><td class="zh">三</td><td>生 “life / birth”</td><td class="pos">Positive</td></tr>
    <tr><td>4</td><td class="zh">四</td><td>死 “death”</td><td class="neg">Avoided</td></tr>
    <tr><td>5</td><td class="zh">五</td><td>五行 five elements · 无 “none”</td><td>Neutral</td></tr>
    <tr><td>6</td><td class="zh">六</td><td>流 “flow / smooth”</td><td class="pos">Very lucky</td></tr>
    <tr><td>7</td><td class="zh">七</td><td>起 “rise” · 气 “anger”</td><td>Mixed</td></tr>
    <tr><td>8</td><td class="zh">八</td><td>發 “prosper”</td><td class="pos">Luckiest</td></tr>
    <tr><td>9</td><td class="zh">九</td><td>久 “long-lasting”</td><td class="pos">Very lucky</td></tr></table></div>
    <p class="small muted mt-1">Cultural and entertainment tool. Regional readings vary between Mandarin and Cantonese.</p>
  </div>
</div>{sidebar()}</div></section>'''
page("decoder", "Chinese Lucky Number Decoder — Luck Score for Any Number",
     "Free Chinese lucky number calculator. Decode any phone number, licence plate, address or stock code: luck score, hidden phrases like 168 and 518, and digit meanings.",
     dec, scripts=("tools.js",), active="lab",
     schema={"@context": "https://schema.org", "@type": "WebApplication", "name": "Chinese Lucky Number Decoder", "applicationCategory": "LifestyleApplication", "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}})

# ======================= ZODIAC + KUA =======================
zod = page_hero("Number Lab / Zodiac", "Chinese Zodiac, Compatibility &amp; Kua Number", "Find your true zodiac sign and element using the lunar calendar (with the correct New Year boundary), check compatibility with anyone, and calculate your feng shui Kua directions.") + f'''
<div class="container">{ad("leader")}</div>
<section class="block" style="padding-top:20px"><div class="container layout"><div>
  <div class="tool"><span class="tag gold">Lunar-calendar accurate</span><h2 class="mt-1">What's my Chinese zodiac sign?</h2>
    <form id="zodiacForm" class="tool-input"><input id="zDob" type="date" required aria-label="Your birth date" value="1990-08-08" style="font-size:1rem;letter-spacing:0"><button class="btn btn-gold" type="submit">Find my sign</button></form>
    <div class="result" id="zodiacResult"></div></div>
  <div class="tool mt-2" id="compat"><h2>Zodiac compatibility</h2>
    <form id="compatForm" class="form"><div class="row"><div><label for="cA">Your sign</label><select id="cA"></select></div><div><label for="cB">Their sign</label><select id="cB"></select></div></div><button class="btn btn-primary" type="submit">Check compatibility</button></form>
    <div class="result" id="compatResult"></div></div>
  {ad("rect")}
  <div class="tool mt-2" id="kua"><span class="tag">Feng shui</span><h2 class="mt-1">Kua number calculator</h2><p class="muted">Your Kua (Gua) number places you in the East or West group and gives you four favourable directions.</p>
    <form id="kuaForm" class="form"><div class="row"><div><label for="kDob">Birth date</label><input id="kDob" type="date" required value="1988-08-08"></div><div><label for="kGender">Gender (traditional formula)</label><select id="kGender"><option value="m">Male</option><option value="f">Female</option></select></div></div><button class="btn btn-jade" type="submit">Calculate Kua</button></form>
    <div class="result" id="kuaResult"></div></div>
  <h2 class="mt-3">The 12 animals</h2><div class="grid-3" id="animalGrid"></div>
  <div class="article mt-2"><h2 class="mt-0">2026 Fire Horse → 2027 Fire Goat</h2>
    <p>The Year of the <b>Fire Horse</b> began on 17 February 2026 and runs to 5 February 2027. The <b>Fire Goat</b> year begins on <b>6 February 2027</b>. The Chinese year starts at Lunar New Year, not on 1 January. That is why many “zodiac by year” charts get January and early-February birthdays wrong. Our finder uses the actual lunar calendar built into your browser.</p>
    <p>Want the full outlook for your sign? Our free <b>2027 Wealth &amp; Luck Guide</b> covers lucky numbers, colours, directions and key dates for all 12 signs.</p></div>
  <div class="mt-2">{lead_box(src="zodiac")}</div>
</div>{sidebar()}</div></section>'''
page("zodiac", "Chinese Zodiac Calculator, Compatibility & Kua Number (Lunar-Accurate)",
     "Find your Chinese zodiac animal and element with the correct Lunar New Year boundary, check zodiac compatibility and calculate your feng shui Kua number and lucky directions.",
     zod, scripts=("tools.js",), active="lab")

# ======================= LEARN HUB =======================
GLOSS = [
 ("A/H premium", "The price gap between a company's mainland A-shares and its Hong Kong H-shares. It is tracked by the Hang Seng Stock Connect China AH Premium Index."),
 ("Board lot", "The standard trading unit for a HK stock (e.g. 100 or 500 shares). Each stock sets its own. Smaller quantities are odd lots."),
 ("CBBC", "Callable Bull/Bear Contract, a leveraged structured product with a mandatory call level. HK codes fall in the 49500–69999 range."),
 ("Derivative warrant", "A leveraged product issued by a third party on a stock or index. HK codes are 10000–29999."),
 ("Dual counter", "A stock that trades in both HKD and RMB. The RMB counter code is usually 8 + the HKD code (e.g. 81810)."),
 ("GEM", "HKEX's growth-company board. Codes are 08001–08999."),
 ("H-share", "A mainland-incorporated company listed in Hong Kong."),
 ("Hang Seng Index (HSI)", "The benchmark index of the largest, most liquid Hong Kong-listed companies."),
 ("Hang Seng TECH Index", "Tracks the 30 largest tech-themed companies listed in Hong Kong."),
 ("Red chip / P chip", "Red chips are overseas-incorporated companies controlled by mainland state entities. P chips are overseas-incorporated companies controlled by mainland private individuals."),
 ("Southbound Stock Connect", "The channel that lets eligible mainland investors buy selected HK-listed stocks."),
 ("Stamp duty", "A 0.1% tax on the value of HK stock trades, charged to both buyer and seller."),
 ("T+2", "Trades settle two business days after the trade date."),
 ("WVR (“-W”)", "Weighted voting rights. HK stock short names ending in “-W” have dual-class shares."),
 ("發 (fā)", "“Prosper”. Its sound-alike, 8, is the luckiest number in Chinese culture."),
 ("Kua number", "A feng shui number from birth year and gender that gives your four favourable directions."),
]
faq = [("How do I buy Hong Kong stocks from outside Hong Kong?", "Use an international broker that offers HKEX access. Compare commission, FX spreads and minimums first. Our Get Started plan includes a broker checklist."),
       ("Why are Hong Kong stock codes five digits?", "HKEX allocates numeric codes in ranges by product type. Ordinary shares use low ranges, and codes are written with leading zeros (00700, 01810)."),
       ("Why is 8 lucky in Chinese culture?", "8 (bā) sounds like 發 (fā), “to prosper”. Buyers have paid millions for numbers full of 8s, and the Beijing Olympics opened at 8:08:08 pm on 8/8/2008."),
       ("Is 01810.com affiliated with any listed company?", "No. 01810 is an independent publication. The name is a number and a domain.")]
glossary = "".join(f"<tr><td><b>{k}</b></td><td>{v}</td></tr>" for k, v in GLOSS)
faqs = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)
learn = page_hero("Learn", "Learning Hub", "Plain-English guides to Hong Kong &amp; China markets and to the number culture behind them.") + f'''
<div class="container">{ad("leader")}</div>
<section class="block" style="padding-top:20px"><div class="container layout"><div>
  <div class="grid-2">
    <a class="card link" href="hk-stock-codes-explained.html"><span class="tag">Markets · 7 min</span><h3 class="mt-1">How Hong Kong stock codes work</h3><p>The 5-digit system, code ranges by product, RMB counters and how to read a ticker instantly.</p></a>
    <a class="card link" href="why-8-is-lucky.html"><span class="tag gold">Culture · 6 min</span><h3 class="mt-1">Why 8 is lucky, and what it's worth</h3><p>Record plate and phone-number sales, the Olympics and how luck affects prices.</p></a>
    <a class="card link" href="meaning-of-01810.html"><span class="tag red">Deep dive · 6 min</span><h3 class="mt-1">The meaning of 01810</h3><p>A ticker, a sound-alike phrase and a year in Qing history.</p></a>
    <a class="card link" href="tools.html#cost"><span class="tag">Tool</span><h3 class="mt-1">What does a HK trade really cost?</h3><p>Stamp duty, levies and fees worked out for your own trade size.</p></a>
  </div>
  {ad("inart")}
  <h2 id="glossary" class="mt-2">Glossary</h2>
  <div class="table-wrap"><table><tr><th style="width:30%">Term</th><th>Meaning</th></tr>{glossary}</table></div>
  <h2 class="mt-3">FAQ</h2>{faqs}
  <div class="mt-2">{cta_band()}</div>
</div>{sidebar()}</div></section>'''
page("learn", "Learn Hong Kong & China Investing + Chinese Number Culture — Guides & Glossary",
     "Guides, glossary and FAQ on Hong Kong stock codes, the Hang Seng, Stock Connect, stamp duty, board lots and Chinese lucky numbers.",
     learn, active="learn",
     schema={"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]})

# ======================= ARTICLES =======================
def article(slug, title, desc, crumb, body, minutes):
    html = page_hero("Learn / " + crumb, title, desc) + f'''
<section class="block" style="padding-top:28px"><div class="container layout"><div>
<article class="article"><div class="meta">By the 01810 Editorial Team · {minutes} min read · Updated September 2026</div>
{body}
<hr style="border:0;border-top:1px solid var(--line);margin:28px 0">
<div class="hero-actions"><button class="btn btn-gold btn-sm" data-share data-text="{title}">Share this guide</button><a class="btn btn-ghost btn-sm" href="learn.html">More guides</a></div>
</article>
<div class="mt-2">{lead_box(src=slug)}</div>
</div>{sidebar()}</div></section>'''
    page(slug, title, desc, html, active="learn",
         schema={"@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc,
                 "author": {"@type": "Organization", "name": "01810 Editorial Team"}, "publisher": {"@type": "Organization", "name": "01810"},
                 "datePublished": "2026-09-29", "dateModified": "2026-09-29", "mainEntityOfPage": SITE + "/" + slug + ".html"})

article("hk-stock-codes-explained", "How Hong Kong Stock Codes Work (5-Digit HKEX Codes Explained)",
 "Why HK tickers are five digits, what the code ranges mean (shares, GEM, warrants, CBBCs, RMB counters) and how to read any code instantly.", "HK stock codes", f'''
<div class="toc"><b>In this guide</b><ol><li><a href="#why">Why five digits?</a></li><li><a href="#ranges">Code ranges by product</a></li><li><a href="#rmb">RMB counters: the “8” prefix</a></li><li><a href="#suffix">Short-name suffixes</a></li><li><a href="#read">Reading a code in 5 seconds</a></li></ol></div>
<h2 id="why">Why five digits?</h2>
<p>US tickers use letters (AAPL, TSLA). Hong Kong uses <b>numbers</b>. HKEX gives every listed security a code of up to five digits, and it is written with leading zeros: <b>00700</b>, <b>09988</b>, <b>01810</b>. Brokers and data sites often drop the zeros (700, 9988, 1810) or add a suffix such as <b>.HK</b>. It is the same security either way.</p>
<p>Numeric codes work across languages. A Cantonese speaker, a Mandarin speaker and an English speaker all read “1810” the same way. That is also why the culture of lucky numbers reaches the stock market. A company's code gets said aloud millions of times.</p>
{ad("inart")}
<h2 id="ranges">Code ranges by product</h2>
<p>HKEX publishes a <a href="https://www.hkex.com.hk/Products/Securities/Stock-Code-Allocation-Plan?sc_lang=en" target="_blank" rel="noopener">Stock Code Allocation Plan</a>. The main blocks are:</p>
<div class="table-wrap"><table><tr><th>Range</th><th>What lives there</th></tr>
<tr><td>00001 – 02799 (and other blocks)</td><td>Main Board ordinary shares</td></tr>
<tr><td>02800 – 03999 (selected)</td><td>ETFs and other exchange-traded products (e.g. 02800)</td></tr>
<tr><td>08001 – 08999</td><td>GEM (growth enterprise) shares</td></tr>
<tr><td>10000 – 29999</td><td>Derivative warrants</td></tr>
<tr><td>49500 – 69999</td><td>Callable Bull/Bear Contracts (CBBCs)</td></tr>
<tr><td>8xxxx</td><td>RMB counters of dual-counter stocks (8 + the HKD code)</td></tr></table></div>
<p class="small muted">Ranges are simplified. Always check HKEX's current allocation plan.</p>
<h2 id="rmb">RMB counters: the “8” prefix</h2>
<p>Under the HKD-RMB dual-counter model, some large companies trade in both currencies. The RMB counter usually takes the HKD code with an 8 in front. For example, the RMB counter linked to code 01810 is <b>81810</b>. The two counters are fungible: shares bought on one can be sold on the other.</p>
<h2 id="suffix">Short-name suffixes</h2>
<ul><li><b>-W</b>: weighted voting rights (dual-class shares).</li><li><b>-S</b>: a secondary listing.</li><li><b>-SW</b>: both.</li><li><b>-B</b>: a pre-revenue biotech listed under Chapter 18A.</li></ul>
<blockquote>Code 01810 made history in July 2018 as the first Hong Kong listing with a weighted-voting-rights structure, hence the “-W” in its short name.</blockquote>
<h2 id="read">Reading a code in 5 seconds</h2>
<ol><li>Five digits starting with <b>0</b> and under 03000? Usually an ordinary share.</li><li>Starting with <b>08</b>? GEM, so expect smaller and riskier companies.</li><li>Starting with <b>1</b> or <b>2</b>? Probably a warrant. Starting with <b>5</b> or <b>6</b>? Possibly a CBBC. These are leveraged products, so be careful.</li><li>Starting with <b>8</b> and five digits long? Likely an RMB counter.</li></ol>
<p>Try it now: open our <a href="markets.html">Markets page</a> and type any code. Or run it through the <a href="decoder.html">Number Decoder</a> to see how “lucky” it sounds.</p>''', 7)

article("why-8-is-lucky", "Why 8 Is Lucky in Chinese Culture — and What It's Worth",
 "8 sounds like 發, “prosper”. See the record prices paid for lucky plates and phone numbers, the 8/8/08 Olympics and how number luck affects prices.", "Why 8 is lucky", f'''
<h2>The sound of money</h2>
<p>In Mandarin, <b>8 (八, bā)</b> sounds close to <b>發 (fā)</b>, “to prosper” or “to get rich”. In Cantonese the match is even closer: <i>baat</i> and <i>faat</i>. Put two or three together and they become phrases. <b>88</b> reads as “double prosperity” and <b>888</b> as “prosperity, prosperity, prosperity”. Put a 1 (read <i>yāo</i>) in front and you get <b>18</b>, “will prosper”. Add a 6 (smooth flow) and you get <b>168</b>, “prosper all the way”.</p>
<h2>Real money behind lucky numbers</h2>
<div class="table-wrap"><table><tr><th>Item</th><th>Price</th><th>Year</th></tr>
<tr><td>Hong Kong licence plate “18”</td><td>HK$16.5 million</td><td>2008</td></tr>
<tr><td>Hong Kong licence plate “28”</td><td>HK$18.1 million</td><td>2016</td></tr>
<tr><td>Hong Kong licence plate “W”</td><td>HK$26 million</td><td>2021</td></tr>
<tr><td>Phone number 8888-8888 (Sichuan Airlines)</td><td>¥2.33 million (~US$280k)</td><td>2003</td></tr></table></div>
<p class="small muted">Sources: Kwiksure / Asia Times (HK plates), China Daily (phone number). A widely shared ¥120M sale of “1888888888” was an April Fools' hoax.</p>
{ad("inart")}
<h2>8:08:08 on 8/8/08</h2>
<p>The clearest proof of the number's power came on the world stage. The Beijing Summer Olympics opening ceremony began at <b>8:08:08 pm on 8 August 2008</b>. Wedding bookings, product launches and business openings often cluster on dates full of 8s.</p>
<h2>The unlucky flip side: 4</h2>
<p><b>4 (四, sì)</b> sounds like <b>死 (sǐ)</b>, “death”. Many buildings in Hong Kong, mainland China and Chinese communities abroad skip the 4th, 14th and 24th floors. Numbers full of 4s sell at a discount. <b>14</b> (“want to die”) and <b>74</b> (“furious”) are especially avoided.</p>
<h2>Does number luck move stock prices?</h2>
<p>There is plenty of anecdotal evidence and some academic interest. Researchers have studied whether IPO pricing clusters around 8s and whether lucky codes trade at a premium. The effect, where it appears, is small next to fundamentals. Our view: <b>enjoy the culture, but invest on the numbers that matter</b>, which are earnings, cash flow, valuation and risk. Our <a href="tools.html">calculators</a> help with those. Our <a href="decoder.html">Decoder</a> handles the fun part.</p>
<h2>Using 8 in daily life</h2>
<ul><li>Gift money in amounts such as 88, 168 or 888 (and never 4 or 250).</li><li>Choose phone numbers and plates with 8, 6 and 9.</li><li>Schedule openings on dates with 8. Check your sign's lucky dates in our <a href="zodiac.html">Zodiac tool</a>.</li></ul>''', 6)

article("meaning-of-01810", "The Meaning of 01810 — Stock Code, Lucky Phrase and History",
 "What does 01810 mean? It is a Hong Kong stock code, a Chinese sound-alike phrase (“you will prosper”) and a date in Qing-dynasty history.", "Meaning of 01810", f'''
<h2>1. A Hong Kong stock code</h2>
<p>On the Hong Kong Stock Exchange, <b>01810</b> is the code of a large Chinese consumer-electronics and EV maker. It listed on <b>9 July 2018</b> as the city's first company with weighted voting rights. As of 31 August 2026 it was about <b>3.0% of the Hang Seng Index</b> (8th largest) and about <b>8.3% of the Hang Seng TECH Index</b> (3rd largest), per Hang Seng Indexes factsheets. It regularly features among the most-traded names by mainland investors through Southbound Stock Connect. Its RMB counter is <b>81810</b>.</p>
<p class="notice">01810.com is <b>independent</b> and not affiliated with that company, HKEX or any index provider. We reference the code for education and commentary only.</p>
{ad("inart")}
<h2>2. A lucky phrase</h2>
<p>Read aloud with Chinese number sounds, 0-1-8-1-0 carries a positive message:</p>
<div class="table-wrap"><table><tr><th>Digit</th><th>Reading</th><th>Sound-alike</th></tr>
<tr><td>0</td><td>líng</td><td>你 “you” (internet slang), or “whole / complete”</td></tr>
<tr><td>1</td><td>yāo</td><td>要 “will”</td></tr>
<tr><td>8</td><td>bā</td><td>發 “prosper”</td></tr>
<tr><td>1</td><td>yāo</td><td>要 “will”</td></tr>
<tr><td>0</td><td>líng</td><td>the circle closes, “complete”</td></tr></table></div>
<p>Our house reading is <b>“You will prosper — the whole circle.”</b> To be clear, this is a modern, playful coinage and not an established idiom. It follows the same logic as the well-documented <b>518 = 我要发</b> (“I will prosper”) and <b>18 ≈ 實發</b> (“sure to prosper”). <a href="decoder.html?n=01810">Run 01810 through the Decoder →</a></p>
<h2>3. A year in history</h2>
<p><b>1810</b> was the 15th year of the Jiaqing Emperor's reign in the Qing dynasty. In April that year, the pirate leader <b>Zheng Yi Sao</b> negotiated the surrender of her confederation to the Qing. Reports list <b>17,318 pirates, 226 ships and 1,315 cannons</b>. It was one of history's most remarkable negotiated settlements, and she kept her fortune.</p>
<h2>4. Other places the digits appear</h2>
<ul><li><b>181</b> is a China Telecom mobile prefix, so many mainland mobile numbers begin 1810…</li><li><b>0181</b> was the Outer London dialling code until 2000.</li></ul>
<h2>Why we built 01810</h2>
<p>Few numbers link a trading screen, a lucky phrase and a historical turning point. We built this site on that overlap. You get market tools and clear education for investors, plus the number culture that shapes how millions of people choose phone numbers, dates and even stocks. <a href="about.html">Read about our mission →</a></p>''', 6)
