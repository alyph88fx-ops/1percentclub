"""Builds the legal pages (terms.html, privacy.html, risk.html) from the text below, in the site's look.

Edit the text here, then run:  python3 tools/build-legal.py
The pages are plain HTML at the repository root and are published with the rest of the site.
"""
import html, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
UPDATED = '27 November 2026'
EMAIL = 'hello@1-percentclub.com'
SITE = 'https://1-percentclub.com'
OWNER = '1 Percent Club ("1 Percent Club", "we", "us" or "our"), a trading education brand operated from Malaysia by its founder'

PAGES = {
  'terms': {
    'title': 'Terms of Use', 'nav': 'Terms',
    'lead': 'These terms cover your use of 1-percentclub.com, the member desk and everything we publish: videos, ebooks, indicators and live sessions.',
    'sections': [
      ('Who we are', f'''<p>This website is run by {OWNER}. You can reach us at <a href="mailto:{EMAIL}">{EMAIL}</a>. By using the website or signing up, you agree to these terms. If you do not agree, please do not use the website.</p>'''),
      ('Education only, not advice', '''<p>Everything we publish is general education about how financial markets work. It is not investment, financial, tax or legal advice, and it is not a recommendation to buy or sell anything.</p>
<p>We are not licensed by the Securities Commission Malaysia or any other regulator to give investment advice or to manage money, and we do neither. We never trade on your behalf, hold your funds or ask for your trading account passwords. Indicators and alerts are tools you configure and use yourself; any trade you take is your own decision.</p>
<p>Read the <a href="risk.html">Risk Disclosure</a> before you trade.</p>'''),
      ('Who can join', '<p>You must be at least 18 years old and able to enter a binding agreement. Trading leveraged products may be restricted where you live; it is your responsibility to follow the laws that apply to you.</p>'),
      ('Your account', '<p>Keep your login details private and tell us straight away if you think someone else has used your account. Accounts are personal: one person per membership. We may suspend an account that is shared, resold or used to break these terms.</p>'),
      ('Memberships and payments', '''<p>We offer a free Starter membership and paid memberships (Pro at US$50 a month and a one-time Lifetime membership at US$500). Prices, what each plan includes and how it renews are shown before you pay.</p>
<ul><li><b>Renewals.</b> Monthly plans renew automatically until you cancel. You can turn off auto-renew at any time from your member desk; you keep access until the end of the period you paid for.</li>
<li><b>Refunds.</b> If you are not happy with your first paid purchase, email us within 7 days and we will refund it. After that, payments are not refundable except where the law requires it.</li>
<li><b>Lifetime.</b> "Lifetime" means for as long as 1 Percent Club operates the membership, and includes future updates to the content and indicators it covers.</li>
<li><b>Price changes.</b> We may change prices for future billing periods. We will tell you at least 14 days before a change affects a renewal.</li></ul>'''),
      ('Indicators and licence keys', '<p>Indicators are licensed to you, not sold. Your licence lets you use them on your own devices (up to two at a time) for as long as your membership includes them. You may not share, resell, decompile or publish them or their licence keys. Indicators show what happened on a chart; they do not predict prices and can be wrong.</p>'),
      ('Our content', '<p>Videos, ebooks, indicators, charts, text and the 1 Percent Club name and logo belong to us or our licensors. You may use them for your own learning. You may not copy, record, re-upload, sell or share them, including in group chats or paid communities, without our written permission.</p>'),
      ('Live sessions and community', '<p>Be respectful in live sessions and community spaces. Do not post spam, promote other services, share signals for payment, harass anyone or share other members\' personal information. We may remove content or members who break these rules.</p>'),
      ('Third-party services', '<p>The website links to and relies on other services, such as TradingView, MetaTrader, brokers, Google and ForexFactory. We do not control them and are not responsible for them. Using them is subject to their own terms.</p>'),
      ('Limits of our responsibility', '''<p>We work hard to keep our material accurate, but markets change and mistakes happen; the website and content are provided "as is". To the extent the law allows, we are not responsible for any trading losses, lost profits or indirect losses arising from your use of the website, our content or our indicators.</p>
<p>Where we are responsible, our total liability to you is limited to the amount you paid us in the 12 months before the claim. Nothing in these terms limits any rights you have under the Consumer Protection Act 1999 or other laws that cannot be excluded.</p>'''),
      ('Ending your membership', '<p>You can stop using the website or cancel your membership at any time. We may suspend or close an account that breaks these terms; if we close a paid account without a good reason, we will refund the unused part of your payment.</p>'),
      ('Changes to these terms', '<p>We may update these terms. The date at the top shows the latest version. If a change is significant, we will tell members by email or on the member desk before it takes effect.</p>'),
      ('Governing law', '<p>These terms are governed by the laws of Malaysia, and the courts of Malaysia have jurisdiction over any dispute. Before going to court, please contact us first so we can try to sort it out.</p>'),
    ]},
  'privacy': {
    'title': 'Privacy Policy', 'nav': 'Privacy',
    'lead': 'What personal data 1 Percent Club collects, why, who it is shared with and how to reach us about it. Written in line with Malaysia\'s Personal Data Protection Act 2010 (PDPA).',
    'sections': [
      ('Who is responsible', f'<p>The data user (controller) is {OWNER}. For any question or request about your personal data, email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>'),
      ('What we collect', '''<ul><li><b>Your email address</b>, when you join the list or create a free account.</li>
<li><b>Account and membership details</b>, if you become a member: your name, email, plan, billing history and support messages.</li>
<li><b>Technical data</b> that any website receives: your IP address, browser and device type, and the pages you request. Our hosting provider records this in short-lived server logs.</li>
<li><b>Preferences stored on your device</b>: the member desk saves a few settings (such as reminders and ticked milestones) in your browser\'s local storage. They stay on your device and are not sent to us.</li></ul>
<p>We do not collect payment card numbers on this website, and we do not use advertising trackers or analytics cookies.</p>'''),
      ('Why we use it', '''<ul><li>To send you what you signed up for: the free Foundations track, membership emails and occasional news about new lessons and live sessions.</li>
<li>To run your membership, answer support requests and keep records we are required to keep.</li>
<li>To keep the website secure and working.</li></ul>
<p>We use your data only for these purposes, or for a directly related purpose, and with your consent where the law requires it. You can unsubscribe from emails at any time by replying "unsubscribe" or using the link in the email.</p>'''),
      ('Who we share it with', '''<p>We never sell your personal data. We share it only with service providers that help us run 1 Percent Club, and only what they need:</p>
<ul><li><b>Google</b> (Google Sheets and Gmail) stores the email list and our email.</li>
<li><b>GitHub</b> (GitHub Pages) hosts the website.</li>
<li><b>Google Fonts, cdnjs and jsDelivr</b> deliver fonts and code libraries to your browser, so they receive your IP address when a page loads.</li>
<li>A payment provider, if you buy a membership. It handles your card details directly; we never see them.</li></ul>
<p>We may also disclose data when the law requires it.</p>'''),
      ('Transfers outside Malaysia', '<p>These providers store data on servers outside Malaysia, mainly in the United States. We use providers that protect personal data to a standard comparable to the PDPA, as permitted by section 129 of the Act.</p>'),
      ('How long we keep it', '<p>We keep your email on the list until you unsubscribe or ask us to delete it. Membership and billing records are kept for as long as you are a member and then for up to 7 years where tax and accounting rules require it. Server logs are kept by our hosting provider for a short time only.</p>'),
      ('Your rights', f'''<p>Under the PDPA you can:</p>
<ul><li>ask for a copy of the personal data we hold about you;</li>
<li>ask us to correct data that is wrong, incomplete or out of date;</li>
<li>withdraw your consent, or ask us to stop sending you marketing;</li>
<li>ask us to delete your data, unless we must keep it by law;</li>
<li>ask us to send your data to another organisation in a common format.</li></ul>
<p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> from the address you signed up with. We will reply within 21 days. If you are not satisfied with our answer, you can complain to the Personal Data Protection Commissioner of Malaysia.</p>'''),
      ('Security', '<p>We limit who can access personal data, use providers with strong security, and serve the website only over an encrypted (HTTPS) connection. If a data breach is likely to cause you significant harm, we will notify you and the Commissioner as the law requires.</p>'),
      ('Children', '<p>1 Percent Club is for adults. We do not knowingly collect data from anyone under 18; if you think we have, contact us and we will delete it.</p>'),
      ('Changes to this policy', '<p>We will update this policy when our practices change. The date at the top shows the latest version; significant changes will be announced by email or on the member desk.</p>'),
      ('Language', '<p>This policy is published in English. A Bahasa Malaysia version is available on request; if the two differ, the Bahasa Malaysia version applies to the extent the PDPA requires.</p>'),
    ]},
  'risk': {
    'title': 'Risk Disclosure', 'nav': 'Risk',
    'lead': 'Please read this before you trade anything you learn about on 1 Percent Club.',
    'sections': [
      ('High risk of losing money', '<p>Trading foreign exchange (forex), contracts for difference (CFDs), indices, gold, cryptocurrencies and other leveraged products carries a high level of risk and is not suitable for everyone. Most retail traders lose money. You can lose all of the money you put in, and with some products and brokers you can lose more than your initial deposit.</p>'),
      ('Leverage works both ways', '<p>Leverage lets you control a large position with a small deposit. A small price move against you can therefore cause a large loss, trigger a margin call or close your positions automatically. Always know your position size and stop loss before you enter a trade.</p>'),
      ('Education, not advice', '<p>1 Percent Club teaches how markets work and how to build and test your own trading plan. Nothing we publish is a recommendation to trade, a signal service or personal advice. We are not licensed by the Securities Commission Malaysia to give investment advice, and we do not manage money. Every trading decision is yours.</p>'),
      ('Past results do not repeat', '<p>Examples, charts, backtests, case studies and student results show what happened in the past, often in specific market conditions. They do not mean you will get the same results. Hypothetical and backtested results have limits: they are made with hindsight and do not include every real-world cost, delay and emotion.</p>'),
      ('Indicators can be wrong', '<p>Our indicators and alerts describe price behaviour on a chart. They can give false or late readings, behave differently on different platforms, brokers and timeframes, and fail in fast or thin markets. Test any tool on a demo account first.</p>'),
      ('Crypto assets', '<p>Cryptocurrencies are highly volatile and may not be regulated where you live. In Malaysia, only digital asset exchanges registered with the Securities Commission may operate legally. Check that any exchange or broker you use is licensed by your local regulator.</p>'),
      ('Only trade what you can afford to lose', '<p>Never trade with money you need for living costs, debts or emergencies, and never borrow to trade. If you are unsure whether trading is right for you, speak to a licensed financial adviser.</p>'),
    ]},
}

CSS = '''
:root { color-scheme: dark; --ink:#0a0a0c; --panel:#111114; --line:#25262c; --line-2:#37383f; --fg:#ecebe6; --muted:#a8a7a2; --dim:#7f7e79; --red:#ff2d55; --crimson:#dc143c;
  --f-display:"Anton","Impact","Arial Narrow",sans-serif; --f-ui:"Chakra Petch","Barlow",system-ui,sans-serif; --f-body:"Barlow",system-ui,-apple-system,"Segoe UI",sans-serif;
  --gl:max(16px, env(safe-area-inset-left, 0px)); --gr:max(16px, env(safe-area-inset-right, 0px)); }
*, *::before, *::after { box-sizing: border-box; }
html { background: var(--ink); -webkit-text-size-adjust: 100%; scroll-padding-top: 90px; }
body { margin: 0; background: var(--ink); color: var(--fg); font: 400 17px/1.7 var(--f-body); -webkit-font-smoothing: antialiased; }
body::before { content: ""; position: fixed; inset: 0 0 auto; height: env(safe-area-inset-top, 0px); z-index: 20; background: var(--ink); }
a { color: var(--fg); text-decoration-color: var(--red); text-underline-offset: 3px; }
:focus-visible { outline: 2px solid var(--red); outline-offset: 3px; }
.wrap { max-width: 1120px; margin-inline: auto; padding-left: var(--gl); padding-right: var(--gr); }
.bar { position: sticky; top: env(safe-area-inset-top, 0px); z-index: 10; background: rgba(10,10,12,.9); -webkit-backdrop-filter: blur(12px); backdrop-filter: blur(12px); border-bottom: 1px solid var(--line); }
.bar .wrap { display: flex; align-items: center; gap: 18px; padding-block: 12px; }
.bar img { height: 32px; width: auto; display: block; }
.bar nav { margin-left: auto; display: flex; gap: 4px; flex-wrap: wrap; }
.bar nav a { font: 600 11px/1 var(--f-ui); letter-spacing: .14em; text-transform: uppercase; color: var(--muted); text-decoration: none; padding: 10px; }
.bar nav a[aria-current="page"] { color: var(--fg); box-shadow: inset 0 -2px 0 var(--red); }
header.top { padding-block: clamp(40px, 7vw, 84px) 28px; border-bottom: 1px solid var(--line); }
.eyebrow { font: 600 12px/1 var(--f-ui); letter-spacing: .22em; text-transform: uppercase; }
.eyebrow::before { content: "[ "; color: var(--red); } .eyebrow::after { content: " ]"; color: var(--red); }
h1 { font: 400 clamp(48px, 8vw, 104px)/.9 var(--f-display); text-transform: uppercase; margin: 16px 0 18px; }
.lead { color: var(--muted); font-size: 19px; max-width: 62ch; margin: 0; }
.updated { font: 500 12px/1 "JetBrains Mono", ui-monospace, monospace; color: var(--dim); margin-top: 18px; }
.layout { display: grid; grid-template-columns: 240px minmax(0, 1fr); gap: 56px; padding-block: 40px 80px; }
.toc { position: sticky; top: 90px; align-self: start; display: grid; gap: 2px; }
.toc span { font: 600 11px/1 var(--f-ui); letter-spacing: .16em; text-transform: uppercase; color: var(--dim); margin-bottom: 10px; }
.toc a { font: 500 14px/1.35 var(--f-body); color: var(--muted); text-decoration: none; padding: 6px 0 6px 12px; border-left: 1px solid var(--line); }
.toc a:hover { color: var(--fg); border-left-color: var(--red); }
article { max-width: 68ch; min-width: 0; }
section { padding-bottom: 30px; margin-bottom: 30px; border-bottom: 1px solid var(--line); }
section:last-child { border-bottom: 0; }
h2 { font: 400 clamp(26px, 3vw, 34px)/1.05 var(--f-display); text-transform: uppercase; margin: 0 0 14px; display: flex; gap: 14px; align-items: baseline; }
h2 .n { font: 500 13px/1 "JetBrains Mono", ui-monospace, monospace; color: var(--red); }
p { margin: 0 0 14px; color: #d6d5cf; } p:last-child { margin-bottom: 0; }
ul { margin: 0 0 14px; padding-left: 20px; color: #d6d5cf; } li { margin-bottom: 8px; } li::marker { color: var(--red); }
b { color: var(--fg); font-weight: 600; }
footer { border-top: 1px solid var(--line); padding-block: 28px calc(env(safe-area-inset-bottom, 0px) + 32px); color: var(--dim); font-size: 14px; }
footer .wrap { display: flex; flex-wrap: wrap; gap: 10px 24px; justify-content: space-between; }
footer a { color: var(--muted); }
@media (max-width: 860px) { .layout { grid-template-columns: 1fr; gap: 28px; } .toc { position: static; } .bar nav a:not([aria-current]) { display: none; } }
'''

def slug(s): return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')

def page(key, d):
    cur = ' aria-current="page"'
    nav = ''.join(f'<a href="{k}.html"{cur if k == key else ""}>{v["nav"]}</a>' for k, v in PAGES.items())
    toc = ''.join(f'<a href="#{slug(t)}">{html.escape(t)}</a>' for t, _ in d['sections'])
    body = ''.join(f'<section id="{slug(t)}"><h2><span class="n">{i:02d}</span>{html.escape(t)}</h2>{c}</section>' for i, (t, c) in enumerate(d['sections'], 1))
    desc = html.escape(d['lead'])
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{d['title']} · 1 Percent Club</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{key}.html">
<meta name="theme-color" content="#0a0a0c">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta property="og:title" content="{d['title']} · 1 Percent Club">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/og-image.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Barlow:wght@400;500;600&family=Chakra+Petch:wght@600&family=JetBrains+Mono:wght@500&display=swap">
<style>{CSS}</style>
</head>
<body>
<div class="bar"><div class="wrap"><a href="index.html" aria-label="1 Percent Club home"><img src="1pc-logo.webp" alt="1 Percent Club" width="821" height="322"></a><nav aria-label="Legal">{nav}</nav></div></div>
<header class="top"><div class="wrap"><span class="eyebrow">Legal</span><h1>{d['title']}</h1><p class="lead">{desc}</p><p class="updated">Last updated {UPDATED}</p></div></header>
<main class="wrap layout"><nav class="toc" aria-label="On this page"><span>On this page</span>{toc}</nav><article>{body}</article></main>
<footer><div class="wrap"><span>© 2026 1 Percent Club · Education only, not financial advice.</span><span><a href="index.html">Home</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></span></div></footer>
</body>
</html>
'''

for k, d in PAGES.items():
    (ROOT / f'{k}.html').write_text(page(k, d), encoding='utf-8')
    print('wrote', k + '.html')
