# 01810.com — Markets & Fortune

Hong Kong & China markets, decoded, plus the culture of lucky numbers. A fast, static, fully responsive website built for GitHub Pages (free plan). No build server or database needed.

**Strategy, research and the phase-wise build prompt:** see [`docs/STRATEGY-AND-BUILD-PROMPT.md`](docs/STRATEGY-AND-BUILD-PROMPT.md).

## What's inside
| Area | Pages |
|---|---|
| Markets (revenue engine) | `markets.html` (HK code lookup, charts, watchlist, overview, hot lists, news, calendar), `tools.html` (HK trading cost, compound, dividend/DRIP, position size) |
| Number Lab (traffic engine) | `decoder.html` (luck score, phrases, digit meanings), `zodiac.html` (lunar-accurate zodiac, compatibility, Kua) |
| Learn / SEO | `learn.html` (glossary + FAQ schema), 3 long-form guides |
| Lead generation | `get-started.html` (4-step investor quiz → plan + reading request), lead-magnet boxes, exit-intent modal, full-report gates, newsletter everywhere |
| Monetisation | AdSense-ready slots (house ads until configured), `advertise.html`, `videos.html` (YouTube), `support.html` (donations), `contests.html`, `careers.html` |
| Legal | `privacy.html`, `terms.html`, `disclaimer.html` (financial + trademark/copyright), cookie consent |

## How publishing works
Every push to `main` runs `.github/workflows/publish.yml`. It builds the HTML pages from `_src/`, renders the PNG images from the SVG sources, commits the output to `main`, and publishes to the `gh-pages` branch, which GitHub Pages serves (free plan).

## Configure (edit `assets/js/config.js` only)
1. **AdSense:** set `adsenseClient: "ca-pub-…"` (+ optional slot IDs) and update `ads.txt`. Ads load only after cookie consent.
2. **Forms:** all forms post via FormSubmit to the owner inbox, which is stored encoded in `config.js` and assembled only at runtime. It never appears in any HTML. **The first submission triggers a one-time FormSubmit activation email. Click "Activate" in it.**
3. **Donations:** PayPal Donate works out of the box (runtime-built link). Optionally add `buyMeACoffeeUrl` or Stripe Payment Links.
4. **YouTube:** set `youtubeChannel` and swap the `videos` list for your own video IDs.
5. **Analytics:** set `ga4`.
6. **Contest end date:** `contestEnds`.

## Edit pages
Pages are generated from `_src/*.py`. Edit the content there and push. The workflow rebuilds everything. To build locally:
```bash
python3 _src/build.py
```

## Custom domain
In **Settings → Pages → Custom domain**, enter `01810.com`. Then point DNS at GitHub Pages: A records `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` and a `www` CNAME → `webworksa1.github.io`. Enable "Enforce HTTPS".

## Trademark / copyright
"01810" is used only as a number and domain name. The site is independent and not affiliated with any listed company, exchange, index provider or platform. See `disclaimer.html`.

Top banner on every page: *Contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership* → https://web.works/contact
