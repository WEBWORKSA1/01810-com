# 01810.com — Research, Winning Idea & Phase-Wise Build Prompt

## 1. Research: what "01810" means

| Lens | Finding | Why it matters |
|---|---|---|
| **Markets** | `01810` is the 5-digit HKEX stock code of a major listed Chinese consumer-tech & EV company (listed 9 Jul 2018, first HK dual-class listing). ~3.0% of the Hang Seng Index (#8) and ~8.3% of Hang Seng TECH (#3) as of 31 Aug 2026. Frequently among top Southbound Stock Connect flows. Its RMB counter is `81810`. | The string is a *ticker* that millions of HK/mainland retail investors type every day. Exact-match type-in + search intent is **finance** intent. |
| **HKEX code system** | Main Board 00001–02799, GEM 08000–08999, warrants 10000–29999, CBBCs 49500–69999; RMB counters = 8 + code. | Evergreen "how HK stock codes work" content ranks and converts. |
| **Numerology** | 0 = líng (slang for 你 "you"; also 良 "good"); 1 = yāo (幺) ≈ 要 "will/want"; 8 = bā ≈ 發 "prosper"; 18 = shí bā ≈ 實發 "sure to prosper". "0181 ≈ 你要发 – *you will prosper*" is a **new coinage** we can own. | Viral, shareable, huge search volume (horoscope ≈ 5M/mo; astrology ≈ 3.35M/mo). |
| **Money behind lucky numbers** | HK plate "18" sold for HK$16.5M (2008); "28" HK$18.1M (2016); 8888-8888 phone number ¥2.33M (2003); Beijing Olympics opened 8:08:08 pm on 8/8/08. | Proves the cultural premium → people pay for number meaning, dates, readings. |
| **History** | 1810 = 15th year of the Jiaqing Emperor; Zheng Yi Sao's pirate fleet (17,318 pirates, 226 ships) surrendered to the Qing in April 1810. | Storytelling content / "On this day" hooks. |
| **Audience** | ~40–60M overseas Chinese (Thailand 9.4M, Malaysia 7.5M, US 5.5M, Canada 1.7M) + HK/mainland Southbound investors + global China-tech investors. | Large, affluent, English-speaking diaspora = high-RPM Tier-1 traffic. |
| **Ad economics** | Finance AdSense RPM ≈ $20–50+; culture/astrology RPM much lower but 10–50× the volume. Broker referral CPAs typically $50–$300. | Blend: culture tools = traffic engine; finance = revenue engine. |

## 2. The decision (no hedging)

**Build "01810 — Markets & Fortune": the English-first hub for Hong Kong & China-tech investing, fused with a Chinese lucky-number lab.**

Why this beats the alternatives:

| Idea | Traffic | RPM | Lead value | Verdict |
|---|---|---|---|---|
| Pure lucky-number/feng-shui site | High | Low ($2–6) | Low (readings) | Traffic without money |
| Pure HK stock data site | Medium (habit-driven, 74% direct at AASTOCKS) | High ($20–50) | High (broker CPA) | Money, but slow SEO climb vs. incumbents |
| **Hybrid: Markets + Number Lab** | **High** (viral tools feed the funnel) | **Blended $10–25** | **High** (investor leads + reading leads + sponsors) | **Winner** |

The bold play: every lucky-number result cross-links to "lucky tickers" (HK codes like 00008, 01688, 01810) → pulls culture traffic into high-RPM finance pages and the investor lead funnel.

**Revenue stack (target order of impact):** 1) Investor lead-gen / broker referrals, 2) AdSense (finance pages), 3) Sponsorship ("Presented by" slots, newsletter sponsor), 4) Paid readings / premium PDF reports, 5) YouTube (embed + channel growth), 6) Donations ("red packet" support), 7) Contests (list growth, sponsor-funded prizes).

**Trademark/copyright position:** "01810" is used purely as a number/domain. No third-party logos, product names in branding, or implied affiliation. Company and exchange names appear only in factual, nominative references with a clear non-affiliation disclosure.

## 3. Features benchmarked from 30 world-class sites

investing.com, tradingview.com, finance.yahoo.com, seekingalpha.com, morningstar.com, fool.com, stockanalysis.com, finviz.com, macrotrends.net, simplywall.st, aastocks.com, etnet.com.hk, futunn.com, moomoo.com, itiger.com, hkex.com.hk, scmp.com, caixinglobal.com, technode.com, kr-asia.com, pandaily.com, yicaiglobal.com, thechinaproject.com, travelchinaguide.com, chinahighlights.com, yourchineseastrology.com, wofs.com, buymeacoffee.com, patreon.com, gleam.io.

Adopted patterns: live index ticker strip · heatmap · two-pillar navigation · universal search (stock code or number) · watchlist without account (localStorage) · Number Decoder with luck score · zodiac + compatibility + Kua calculators · HK stamp-duty/fee, compound-growth, dividend and position-size calculators · explainer/academy content · YouTube in-flow embeds · email-only newsletter with two interest checkboxes · content-gated "full report" · multi-step investor-profile quiz · consultation request form · trust signals (data source, methodology, disclaimer) · reserved-space ad slots (no CLS) · "Presented by" sponsor slot · Gleam-style bonus-entry contest · Buy-Me-a-Coffee-style red-packet donations ($8/$18/$88) with supporters wall and monthly tiers · dark mode · schema markup · sitemap.

---

## 4. PHASE-WISE BUILD PROMPT (copy each phase into your AI builder)

> **Global rules for every phase:** Static site (HTML/CSS/vanilla JS), hosted free on GitHub Pages; all paths relative; mobile-first responsive; WCAG AA; Lighthouse ≥ 90. On top of every page show: "Contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership" → link `https://web.works/contact`. The only email is the owner's inbox; it must **never appear in page text or raw HTML** — store it character-encoded in JS and assemble it at runtime for form endpoints and mailto links behind link text. No third-party logos or trademarks; include the trademark/copyright disclosure.

### Phase 1 — Foundation & brand
"Create the design system for **01810 — Markets & Fortune**: colors (ink #0b0f1a, jade #0fa37f, lucky red #e23d3d, gold #f5b301), Inter + Noto Serif SC fonts, light/dark themes with CSS tokens, 8-pt spacing, card/button/badge/table/form components. Build a shared header (sticky, two-pillar mega nav: Markets | Number Lab | Tools | Learn | Videos | Community), the top interest banner, a live index ticker strip (HSI, HS TECH, HSCEI, CSI 300, USD/CNH via free TradingView widget), a universal search that routes a stock code to the Markets page and any other number to the Decoder, a mobile bottom tab bar, cookie-consent banner, and a rich footer (sitemap, legal, social, newsletter)."

### Phase 2 — Core pages & content
"Build: Home (hero with Decoder input + market snapshot, feature grid, lucky-ticker spotlight, latest insights, video strip, lead magnet, contest teaser, support CTA), Markets (overview widget, heatmap, symbol lookup by HK code, watchlist saved in localStorage, HK trading calendar & A/H explainer), Learn hub (glossary + evergreen articles: 'How Hong Kong stock codes work', 'Why 8 is lucky — and what it's worth', 'The meaning of 01810'), About, Privacy, Terms, Disclaimer (financial + trademark/copyright), 404."

### Phase 3 — Interactive tools (traffic engine)
"Build the **Number Decoder** (digit meanings, known combos 168/518/520/888/1314/4/14/74, luck score 0–100, share button, 'lucky ticker' cross-link), **Zodiac finder** (lunar-new-year aware, 1924–2043) with compatibility matcher, **Kua number** calculator with 4 favorable directions, and investor calculators: HK trade cost (stamp duty 0.1%, SFC levy 0.0027%, AFRC 0.00015%, HKEX fee 0.00565%, broker commission input), compound growth, dividend income/DRIP, HKD↔USD position size. Every tool ends with an ad slot and a 'Email me my full report' gate."

### Phase 4 — Lead generation (revenue engine)
"Build a dedicated **Get Started** page: 4-step investor-profile quiz (goal → experience → capital band → markets of interest) with progress bar, then name/email/country/phone(optional)/consent; show a personalised result and 'broker comparison' with affiliate-ready CTAs. Add a **Personal Number & Fortune Reading** request form, a newsletter (HK Markets Daily / Lucky Numbers Weekly), exit-intent modal, sticky mobile CTA, inline end-of-article forms. All forms POST via AJAX to FormSubmit using the runtime-assembled email; add honeypot, validation, success state, UTM + source-page capture."

### Phase 5 — Monetisation layer
"Add AdSense auto-loader driven by a single `config.js` publisher ID (no script until configured + consent), reserved-size ad slots (leaderboard, in-article, sidebar sticky, below-tool), `ads.txt`; YouTube Videos page with categorised lazy-loaded embeds (privacy-enhanced youtube-nocookie) and channel subscribe CTA; Advertise/Sponsor page with packages (Presented-by, newsletter sponsor, contest sponsor, custom content), media-kit request form."

### Phase 6 — Community, donations, contests, hiring
"Build **Support** (red-packet amounts $8/$18/$88/custom, one-time/monthly toggle, tiers with perks, supporters wall, transparency on how funds are used: operations, promotion, marketing, hiring, prizes), **Contests** (monthly 'Pick 3 HK stocks' + 'Lucky Number Story' contests, prizes, bonus-entry actions, countdown, rules, entry form), **Careers** (open roles: writer, video editor, analyst, growth marketer, translators; application form with portfolio link)."

### Phase 7 — SEO, performance, compliance, launch
"Add per-page titles/meta/OG/Twitter cards, JSON-LD (Organization, WebSite+SearchAction, FAQPage, Article), sitemap.xml, robots.txt, manifest + SVG favicon, lazy loading, no layout shift, GitHub Pages deploy workflow, README with configuration steps (AdSense ID, FormSubmit activation, YouTube IDs, custom domain CNAME)."

### Phase 8 — Growth roadmap (post-launch)
Programmatic pages for numbers 0–9999 and every HK code (static generation), Traditional/Simplified Chinese versions with hreflang, daily market brief + newsletter automation, YouTube Shorts "Number of the Day", broker affiliate approvals (Futu/moomoo, Tiger, IBKR), sponsor outreach, contest partnerships.

---

## 5. KPIs (12-month targets, aggressive but achievable)

| Metric | M3 | M6 | M12 |
|---|---|---|---|
| Monthly visits | 15k | 80k | 300k |
| Newsletter subs | 1k | 6k | 25k |
| Leads / month | 150 | 900 | 3,500 |
| Blended RPM | $8 | $12 | $18 |
| Monthly revenue (ads + leads + sponsors) | ~$400 | ~$3.5k | ~$15k+ |

The biggest lever isn't AdSense — it's the investor-lead funnel and sponsor slots. Ads pay the bills; leads build the business.
