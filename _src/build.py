#!/usr/bin/env python3
"""01810.com static site builder.
Run:  python3 _src/build.py   -> writes all *.html pages to the repo root.
Pages are defined in pages_*.py as dicts registered via page()."""
import json, os, sys, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://01810.com"
VERSION = datetime.date.today().strftime("%Y%m%d")
PAGES = []

def page(slug, title, desc, body, schema=None, scripts=(), active="", hero=None, noindex=False):
    PAGES.append(dict(slug=slug, title=title, desc=desc, body=body, schema=schema,
                      scripts=scripts, active=active, hero=hero, noindex=noindex))

# ---------------- partials ----------------
def hp():
    return '<div class="hp" aria-hidden="true"><label>Leave empty<input name="_honey" tabindex="-1" autocomplete="off"></label></div>'

def status():
    return '<div class="form-status" role="status" aria-live="polite"></div>'

def ad(kind="leader"):
    return f'<div class="ad {kind}" aria-label="Advertisement"></div>'

def newsletter_inline(src="inline", dark=False):
    return f'''<form class="form" data-form="Newsletter signup ({src})" data-success="You're in! Watch your inbox for the next brief.">
  <div class="inline-form"><input type="email" name="email" required placeholder="Your email address" aria-label="Email address">
  <button class="btn btn-gold" type="submit">Get the free brief</button></div>
  <div class="chips"><label class="check" style="color:{'#c9d0e2' if dark else 'var(--muted)'}"><input type="checkbox" name="lists" value="HK Markets Daily" checked> HK Markets Daily</label>
  <label class="check" style="color:{'#c9d0e2' if dark else 'var(--muted)'}"><input type="checkbox" name="lists" value="Lucky Numbers Weekly" checked> Lucky Numbers Weekly</label></div>
  {hp()}{status()}
  <p class="form-note">Free. No spam. Unsubscribe anytime. By subscribing you agree to our <a href="privacy.html">Privacy Policy</a>.</p>
</form>'''

def lead_box(title="Get your free 2027 Wealth &amp; Luck Guide", sub="The Fire Goat year starts 6 Feb 2027. Get our free guide: lucky numbers and colours for each sign, dates to note, and a Hong Kong &amp; China markets outlook. Delivered with our weekly brief.", src="lead-box"):
    return f'''<div class="lead-box">
  <div>
    <span class="eyebrow">Free download · 2027 edition</span>
    <h2 class="mt-1">{title}</h2>
    <p>{sub}</p>
    <ul class="list-check" style="color:#e8ecf5"><li>Lucky numbers, colours &amp; directions for all 12 signs</li><li>HK/China market calendar, IPO watch &amp; key dates</li><li>Our favourite free calculators for smarter decisions</li></ul>
    <div class="trust"><span>🔒 No spam</span><span>✉ Weekly, free</span><span>⚡ Instant access</span></div>
  </div>
  <div class="card">
    <form class="form" data-form="Lead magnet: 2027 Guide ({src})" data-success="Done! Your guide is on its way. Check your inbox (and promotions tab).">
      <div><label for="lb-name-{src}">First name</label><input id="lb-name-{src}" name="name" required autocomplete="given-name" placeholder="e.g. Mei"></div>
      <div><label for="lb-email-{src}">Email</label><input id="lb-email-{src}" type="email" name="email" required autocomplete="email" placeholder="you@example.com"></div>
      <div><label for="lb-int-{src}">I'm most interested in</label><select id="lb-int-{src}" name="interest"><option>Hong Kong &amp; China investing</option><option>Lucky numbers &amp; feng shui</option><option>Both — give me everything</option></select></div>
      <label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to receive emails from 01810 and accept the <a href="privacy.html">Privacy Policy</a>.</label>
      {hp()}
      <button class="btn btn-primary btn-block" type="submit">Send my free guide →</button>
      {status()}
    </form>
  </div>
</div>'''

def sidebar(extra=""):
    return f'''<aside class="sidebar">
  {extra}
  <div class="card"><h3>📬 Free weekly brief</h3><p class="small">HK &amp; China markets + the week's lucky numbers. Takes 3 minutes to read.</p>{newsletter_inline("sidebar")}</div>
  {ad("tall")}
  <div class="card"><h3>Popular tools</h3><ul class="list-check small"><li><a href="decoder.html">Number Decoder</a></li><li><a href="zodiac.html">Zodiac &amp; Compatibility</a></li><li><a href="zodiac.html#kua">Kua Number</a></li><li><a href="tools.html#cost">HK Trading Cost</a></li><li><a href="markets.html">Markets &amp; Watchlist</a></li></ul></div>
</aside>'''

def cta_band(title="Ready to invest smarter in Hong Kong &amp; China?", sub="Take the 60-second investor profile and get a personalised starter plan.", href="get-started.html", label="Get my free plan →"):
    return f'<div class="cta-band"><div><h2 style="margin:0 0 .2em">{title}</h2><p>{sub}</p></div><a class="btn btn-gold" href="{href}">{label}</a></div>'

# ---------------- chrome ----------------
NAV = [
    ("markets", "markets.html", "Markets", None),
    ("lab", None, "Number Lab", [
        ("decoder.html", "Number Decoder", "Luck score for any number"),
        ("zodiac.html", "Chinese Zodiac", "Sign, element &amp; compatibility"),
        ("zodiac.html#kua", "Kua &amp; Feng Shui", "Your best directions"),
        ("why-8-is-lucky.html", "Why 8 is lucky", "The money behind numbers")]),
    ("tools", "tools.html", "Tools", None),
    ("learn", None, "Learn", [
        ("learn.html", "Learning Hub", "Guides, glossary &amp; FAQ"),
        ("hk-stock-codes-explained.html", "HK stock codes explained", "The 5-digit system"),
        ("meaning-of-01810.html", "The meaning of 01810", "Market, culture, history"),
        ("learn.html#glossary", "Glossary", "A–Z of HK &amp; China markets")]),
    ("videos", "videos.html", "Videos", None),
    ("community", None, "Community", [
        ("contests.html", "Contests &amp; Prizes", "Win monthly prizes"),
        ("support.html", "Support 01810", "Send a red packet"),
        ("careers.html", "Careers", "Join the team"),
        ("advertise.html", "Advertise &amp; Sponsor", "Reach our audience"),
        ("about.html", "About us", "Mission &amp; standards")]),
]

def header(active):
    items = []
    for key, href, label, sub in NAV:
        cur = ' aria-current="page"' if key == active else ""
        if sub:
            dd = "".join(f'<a href="{h}">{l}<small>{s}</small></a>' for h, l, s in sub)
            items.append(f'<li><button type="button" aria-haspopup="true"{cur}>{label} ▾</button><div class="dropdown">{dd}</div></li>')
        else:
            items.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    return f'''<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><a href="https://web.works/contact" target="_blank" rel="noopener">Contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership<span>Contact →</span></a></div>
<header class="site-header">
  <div class="container nav">
    <a class="brand" href="index.html" aria-label="01810 home"><img class="logo" src="assets/img/logo.svg" alt="" width="38" height="38"><span>01810<small>Markets &amp; Fortune</small></span></a>
    <ul class="menu">{"".join(items)}</ul>
    <div class="nav-right">
      <form class="search" role="search"><input aria-label="Search a stock code or any number" placeholder="Stock code or number…" inputmode="numeric"><button aria-label="Search">→</button></form>
      <button class="icon-btn" id="themeBtn" type="button" aria-label="Toggle dark mode">☾</button>
      <a class="btn btn-primary btn-sm" href="get-started.html">Get Started</a>
      <button class="icon-btn hamburger" type="button" aria-label="Open menu" aria-expanded="false">☰</button>
    </div>
  </div>
</header>
<div class="ticker-wrap"><div id="ticker"></div></div>'''

def footer():
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="foot-grid">
      <div>
        <a class="brand" href="index.html"><img class="logo" src="assets/img/logo.svg" alt="" width="38" height="38"><span>01810<small>Markets &amp; Fortune</small></span></a>
        <p class="mt-1">Hong Kong &amp; China markets, decoded — plus the culture of lucky numbers that moves money across Asia. Free tools, clear guides, weekly briefs.</p>
        {newsletter_inline("footer", dark=True)}
        <div class="socials"><a href="#" data-social-youtube aria-label="YouTube" target="_blank" rel="noopener">▶</a><a href="#" data-mail="Hello from a 01810 reader" aria-label="Email us">✉</a><a href="https://web.works/contact" target="_blank" rel="noopener" aria-label="Partnerships">🤝</a></div>
      </div>
      <div><h4>Markets &amp; Tools</h4><ul><li><a href="markets.html">Markets overview</a></li><li><a href="markets.html#watchlist">Watchlist</a></li><li><a href="tools.html#cost">HK trading cost</a></li><li><a href="tools.html#growth">Compound growth</a></li><li><a href="tools.html#dividend">Dividend / DRIP</a></li><li><a href="tools.html#position">Position size</a></li></ul></div>
      <div><h4>Number Lab</h4><ul><li><a href="decoder.html">Number Decoder</a></li><li><a href="zodiac.html">Chinese Zodiac</a></li><li><a href="zodiac.html#compat">Compatibility</a></li><li><a href="zodiac.html#kua">Kua number</a></li><li><a href="why-8-is-lucky.html">Why 8 is lucky</a></li><li><a href="meaning-of-01810.html">Meaning of 01810</a></li></ul></div>
      <div><h4>Community</h4><ul><li><a href="get-started.html">Get Started (free plan)</a></li><li><a href="contests.html">Contests &amp; prizes</a></li><li><a href="support.html">Support us</a></li><li><a href="careers.html">Careers</a></li><li><a href="videos.html">Videos</a></li><li><a href="learn.html">Learning hub</a></li></ul></div>
      <div><h4>Company</h4><ul><li><a href="about.html">About</a></li><li><a href="contact.html">Contact</a></li><li><a href="advertise.html">Advertise &amp; sponsor</a></li><li><a href="https://web.works/contact" target="_blank" rel="noopener">Buy / partner on this domain</a></li><li><a href="privacy.html">Privacy</a></li><li><a href="terms.html">Terms</a></li><li><a href="disclaimer.html">Disclaimer &amp; trademarks</a></li></ul></div>
    </div>
    <div class="legal">
      <p>© <span data-year>2026</span> 01810.com. All rights reserved. Original content, design, tools and code are the property of 01810.com and may not be reproduced without permission.</p>
      <p><b>Trademark &amp; copyright disclosure:</b> “01810” is used on this site only as a number and domain name. 01810.com is an independent publication and is <b>not affiliated with, endorsed by or sponsored by</b> any company whose securities trade under code 01810 or any similar code, nor by Hong Kong Exchanges and Clearing Ltd, Hang Seng Indexes Company, TradingView, YouTube/Google or any broker. All third-party names, tickers and marks belong to their respective owners and are used for identification and commentary only. Embedded videos and market widgets remain the property of their creators. See our full <a href="disclaimer.html">Disclaimer &amp; Trademark notice</a>.</p>
      <p><b>Not financial advice:</b> Content and tools are for education and entertainment only. Market data may be delayed. Numerology and feng shui content is cultural and for entertainment. Investing involves risk, including loss of principal.</p>
    </div>
  </div>
</footer>
<div id="chrome"></div>'''

def render(p):
    url = SITE + "/" + ("" if p["slug"] == "index" else p["slug"] + ".html")
    schema = ""
    if p["schema"]:
        for s in (p["schema"] if isinstance(p["schema"], list) else [p["schema"]]):
            schema += '<script type="application/ld+json">' + json.dumps(s, ensure_ascii=False) + "</script>\n"
    scripts = "".join(f'<script src="assets/js/{s}?v={VERSION}" defer></script>' for s in p["scripts"])
    robots = '<meta name="robots" content="noindex">' if p["noindex"] else '<meta name="robots" content="index,follow,max-image-preview:large">'
    full_title = p["title"] if p["slug"] == "index" else p["title"] + " | 01810"
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{p['desc']}">
{robots}
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#0b0f1a">
<meta property="og:type" content="{'article' if p['schema'] and 'Article' in json.dumps(p['schema']) else 'website'}">
<meta property="og:site_name" content="01810 — Markets &amp; Fortune">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{p['desc']}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/og.svg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/img/logo.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/img/logo.svg">
<link rel="manifest" href="manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&family=Noto+Serif+SC:wght@600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css?v={VERSION}">
<script>try{{var t=localStorage.getItem("theme");if(t)document.documentElement.setAttribute("data-theme",JSON.parse(t))}}catch(e){{}}</script>
<script src="assets/js/config.js?v={VERSION}" defer></script>
<script src="assets/js/chrome.js?v={VERSION}" defer></script>
<script src="assets/js/app.js?v={VERSION}" defer></script>
{scripts}
{schema}</head>
<body>
{header(p['active'])}
<main id="main">
{p['body']}
</main>
{footer()}
</body>
</html>
'''

def page_hero(crumb, title, sub, extra=""):
    return f'''<section class="page-hero"><div class="container"><div class="crumbs"><a href="index.html">Home</a> / {crumb}</div><h1>{title}</h1><p>{sub}</p>{extra}</div></section>'''

def build():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import build as B
    import pages_main, pages_lab, pages_community, pages_legal  # noqa: F401 (register pages)
    PAGES = B.PAGES
    for p in PAGES:
        with open(os.path.join(ROOT, p["slug"] + ".html"), "w", encoding="utf-8") as f:
            f.write(render(p))
    # sitemap
    urls = "".join(f"<url><loc>{SITE}/{'' if p['slug']=='index' else p['slug']+'.html'}</loc><lastmod>{datetime.date.today()}</lastmod><priority>{'1.0' if p['slug']=='index' else '0.8'}</priority></url>" for p in PAGES if not p["noindex"])
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    print(f"Built {len(PAGES)} pages")

if __name__ == "__main__":
    build()
