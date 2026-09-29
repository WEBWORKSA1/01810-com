from build import page, ad, newsletter_inline, lead_box, sidebar, cta_band, page_hero, hp, status, SITE

# ======================= CONTESTS =======================
contests = page_hero("Community / Contests", "Contests &amp; Prizes", "Free to enter and open worldwide where permitted. Compete, learn and win prizes every month.",
  '<div class="countdown mt-2" data-countdown><div><b>00</b><small>days</small></div><div><b>00</b><small>hrs</small></div><div><b>00</b><small>min</small></div><div><b>00</b><small>sec</small></div></div><p class="small mt-1" style="color:#c9d0e2">October 2026 contests close 31 Oct, 23:59 HKT</p>') + f'''
<section class="block"><div class="container">
  <div class="grid-2">
    <div class="card"><span class="tag">Contest #1 · Markets</span><h2 class="mt-1">📈 Pick-3 HK Stock Challenge</h2><p>Pick three Hong Kong-listed stocks. The portfolio with the highest equal-weighted 30-day return from the start date wins. Paper trading only, so no money is invested.</p>
      <ul class="list-check"><li>Free, with one entry per person per month</li><li>Leaderboard published weekly</li><li>Winners featured in our newsletter</li></ul></div>
    <div class="card"><span class="tag gold">Contest #2 · Culture</span><h2 class="mt-1">✦ My Lucky Number Story</h2><p>Tell us, in 300 words or a short video, how a lucky number changed a decision: a plate, a phone number, a wedding date. Judged on story, originality and cultural insight.</p>
      <ul class="list-check"><li>Text, photo or video link</li><li>Best stories published on 01810</li><li>Community vote for the People's Choice award</li></ul></div>
  </div>
  <h2 class="mt-3 center">Monthly prizes</h2>
  <div class="grid-4 mt-2">
    <div class="card prize"><div class="medal">🥇</div><h3>1st place</h3><p><b>US$188</b> red packet + winner feature</p></div>
    <div class="card prize"><div class="medal">🥈</div><h3>2nd place</h3><p><b>US$88</b> red packet</p></div>
    <div class="card prize"><div class="medal">🥉</div><h3>3rd place</h3><p><b>US$18</b> red packet</p></div>
    <div class="card prize"><div class="medal">🧧</div><h3>People's Choice</h3><p>Personal Number &amp; Fortune reading</p></div>
  </div>
  <p class="center small muted mt-1">Prize pools are funded by sponsors and supporters. Want to sponsor a prize? <a href="advertise.html">Become a contest sponsor →</a></p>
  {ad("leader")}
  <div class="grid-2 mt-2" style="align-items:start">
    <div class="card"><h2>Enter now</h2>
      <form class="form" data-form="Contest entry" data-success="🎉 You're entered! Share your referral link below for bonus entries.">
        <div><label for="ctType">Contest</label><select id="ctType" name="contest" required><option value="Pick-3 HK Stock Challenge">📈 Pick-3 HK Stock Challenge</option><option value="My Lucky Number Story">✦ My Lucky Number Story</option></select></div>
        <div class="row"><div><label for="ctName">Full name</label><input id="ctName" name="name" required></div><div><label for="ctEmail">Email</label><input id="ctEmail" type="email" name="email" required></div></div>
        <div><label for="ctPicks">Your 3 HK stock codes (Pick-3) <span class="muted">e.g. 00700, 01810, 00005</span></label><input id="ctPicks" name="picks" placeholder="00000, 00000, 00000"></div>
        <div><label for="ctStory">Your story or video link (Lucky Number Story)</label><textarea id="ctStory" name="story" maxlength="2500"></textarea></div>
        <div><label for="ctCountry">Country</label><input id="ctCountry" name="country" required></div>
        <fieldset style="border:1px solid var(--line);border-radius:12px;padding:12px"><legend class="small"><b>Bonus entries (+1 each)</b></legend>
          <label class="check"><input type="checkbox" name="bonus" value="Newsletter"> Subscribe me to the free weekly brief</label>
          <label class="check"><input type="checkbox" name="bonus" value="YouTube"> I subscribed to the 01810 YouTube channel</label>
          <label class="check"><input type="checkbox" name="bonus" value="Shared"> I shared 01810 with a friend</label>
          <div class="mt-1"><label for="ctRef">Referred by (email or name)</label><input id="ctRef" name="referred_by"></div></fieldset>
        <label class="check"><input type="checkbox" name="rules" value="accepted" required> I am 18+ and accept the <a href="#rules">official rules</a>.</label>
        {hp()}<button class="btn btn-primary btn-block" type="submit">Submit my entry 🏆</button>{status()}
      </form>
      <div class="notice mt-1 small">Your referral link: <b id="refLink"></b> <button class="btn btn-sm btn-gold" data-share id="refShare" type="button">Copy / share</button></div>
    </div>
    <div>
      <div class="card" id="rules"><h2>Official rules (summary)</h2>
        <ol class="small"><li><b>No purchase necessary.</b> Free to enter. Void where prohibited or restricted by law.</li><li>Entrants must be 18 or older (or the age of majority where they live).</li><li>One entry per person per contest per month, plus up to 3 bonus entries. Duplicate or automated entries are disqualified.</li><li>Pick-3 performance is measured on HKEX closing prices over the stated period, equal-weighted, excluding dividends. Paper trading only.</li><li>Stories must be original. By entering, you grant 01810 a non-exclusive licence to publish your entry with credit.</li><li>Winners are notified by email and must reply within 14 days. Otherwise an alternate is selected.</li><li>Prizes are paid digitally (e.g. PayPal) and are non-transferable. Winners are responsible for any taxes.</li><li>Where a skill-testing question is required by law (e.g. Canada), winners must answer it correctly.</li><li>01810 may modify, suspend or cancel a contest for fraud, technical failure or reasons beyond its control.</li><li>Contests are not sponsored, endorsed or administered by any social platform, exchange or listed company.</li></ol></div>
      <div class="card mt-2"><h3>Past winners</h3><p class="muted small">Our first winners will be announced in November 2026. Your name could be first on this list.</p></div>
    </div>
  </div>
</div></section>
<script>
document.addEventListener("DOMContentLoaded",function(){{
  var id=Site.store.get("ref_id",null);if(!id){{id=Math.random().toString(36).slice(2,8);Site.store.set("ref_id",id);}}
  var url=location.origin+location.pathname+"?ref="+id;document.getElementById("refLink").textContent=url;document.getElementById("refShare").setAttribute("data-share",url);
  var r=new URLSearchParams(location.search).get("ref");if(r)document.getElementById("ctRef").value="ref:"+r;
}});
</script>'''
page("contests", "Contests & Prizes — Pick-3 HK Stock Challenge & Lucky Number Story",
     "Free monthly contests: pick 3 Hong Kong stocks or share your lucky number story. Win red-packet prizes and a personal reading, and earn bonus entries.",
     contests, active="community")

# ======================= SUPPORT / DONATIONS =======================
support = page_hero("Community / Support", "Support 01810 — send a red packet 🧧", "01810 is free and independent. Your support keeps the tools running and funds new features, videos, marketing, contest prizes and new team members.") + f'''
<section class="block"><div class="container grid-2" style="align-items:start">
  <div class="tool" id="donate">
    <div class="toggle" data-group="freq" role="group" aria-label="Frequency"><button type="button" class="on" data-f="once">One-time</button><button type="button" data-f="monthly">Monthly</button></div>
    <h2 class="mt-2">Choose a lucky amount</h2>
    <div class="amounts" data-group="amount">
      <button type="button" class="amount" data-value="8"><b>$8</b><small>發 prosper</small></button>
      <button type="button" class="amount selected" data-value="18"><b>$18</b><small>要發 will prosper</small></button>
      <button type="button" class="amount" data-value="88"><b>$88</b><small>double fortune</small></button>
      <button type="button" class="amount" data-value="168"><b>$168</b><small>一路發 all the way</small></button>
    </div>
    <div class="mt-1"><label for="dCustom">Or enter a custom amount (USD)</label><input id="dCustom" type="number" min="1" placeholder="e.g. 28"></div>
    <div class="hero-actions">
      <button class="btn btn-primary" id="payPal" type="button">Give $<span id="dAmt">18</span> with PayPal</button>
      <a class="btn btn-gold" id="bmc" href="#" target="_blank" rel="noopener" style="display:none">☕ Buy us a coffee</a>
      <a class="btn btn-jade" id="stripe" href="#" target="_blank" rel="noopener" style="display:none">💳 Card / Apple Pay</a>
    </div>
    <p class="form-note mt-1">Secure payment on the provider's site. Card and PayPal details never touch our servers.</p>
    <hr style="border:0;border-top:1px solid var(--line);margin:22px 0">
    <h3>Prefer to pledge or give another way?</h3>
    <p class="small muted">Bank transfer, corporate matching, in-kind support (hosting, design, data) or a larger gift: tell us and we'll reply with details.</p>
    <form class="form" data-form="Donation pledge" data-success="Thank you! We'll reply with payment details shortly. 🧧">
      <div class="row"><div><label for="plName">Name</label><input id="plName" name="name" required></div><div><label for="plEmail">Email</label><input id="plEmail" type="email" name="email" required></div></div>
      <div class="row"><div><label for="plAmt">Amount</label><input id="plAmt" name="amount" placeholder="e.g. $888 or in-kind"></div><div><label for="plUse">Direct my support to</label><select id="plUse" name="designation"><option>Where it's needed most</option><option>Operations &amp; hosting</option><option>Promotion &amp; marketing</option><option>Hiring talent</option><option>Contest prizes</option><option>Video production</option></select></div></div>
      <div><label for="plMsg">Message for the supporters wall <span class="muted">(optional)</span></label><input id="plMsg" name="message" maxlength="140"></div>
      <label class="check"><input type="checkbox" name="public" value="yes"> Show my first name on the supporters wall</label>
      {hp()}<button class="btn btn-ghost btn-block" type="submit">Send pledge</button>{status()}
    </form>
  </div>
  <div>
    <h2>Where your money goes</h2>
    <div class="card">
      <p class="small"><b>Operations &amp; hosting</b> · 30%</p><div class="bar"><span style="width:30%"></span></div>
      <p class="small mt-1"><b>New tools &amp; content</b> · 25%</p><div class="bar"><span style="width:25%"></span></div>
      <p class="small mt-1"><b>Promotion &amp; marketing</b> · 20%</p><div class="bar"><span style="width:20%"></span></div>
      <p class="small mt-1"><b>Hiring writers, editors &amp; translators</b> · 15%</p><div class="bar"><span style="width:15%"></span></div>
      <p class="small mt-1"><b>Contest prizes</b> · 10%</p><div class="bar"><span style="width:10%"></span></div>
      <p class="form-note mt-1">Target allocation. We publish an annual transparency note.</p>
    </div>
    <h2 class="mt-2">Monthly supporter tiers</h2>
    <div class="grid-3">
      <div class="card tier"><h3>Friend</h3><div class="price">$5<small>/mo</small></div><ul class="list-check small"><li>Name on supporters wall</li><li>Supporter badge in newsletter</li></ul></div>
      <div class="card tier featured"><span class="ribbon">Popular</span><h3>Lucky 8</h3><div class="price">$8<small>/mo</small></div><ul class="list-check small"><li>Everything in Friend</li><li>Ad-light newsletter</li><li>Early access to new tools</li></ul></div>
      <div class="card tier"><h3>Patron</h3><div class="price">$18<small>/mo</small></div><ul class="list-check small"><li>Everything in Lucky 8</li><li>Annual personal reading</li><li>Vote on new features</li></ul></div>
    </div>
    <h2 class="mt-2">Supporters wall</h2>
    <div class="wall"><div>🧧 Be our first founding supporter. Your name goes here.</div></div>
    <div class="card mt-2"><h3>Businesses: sponsor instead</h3><p class="small">Get your brand in front of investors and culture lovers with “Presented by” placements, newsletter slots and contest sponsorships.</p><a class="btn btn-jade btn-sm" href="advertise.html">See sponsorship packages →</a></div>
  </div>
</div></section>
<script>
document.addEventListener("DOMContentLoaded",function(){{
  var C=window.SITE_CONFIG||{{}},amt=18,freq="once",$=Site.$;
  function upd(){{var c=+$("#dCustom").value;if(c>0)amt=c;$("#dAmt").textContent=amt;}}
  $("[data-group=amount]").addEventListener("pick",function(e){{amt=+e.detail;$("#dCustom").value="";upd();}});
  $("#dCustom").addEventListener("input",upd);
  Site.$$("[data-group=freq] button").forEach(function(b){{b.addEventListener("click",function(){{Site.$$("[data-group=freq] button").forEach(function(x){{x.classList.remove("on")}});b.classList.add("on");freq=b.dataset.f;}});}});
  if(C.buyMeACoffeeUrl){{$("#bmc").href=C.buyMeACoffeeUrl;$("#bmc").style.display="";}}
  if(C.stripeLinks&&(C.stripeLinks.once||C.stripeLinks.monthly)){{$("#stripe").style.display="";$("#stripe").addEventListener("click",function(){{this.href=(freq==="monthly"&&C.stripeLinks.monthly)||C.stripeLinks.once;}});}}
  $("#payPal").addEventListener("click",function(){{
    if(!C.paypalDonate){{location.hash="#donate";return;}}
    var u="https://www.paypal.com/donate/?business="+encodeURIComponent(Site.inbox())+"&amount="+amt+"&currency_code=USD&no_recurring="+(freq==="monthly"?"0":"1")+"&item_name="+encodeURIComponent("Support 01810.com ("+freq+")");
    window.open(u,"_blank","noopener");
  }});
}});
</script>'''
page("support", "Support 01810 — Donate a Lucky Red Packet ($8, $18, $88)",
     "Support independent Hong Kong & China market education and Chinese number-culture tools. Give $8, $18 or $88 one-time or monthly via PayPal, or pledge another way.",
     support, active="community")

# ======================= CAREERS =======================
ROLES = [
 ("Markets Writer (HK &amp; China)", "Freelance · Remote", "Daily briefs, earnings recaps and explainers. You know HKEX, Stock Connect and China tech."),
 ("Video Editor / Shorts Creator", "Freelance · Remote", "Turn our guides into YouTube videos and Shorts. Motion graphics are a plus."),
 ("Culture &amp; Feng Shui Writer", "Freelance · Remote", "Write on number meanings, the zodiac, festivals and auspicious dates, with care and accuracy."),
 ("Growth &amp; SEO Marketer", "Part-time · Remote", "Own organic growth, programmatic SEO, the newsletter funnel and partnerships."),
 ("Translators (繁體 / 简体)", "Freelance · Remote", "Localise our guides and tools for Traditional and Simplified Chinese readers."),
 ("Front-end Developer", "Contract · Remote", "Build new calculators and data tools in vanilla JS with a focus on speed and accessibility."),
]
roles = "".join(f'<div class="card"><span class="tag">{t}</span><h3 class="mt-1">{n}</h3><p>{d}</p><a class="btn btn-sm btn-jade" href="#apply" onclick="document.getElementById(\'apRole\').value=this.dataset.r" data-r="{n.replace("&amp;","&")}">Apply →</a></div>' for n, t, d in ROLES)
careers = page_hero("Community / Careers", "Careers at 01810", "Help us build the web's best bridge between Asian markets and number culture. We're remote-first and pay for great work.") + f'''
<section class="block"><div class="container">
  <div class="section-head"><h2>Open roles</h2><p>Don't see your role? Apply anyway. We hire for talent.</p></div>
  <div class="grid-3">{roles}</div>
  <div class="grid-2 mt-3" style="align-items:start">
    <div><h2>Why work with us</h2><ul class="list-check"><li>Remote and flexible, wherever you are</li><li>Paid per project or on a monthly retainer</li><li>Bylines and portfolio credit</li><li>Early team with real ownership of what you build</li></ul>{ad("rect")}</div>
    <div class="card" id="apply"><h2>Apply</h2>
      <form class="form" data-form="Job application" data-success="Application received. We review every application and reply within 7 days.">
        <div class="row"><div><label for="apName">Full name</label><input id="apName" name="name" required></div><div><label for="apEmail">Email</label><input id="apEmail" type="email" name="email" required></div></div>
        <div class="row"><div><label for="apRole">Role</label><select id="apRole" name="role">{''.join(f"<option>{n.replace('&amp;','&')}</option>" for n,_,_ in ROLES)}<option>Other / open application</option></select></div><div><label for="apLoc">Location / time zone</label><input id="apLoc" name="location"></div></div>
        <div><label for="apLink">Portfolio / LinkedIn / CV link</label><input id="apLink" type="url" name="portfolio" placeholder="https://" required></div>
        <div><label for="apLang">Languages</label><input id="apLang" name="languages" placeholder="English, 粵語, 普通话…"></div>
        <div><label for="apWhy">Why you? (short)</label><textarea id="apWhy" name="message" required></textarea></div>
        <div><label for="apRate">Expected rate</label><input id="apRate" name="rate" placeholder="e.g. $X per article / hour"></div>
        {hp()}<button class="btn btn-primary btn-block" type="submit">Send application</button>{status()}
      </form></div>
  </div>
</div></section>'''
page("careers", "Careers — Remote Writer, Video, SEO & Developer Jobs at 01810",
     "Join 01810: remote freelance and part-time roles for markets writers, video editors, culture writers, growth marketers, translators and developers.", careers, active="community")

# ======================= ADVERTISE =======================
PK = [("Presented-by Sponsor", "from $888/mo", "Exclusive “Presented by” branding on one tool (Decoder, Zodiac or Calculators), logo in the header slot and a monthly newsletter mention.", True),
      ("Newsletter Sponsor", "from $388/issue", "Top placement in the HK Markets Daily or Lucky Numbers Weekly brief, with a 60-word message, logo and link.", False),
      ("Contest Sponsor", "from $1,888/mo", "Fund the monthly prize pool. Your brand appears on the contest page, entry emails and winner announcements.", False),
      ("Sponsored Guide / Video", "from $1,288", "A clearly labelled in-depth guide or video co-created with our editorial team, with permanent placement.", False),
      ("Display &amp; Native", "CPM from $18", "Direct-sold banners in premium positions: leaderboard, sidebar and below-tool.", False),
      ("Lead-gen Partnership", "CPL / CPA", "Brokers, wealth platforms and education providers can reach qualified leads from our investor-profile funnel.", False)]
pk = "".join(f'<div class="card tier{" featured" if f else ""}">{"<span class=ribbon>Best value</span>" if f else ""}<h3>{n}</h3><div class="price" style="font-size:1.4rem">{p}</div><p class="small">{d}</p></div>' for n, p, d, f in PK)
adv = page_hero("Community / Advertise", "Advertise &amp; Sponsor on 01810", "Reach a rare mix of Hong Kong &amp; China investors and a global audience that cares about Chinese culture, across Asia and the diaspora.") + f'''
<section class="block"><div class="container">
  <div class="grid-4">
    <div class="card center"><h2 style="margin:0">HK · CN · SG · MY</h2><p class="small muted">Core Asian markets</p></div>
    <div class="card center"><h2 style="margin:0">US · CA · UK · AU</h2><p class="small muted">Tier-1 diaspora audience</p></div>
    <div class="card center"><h2 style="margin:0">High intent</h2><p class="small muted">Readers who invest, trade and plan</p></div>
    <div class="card center"><h2 style="margin:0">Brand-safe</h2><p class="small muted">Editorial, education, culture</p></div>
  </div>
  <h2 class="mt-3">Packages</h2>
  <div class="grid-3">{pk}</div>
  <div class="grid-2 mt-3" style="align-items:start">
    <div><h2>Who advertises with us</h2><ul class="list-check"><li>Brokers &amp; trading platforms (HK, US, SG)</li><li>Wealth, insurance &amp; remittance services</li><li>Education &amp; language-learning brands</li><li>Travel, luxury &amp; lifestyle brands for festive seasons</li><li>Feng shui consultants, jewellers &amp; wedding services</li></ul>
      <div class="notice mt-2"><b>Interested in the whole site or domain?</b> We're open to acquisitions, joint ventures and strategic partnerships. <a href="https://web.works/contact" target="_blank" rel="noopener">Contact us via web.works →</a></div>
      <p class="small muted mt-2">All sponsored content is clearly labelled. We reserve the right to decline advertisers that are not a fit for our audience or that don't meet regulatory standards.</p></div>
    <div class="card"><h2>Request the media kit</h2>
      <form class="form" data-form="Advertising / media kit request" data-success="Thanks! Our partnerships team will send the media kit and rates within 1 business day.">
        <div class="row"><div><label for="adName">Name</label><input id="adName" name="name" required></div><div><label for="adEmail">Work email</label><input id="adEmail" type="email" name="email" required></div></div>
        <div class="row"><div><label for="adCo">Company</label><input id="adCo" name="company" required></div><div><label for="adSite">Website</label><input id="adSite" name="website" type="url" placeholder="https://"></div></div>
        <div class="row"><div><label for="adPkg">Interested in</label><select id="adPkg" name="package">{''.join(f"<option>{n.replace('&amp;','&')}</option>" for n,_,_,_ in PK)}<option>Site / domain acquisition or partnership</option></select></div><div><label for="adBud">Monthly budget</label><select id="adBud" name="budget"><option>Under $500</option><option>$500 – $2,000</option><option>$2,000 – $10,000</option><option>$10,000+</option></select></div></div>
        <div><label for="adMsg">Goals / details</label><textarea id="adMsg" name="message"></textarea></div>
        {hp()}<button class="btn btn-primary btn-block" type="submit">Get media kit &amp; rates</button>{status()}
      </form></div>
  </div>
</div></section>'''
page("advertise", "Advertise & Sponsor — Reach HK & China Investors and the Chinese Diaspora",
     "Advertising and sponsorship on 01810: Presented-by tool sponsorships, newsletter sponsors, contest sponsors, sponsored guides, display and lead-gen partnerships.", adv, active="community")

# ======================= ABOUT =======================
about = page_hero("About", "About 01810", "An independent publication where Hong Kong &amp; China markets meet the culture of lucky numbers.") + f'''
<section class="block"><div class="container layout"><div class="article">
  <h2 class="mt-0">Our mission</h2>
  <p>Millions of people invest in Hong Kong and China. Millions more choose phone numbers, wedding dates and even stock codes by how lucky they sound. Most sites serve only one of these groups. <b>01810 serves both</b>, with free tools, plain-English education and a respect for culture.</p>
  <h2>What we stand for</h2>
  <ul class="list-check"><li><b>Free and useful:</b> every core tool is free, with no account needed.</li><li><b>Accurate:</b> we cite sources, date our figures and correct mistakes quickly.</li><li><b>Independent:</b> we are not affiliated with any exchange, index provider or listed company. Sponsored content is always labelled.</li><li><b>Respectful:</b> number culture is presented as culture and entertainment, never as a promise.</li></ul>
  <h2>Editorial standards</h2>
  <p>Market figures come from primary sources such as HKEX, Hang Seng Indexes and company filings. Cultural content is checked against established references. Calculators show their formulas and assumptions. Read our <a href="disclaimer.html">disclaimer</a>.</p>
  <h2>Work with us</h2>
  <div class="hero-actions"><a class="btn btn-primary" href="advertise.html">Advertise / sponsor</a><a class="btn btn-ghost" href="careers.html">Join the team</a><a class="btn btn-ghost" href="support.html">Support us</a><a class="btn btn-ghost" href="https://web.works/contact" target="_blank" rel="noopener">Domain / partnership inquiries</a></div>
</div>{sidebar()}</div></section>'''
page("about", "About 01810 — Mission, Editorial Standards & Team",
     "01810 is an independent publication combining Hong Kong & China market education with Chinese lucky-number culture. Learn about our mission and editorial standards.", about, active="community")

# ======================= CONTACT =======================
contact = page_hero("Contact", "Contact us", "Questions, corrections, partnerships or press. We read every message.") + f'''
<section class="block"><div class="container grid-2" style="align-items:start">
  <div class="card"><h2>Send a message</h2>
    <form class="form" data-form="Contact form" data-success="Message sent. We'll reply within 1–2 business days.">
      <div class="row"><div><label for="coName">Name</label><input id="coName" name="name" required autocomplete="name"></div><div><label for="coEmail">Email</label><input id="coEmail" type="email" name="email" required autocomplete="email"></div></div>
      <div><label for="coTopic">Topic</label><select id="coTopic" name="topic"><option>General question</option><option>Advertising / sponsorship</option><option>Buy or partner on this website / domain</option><option>Personal reading</option><option>Contest</option><option>Donation / support</option><option>Careers</option><option>Correction / feedback</option><option>Press</option></select></div>
      <div><label for="coMsg">Message</label><textarea id="coMsg" name="message" required></textarea></div>
      <label class="check"><input type="checkbox" name="newsletter" value="yes"> Also subscribe me to the free weekly brief</label>
      {hp()}<button class="btn btn-primary btn-block" type="submit">Send message</button>{status()}
    </form></div>
  <div>
    <div class="card"><h3>✉ Email</h3><p class="small">Prefer your own mail app?</p><a class="btn btn-jade btn-sm" href="#" data-mail="Inquiry from 01810.com">Email the 01810 team</a></div>
    <div class="card mt-2"><h3>🤝 Website, domain, sponsorship &amp; partnership</h3><p class="small">Interested in acquiring this website or domain, or in sponsorship, advertising or a partnership?</p><a class="btn btn-gold btn-sm" href="https://web.works/contact" target="_blank" rel="noopener">Contact via web.works →</a></div>
    <div class="card mt-2"><h3>⏱ Response times</h3><ul class="list-check small"><li>General: 1–2 business days</li><li>Advertising: 1 business day</li><li>Corrections: prioritised</li></ul></div>
  </div>
</div></section>'''
page("contact", "Contact 01810 — Advertising, Partnerships, Readings & Feedback",
     "Contact the 01810 team about advertising, sponsorship, partnerships, readings, contests, careers or corrections.", contact)
