from build import page, page_hero

def legal(slug, title, desc, body):
    page(slug, title, desc, page_hero(title, title, desc) + f'<section class="block"><div class="container"><div class="article" style="max-width:860px;margin:0 auto"><div class="meta">Last updated: 29 September 2026</div>{body}</div></div></section>')

legal("privacy", "Privacy Policy", "How 01810 collects, uses and protects your information.", '''
<h2 class="mt-0">What we collect</h2>
<ul><li><b>Information you give us:</b> name, email, and other details you enter in forms (newsletter, lead, contest, reading, application, contact, pledge).</li><li><b>Stored on your device:</b> theme, watchlist, consent choice and referral ID, kept in your browser's local storage. It is never sent to us unless you submit a form.</li><li><b>With your consent:</b> analytics and advertising cookies from Google (Analytics / AdSense).</li></ul>
<h2>How we use it</h2>
<ul><li>To reply to you, deliver guides, reports, readings and newsletters, and run contests.</li><li>To improve the site and measure what's useful.</li><li>If you opt in, to share vetted partner offers. We do <b>not</b> sell your personal information.</li></ul>
<h2>Service providers</h2>
<p>Forms are delivered by email through a third-party form-relay service (FormSubmit). Payments are processed by the provider you choose (e.g. PayPal). Market widgets are provided by TradingView and videos by YouTube (privacy-enhanced mode). Hosting is on GitHub Pages. These providers have their own privacy policies.</p>
<h2>Advertising (Google AdSense)</h2>
<p>With consent, third-party vendors including Google use cookies to serve ads based on your previous visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visits. You can opt out of personalised advertising at <a href="https://adssettings.google.com" target="_blank" rel="noopener">Google Ads Settings</a> or <a href="https://www.aboutads.info" target="_blank" rel="noopener">aboutads.info</a>.</p>
<h2>Your rights</h2>
<p>Depending on where you live (for example under GDPR, UK GDPR, PIPEDA, Québec Law 25, CCPA or Hong Kong PDPO), you may access, correct, delete or export your data and withdraw consent. Use the <a href="contact.html">contact form</a> and choose “Correction / feedback”. You can change cookie consent by clearing your browser's site data.</p>
<h2>Retention &amp; security</h2><p>We keep submissions only as long as needed for the purpose collected, or as required by law. Submissions are transmitted over HTTPS.</p>
<h2>Children</h2><p>This site is not directed to children under 16, and contests are for adults 18+.</p>
<h2>Changes</h2><p>We may update this policy and will revise the date above.</p>''')

legal("terms", "Terms of Use", "The rules for using 01810.com, its tools and content.", '''
<h2 class="mt-0">Acceptance</h2><p>By using 01810.com you agree to these terms. If you do not agree, please do not use the site.</p>
<h2>Educational &amp; entertainment use only</h2><p>All content, calculators and tools are general information. Nothing on this site is financial, investment, tax, legal or professional advice, or a recommendation to buy or sell any security. Numerology, zodiac and feng shui content is cultural and for entertainment.</p>
<h2>Accuracy</h2><p>We work hard to be accurate, but data may be delayed, incomplete or out of date. Verify important information with primary sources and licensed professionals before acting.</p>
<h2>Intellectual property</h2><p>Original text, design, graphics, tools and code on 01810.com are protected by copyright. You may share links and short quotations with attribution. You may not copy, scrape or republish substantial portions without written permission. Third-party content (videos, widgets, trademarks) belongs to its owners.</p>
<h2>User submissions</h2><p>When you submit content (e.g. contest stories), you confirm it is yours and grant us a non-exclusive, worldwide, royalty-free licence to display it with credit. Do not submit unlawful, infringing or harmful content.</p>
<h2>Contests &amp; donations</h2><p>Contests follow the official rules on the <a href="contests.html">Contests page</a>. Donations are voluntary support for an independent publication. They are not charitable donations and are generally not tax-deductible.</p>
<h2>Links</h2><p>We are not responsible for third-party sites we link to or embed. Some links may be affiliate links, disclosed where they appear.</p>
<h2>Limitation of liability</h2><p>To the fullest extent permitted by law, 01810.com is not liable for any loss arising from use of the site, including investment losses.</p>
<h2>Changes &amp; contact</h2><p>We may update these terms at any time. Questions? <a href="contact.html">Contact us</a>.</p>''')

legal("disclaimer", "Disclaimer & Trademark / Copyright Notice", "Financial disclaimer, trademark and copyright disclosure for 01810.com.", '''
<h2 class="mt-0">Trademark disclosure</h2>
<p>“01810” is used on this website solely as a <b>number</b> and as the <b>domain name</b> 01810.com. It is used descriptively and culturally, including as a sound-alike phrase and a historical year. It is not used to identify or imitate any company, product or service.</p>
<p>01810.com is an <b>independent publication</b>. It is <b>not affiliated with, endorsed by, sponsored by or connected to</b>:</p>
<ul><li>any company whose securities trade, or have traded, under code 01810, 1810, 81810 or any similar code on any exchange;</li><li>Hong Kong Exchanges and Clearing Limited (HKEX), Hang Seng Indexes Company Limited, or any other exchange or index provider;</li><li>TradingView, Google, YouTube, PayPal, FormSubmit or any broker or financial institution mentioned or embedded.</li></ul>
<p>All company names, product names, tickers, index names, logos and trademarks mentioned are the property of their respective owners. They are used only for identification, education, commentary and news reporting, which is nominative and fair use. No third-party logos are used as branding on this site.</p>
<h2>Copyright</h2>
<p>© 2026 01810.com. All original content, including text, graphics, the 01810 logo artwork, page design, calculators and source code, is owned by 01810.com. Embedded YouTube videos remain the copyright of their creators and are shown through YouTube's official embed player under YouTube's Terms of Service. Market widgets are provided by TradingView under its widget terms. If you believe content on this site infringes your rights, please <a href="contact.html">contact us</a> with details and we will review it promptly.</p>
<h2>Financial disclaimer</h2>
<p>Content on 01810.com is for <b>educational and informational purposes only</b>. It is not investment advice, a solicitation or an offer to buy or sell any security. Past performance does not guarantee future results. Market data may be delayed or inaccurate. Consult a licensed financial adviser before making investment decisions. 01810.com and its contributors may hold positions in securities discussed.</p>
<h2>Cultural content disclaimer</h2>
<p>Lucky-number scores, zodiac readings, compatibility and Kua directions are based on traditional Chinese cultural beliefs. They are provided for entertainment and cultural interest and are not predictions or professional advice.</p>
<h2>Advertising &amp; affiliate disclosure</h2>
<p>We may earn revenue from advertising (including Google AdSense), sponsorships and affiliate or referral partnerships. Sponsored content is clearly labelled. Compensation does not influence our editorial opinions.</p>''')

page("404", "Page not found", "This page could not be found.", page_hero("404", "This number didn't add up 🧮", "The page you're looking for doesn't exist. But 404 isn't lucky anyway. Try one of these:") + '''
<section class="block"><div class="container grid-4"><a class="card link" href="index.html"><h3>🏠 Home</h3></a><a class="card link" href="decoder.html"><h3>✦ Number Decoder</h3></a><a class="card link" href="markets.html"><h3>📈 Markets</h3></a><a class="card link" href="get-started.html"><h3>🚀 Get Started</h3></a></div></section>''', noindex=True)
