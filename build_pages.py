#!/usr/bin/env python3
"""Generate NPhones subpages from a shared template."""
import os

LOGO_SVG = '''<svg width="30" height="42" viewBox="8 8 86 120" aria-hidden="true"><rect x="10" y="10" width="50" height="78" rx="16" fill="#B9E7DE"/><rect x="24" y="24" width="52" height="82" rx="16" fill="#15B097"/><rect x="38" y="40" width="54" height="86" rx="16" fill="#0B6B5C"/><rect x="46" y="50" width="38" height="66" rx="8" fill="#F4F6F5"/></svg>'''
FOOT_SVG = LOGO_SVG.replace('width="30" height="42"', 'width="24" height="34"').replace('fill="#0B6B5C"', 'fill="#F4F6F5"', 1)

def blob(kind, depth, style):
    return f'<div class="blob {kind}" data-depth="{depth}" style="{style}"><div class="blob-inner"></div></div>'

BLOBSET = (blob('leaf', '0.05', 'width:380px;height:380px;top:-110px;right:-70px;')
           + blob('sage', '0.03', 'width:340px;height:340px;bottom:-100px;left:-80px;'))

def page(title, desc, kicker, h1, sub, body, cta_href="contact.html#demo"):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
<link rel="icon" type="image/svg+xml" href="assets/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32.png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="stylesheet" href="assets/style.css?v=11">
</head>
<body>
<div class="nav-wrap">
  <nav class="nav" aria-label="Main">
    <a class="nav-logo" href="index.html" aria-label="NPhones home">{LOGO_SVG}<span class="wordmark">NPhones</span></a>
    <ul class="nav-links">
      <li><a href="platform.html">Platform</a></li>
      <li><a href="use-cases.html">Use cases</a></li>
      <li><a href="pricing.html">Pricing</a></li>
      <li><a href="partners.html">Partners</a></li>
      <li><a href="about.html">About</a></li>
      <li class="menu-cta"><a class="btn btn-primary" href="{cta_href}">Request a demo</a></li>
    </ul>
    <a class="btn btn-primary nav-cta" href="{cta_href}">Request a demo</a>
    <button class="nav-burger" aria-label="Menu"><svg width="18" height="14" viewBox="0 0 18 14" aria-hidden="true"><path d="M1 1h16M1 7h16M1 13h16" stroke="#080808" stroke-width="2" stroke-linecap="round"/></svg></button>
  </nav>
</div>

<header class="section section-tint page-first">
  <div class="blobs" aria-hidden="true">{BLOBSET}</div>
  <div class="section-inner">
    <div class="section-head" style="max-width:720px">
      <span class="kicker">{kicker}</span>
      <h1>{h1}</h1>
      <p style="margin-top:1rem;color:rgba(8,8,8,.65)">{sub}</p>
    </div>
  </div>
</header>

{body}

<footer class="section section-dark footer">
  <div class="blobs" aria-hidden="true">{blob('forest', '0.04', 'width:360px;height:360px;top:-100px;right:10%;')}</div>
  <div class="section-inner">
    <div class="footer-grid">
      <div>
        <div style="display:flex;align-items:center;gap:10px">{FOOT_SVG}<span class="wordmark">NPhones</span></div>
        <p class="tagline">One device, Ndless phones.</p>
        <p style="margin-top:1rem;font-size:14px;color:rgba(247,247,245,.6)">The cloud business phone platform for enterprises.<br>Beer Sheva, Israel</p>
      </div>
      <div><h4>Product</h4><ul>
        <li><a href="platform.html">Platform</a></li>
        <li><a href="how-it-works.html">How it works</a></li>
        <li><a href="security.html">Security</a></li>
        <li><a href="insights.html">Insights</a></li>
        <li><a href="pricing.html">Pricing</a></li>
      </ul></div>
      <div><h4>Company</h4><ul>
        <li><a href="use-cases.html">Use cases</a></li>
        <li><a href="partners.html">Partners</a></li>
        <li><a href="about.html">About</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul></div>
      <div><h4>Account</h4><ul>
        <li><a href="https://app.nphones.com/login">Log in</a></li>
        <li><a href="privacy.html">Privacy</a></li>
        <li><a href="terms.html">Terms</a></li>
      </ul></div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 NPhones. All rights reserved.</span>
      <a href="https://www.linkedin.com/" aria-label="NPhones on LinkedIn" style="color:rgba(247,247,245,.6)">LinkedIn</a>
    </div>
  </div>
</footer>
<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.18/dist/lenis.min.js"></script>
<script src="assets/main.js?v=8"></script>
</body>
</html>
'''

def cta_strip(h, sub, btn="Request a demo", href="contact.html#demo"):
    return f'''<section class="section section-forest cta-panel">
  <div class="blobs" aria-hidden="true">{blob('leaf', '0.05', 'width:360px;height:360px;top:-110px;right:-80px;')}</div>
  <div class="section-inner">
    <h2 style="max-width:24ch;margin-inline:auto">{h}</h2>
    <p style="margin:1rem auto 0;max-width:52ch;color:rgba(247,247,245,.75)">{sub}</p>
    <div style="margin-top:1.8rem"><a class="btn btn-light" href="{href}">{btn}</a></div>
  </div>
</section>'''

def card(title, text, extra=''):
    return f'<div class="glass card reveal" data-tilt><h3>{title}</h3><p style="margin-top:.5rem">{text}</p>{extra}</div>'

def section(inner, cls='', el='section'):
    return f'<{el} class="section {cls}"><div class="blobs" aria-hidden="true">{BLOBSET}</div><div class="section-inner">{inner}</div></{el}>'

def head(kicker, h2, sub=''):
    s = f'<p>{sub}</p>' if sub else ''
    return f'<div class="section-head center reveal"><span class="kicker">{kicker}</span><h2>{h2}</h2>{s}</div>'

PAGES = {}

# ---------------- platform ----------------
PAGES['platform.html'] = page(
    'Platform — A Complete Cloud Business Phone | NPhones',
    'The NPhones platform delivers a complete business phone from the cloud: native dialing, messaging, app isolation, zero-trust access and central IT control.',
    'The platform', 'A complete phone. Running in the cloud.',
    'NPhones is not an app folder, a work profile or an MDM policy. It is an entire business phone — number, apps, contacts, files — running in the cloud and reached from the device your employees already carry.',
    section(
        head('Key capabilities', 'Everything a business phone does. Nothing installed.')
        + '<div class="grid-3">'
        + card('Native dialing', 'Make and receive calls on a dedicated business number — carrier-grade, not a softphone hack.')
        + card('SMS &amp; messaging', 'A separate work messaging channel, including WhatsApp Business, with full logging by policy.')
        + card('App isolation', 'Business apps run inside the cloud phone. Zero data ever touches the personal space.')
        + card('Zero-trust access', 'Every session is authenticated. Admins control access policies centrally, per user or group.')
        + card('End-to-end encryption', 'All communication encrypted in transit and at rest — only a display stream reaches the device.')
        + card('Cloud-native', 'No on-premise requirement, no hardware fleet. Deploy a workforce in minutes, globally.')
        + '</div>'
    )
    + section(
        head('Go deeper', 'The three pillars')
        + '<div class="grid-3">'
        + card('How it works', 'From console to pocket in four steps — provisioning, invite, sign-in, work.', '<a class="link-arrow" href="how-it-works.html">Explore →</a>')
        + card('Security architecture', 'Streaming-only delivery, isolation and governance designed for regulated industries.', '<a class="link-arrow" href="security.html">Explore →</a>')
        + card('Insights &amp; analytics', 'Business communication as a governed, analyzable enterprise data source.', '<a class="link-arrow" href="insights.html">Explore →</a>')
        + '</div>', 'section-tint'
    )
    + cta_strip('See the platform in action', 'A live deployment, from console to a working business phone, in one call.')
)

# ---------------- how it works ----------------
PAGES['how-it-works.html'] = page(
    'How It Works — NPhones',
    'How NPhones deploys a complete cloud business phone: create, invite, sign in, work. 30-second setup, one-click offboarding.',
    'How it works', 'From console to pocket in minutes.',
    'IT replaces phone logistics — boxes, SIMs, shipping, returns — with one cloud console.',
    section(
        '<div class="steps">'
        + card('01 · Create the phone', 'From the NPhones console, IT creates a cloud phone: number, apps, working hours and policies. Templates make the tenth phone faster than the first.')
        + card('02 · Send the invite', 'The employee gets an SMS with a secure install link. No box to ship, no SIM to activate, no waiting.')
        + card('03 · Sign in, done', 'They install a lightweight app — or use the browser — and sign in. The business phone is live in about 30 seconds.')
        + card('04 · Work, separated', 'Calls, WhatsApp Business, email and enterprise apps run on the business number, fully apart from personal life.')
        + '</div>'
        + '<div class="stats" style="margin-top:2.2rem">'
        + '<div class="glass stat reveal"><div class="num"><span data-count="30" data-suffix="s">0s</span></div><div class="lbl">Setup per employee</div></div>'
        + '<div class="glass stat reveal reveal-d1"><div class="num"><span data-count="0">0</span></div><div class="lbl">Traces on the device</div></div>'
        + '<div class="glass stat reveal reveal-d2"><div class="num"><span data-count="1">0</span></div><div class="lbl">Click to offboard</div></div>'
        + '</div>'
    )
    + section(
        head('Lifecycle', 'The whole employee lifecycle, handled')
        + '<div class="grid-3">'
        + card('Onboarding', 'New hire starts Monday? Their business phone is ready before their coffee. Contractors get access scoped to the project.')
        + card('Device change', 'Lost, broken or upgraded phone — the business phone lives in the cloud, so access moves with the user, not the hardware.')
        + card('Offboarding', 'One click revokes access. The number, contacts and every customer conversation stay with the company.')
        + '</div>', 'section-tint'
    )
    + cta_strip('Watch a live provisioning', 'We’ll create a cloud phone and hand it to you during the demo.')
)

# ---------------- security ----------------
PAGES['security.html'] = page(
    'Security — Zero Data on Device | NPhones',
    'NPhones security architecture: streaming-only delivery, complete isolation, zero-trust access, encryption in transit and at rest.',
    'Security', 'The phone your data never leaves.',
    'The entire business phone runs in the cloud. Only an encrypted display stream reaches the employee’s device — so there is nothing on the device to lose, steal or leak.',
    section(
        head('Architecture', 'Secure by construction, not by policy')
        + '<div class="grid-3">'
        + card('Streaming-only delivery', 'Apps, files and messages are rendered in the cloud and streamed as encrypted pixels. Company data is never stored on the personal device.')
        + card('Total isolation', 'The business phone and the personal phone share nothing: no storage, no clipboard by default, no contacts, no camera roll.')
        + card('Zero-trust sessions', 'Every connection is authenticated and policy-checked. Sessions can be limited by time, network, geography or role.')
        + card('Encryption everywhere', 'TLS in transit, AES at rest in the cloud environment. Keys managed per tenant.')
        + card('Central governance', 'Admins define app catalogs, availability hours, and data policies from one console — enforced in the cloud, not on the device.')
        + card('Instant revocation', 'Kill access in one click. Because nothing lives on the device, revocation is complete the moment it’s issued.')
        + '</div>'
    )
    + section(
        head('Deployment options', 'Your cloud, our cloud, on-prem')
        + '<div class="grid-3">'
        + card('Our cloud', 'Fastest path: fully managed NPhones cloud, deployed in minutes.')
        + card('Your cloud', 'Run the platform inside your own cloud tenancy for full data residency control.')
        + card('On-premises', 'For defense and critical infrastructure: the entire platform inside your perimeter.')
        + '</div>'
        + '<p class="reveal" style="margin:1.6rem auto 0;text-align:center;font-size:13.5px;color:rgba(8,8,8,.5);max-width:60ch">Compliance certifications are in progress — ask us for the current security documentation and audit roadmap.</p>',
        'section-tint'
    )
    + cta_strip('Talk to our security team', 'Architecture review, threat model and deployment options for your environment.')
)

# ---------------- insights ----------------
PAGES['insights.html'] = page(
    'Insights &amp; Analytics — NPhones',
    'NPhones turns business communication into a governed enterprise data source: aggregation, AI insights, audit and analytics.',
    'Intelligence layer', 'Your business calls. Finally visible to the business.',
    'Every call, message and WhatsApp thread on the business line is company property — loggable, auditable and analyzable. Data that used to walk around in employees’ pockets becomes an enterprise asset.',
    '''<section class="section section-dark" id="insights">
  <div class="blobs" aria-hidden="true">''' + blob('leaf', '0.05', 'width:420px;height:420px;top:-140px;left:-100px;') + blob('forest', '0.07', 'width:320px;height:320px;bottom:-100px;right:-80px;') + '''</div>
  <div class="section-inner">
    ''' + head('What you get', 'Four layers of visibility') + '''
    <div class="grid-4">
      ''' + card('One pipeline', 'Calls, SMS and messaging from every business line, aggregated into a single governed stream.')
        + card('AI insights', 'Deal signals, churn risk and service quality surfaced automatically from work conversations.')
        + card('Audit &amp; compliance', 'Full communication records for regulated teams — finance, healthcare, government — by policy, not by chance.')
        + card('Enterprise analytics', 'Response times, activity and coverage across the whole workforce — data that was simply invisible before.') + '''
    </div>
    <p class="reveal" style="margin:2rem auto 0;text-align:center;font-size:13.5px;color:rgba(247,247,245,.5);max-width:56ch">Scope: the business line only. Personal calls, apps and data on the device are never visible to the company.</p>
  </div>
</section>'''
    + section(
        head('Why it matters', 'From black box to dashboard')
        + '<div class="grid-3">'
        + card('For sales leaders', 'See which accounts go quiet before they churn. Keep every customer relationship when reps move on.')
        + card('For compliance officers', 'Prove who said what, when — with records that survive device changes and departures.')
        + card('For operations', 'Response-time and coverage metrics across field teams that used to be unmeasurable.')
        + '</div>', 'section-tint'
    )
    + cta_strip('See your communication as data', 'A demo of the insights console on realistic enterprise data.')
)

# ---------------- use-cases hub ----------------
UC_ICONS = {
    'sales': '<path d="M3 18v-6a9 9 0 0 1 18 0v6"/><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"/>',
    'field': '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
    'logistics': '<rect x="1" y="3" width="15" height="13" rx="2"/><path d="M16 8h4l3 3v5h-7V8z"/><circle cx="5.5" cy="18.5" r="2"/><circle cx="18.5" cy="18.5" r="2"/>',
    'contractors': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/>',
    'remote': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a15 15 0 0 1 0 18M12 3a15 15 0 0 0 0 18"/>',
    'government': '<path d="M12 3l8 4v5c0 5-3.5 8-8 9-4.5-1-8-4-8-9V7z"/><path d="M9 12l2 2 4-4"/>',
}
def uc_icon(key):
    return (f'<div class="icon-chip"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" '
            f'stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
            f'aria-hidden="true">{UC_ICONS[key]}</svg></div>')
def uc_card(href, title, text, icon):
    return (f'<div class="glass card reveal" data-tilt>{uc_icon(icon)}'
            f'<h3>{title}</h3><p style="margin-top:.5rem">{text}</p>'
            f'<a class="link-arrow" href="{href}">Explore →</a></div>')

PAGES['use-cases.html'] = page(
    'Use Cases — A Cloud Business Phone for Every Workforce | NPhones',
    'NPhones use cases: sales teams, field service, logistics, contractors, remote teams, government and defense.',
    'Use cases', 'Every workforce. One device.',
    'Not every employee works from a desk, and no organization wants to buy, ship and manage another physical phone. NPhones gives each user a complete business phone on the device they already have.',
    section(
        '<div class="grid-3">'
        + uc_card('uc-sales.html', 'Sales &amp; customer-facing teams', 'A dedicated business number, WhatsApp Business, CRM and contacts — without another device, and without losing the customer when the rep leaves.', 'sales')
        + uc_card('uc-field.html', 'Field service &amp; technicians', 'Work orders, service apps and a business camera roll for teams that live on the road, not at a desk.', 'field')
        + uc_card('uc-logistics.html', 'Delivery &amp; logistics', 'Connect drivers and couriers without exposing personal numbers or managing fleets of phones.', 'logistics')
        + uc_card('uc-contractors.html', 'Contractors &amp; temporary workers', 'A complete business phone for exactly as long as the project lasts — then one click removes it.', 'contractors')
        + uc_card('uc-remote.html', 'Remote &amp; global teams', 'A consistent business identity for distributed employees, wherever they work from.', 'remote')
        + uc_card('uc-government.html', 'Government &amp; defense', 'Managed mobile access for sensitive environments — with nothing stored on personal devices.', 'government')
        + '</div>'
    )
    + cta_strip('Which use case fits your organization?', 'Tell us about your workforce and we’ll map NPhones to it.')
)

# ---------------- use-case children ----------------
def uc_page(fname, title, desc, kicker, h1, sub, whofor, benefits, closing):
    chips = ''.join(f'<span class="chip">{w}</span>' for w in whofor)
    bl = ''.join(f'<li>{b}</li>' for b in benefits)
    body = section(
        head('Best for', 'Who this is built for')
        + f'<div class="chips reveal" style="justify-content:center">{chips}</div>'
    ) + section(
        head('Key benefits', 'What changes with NPhones')
        + f'<div class="glass card reveal" style="max-width:640px;margin-inline:auto"><ul class="check-list">{bl}</ul></div>',
        'section-tint'
    ) + cta_strip(closing, 'A live walkthrough mapped to your team, in 30 minutes.')
    PAGES[fname] = page(title, desc, kicker, h1, sub, body)

uc_page('uc-sales.html', 'Sales Teams — NPhones', 'Give every salesperson a dedicated business number, WhatsApp Business, CRM and contacts without another device.',
    'Use case · Sales', 'The customer stays with the company.',
    'Give every salesperson a dedicated business number, messaging, contacts and CRM access — and keep every customer relationship under company control when people move on.',
    ['Sales representatives', 'Account managers', 'Customer service', 'Recruiters', 'Real estate &amp; insurance agents'],
    ['Separate personal and business communication completely', 'Business contacts and WhatsApp threads stay company property', 'Define business availability hours — real work-life separation', 'Reassign a departing rep’s number and pipeline in one click', 'Consistent company identity on every customer touchpoint'],
    'Equip your sales team without buying a single phone')

uc_page('uc-field.html', 'Field Service — NPhones', 'Equip technicians and installers with a complete cloud business phone: service apps, work photos, business number.',
    'Use case · Field service', 'The office, in the field.',
    'Technicians, installers and inspectors get everything they need to communicate, document work and reach business systems — from one secure cloud phone on their own device.',
    ['Technicians', 'Installers', 'Maintenance teams', 'Field engineers', 'Inspectors'],
    ['Service, CRM and work-order apps in the business phone', 'A dedicated business number for customer contact', 'Work photos and files stay in the business environment', 'Onboard new field workers in minutes, not shipping cycles', 'Remove access remotely the moment a contract ends'],
    'Connect your field force this week')

uc_page('uc-logistics.html', 'Logistics &amp; Delivery — NPhones', 'Connect drivers and couriers without exposing personal numbers or managing device fleets.',
    'Use case · Logistics', 'Every driver connected. No fleet to manage.',
    'Drivers, couriers and distribution teams communicate with customers on business numbers — without a second device in every glovebox.',
    ['Drivers', 'Couriers', 'Delivery teams', 'Warehouse teams', 'Route managers'],
    ['Customer communication separated from personal life', 'Navigation and delivery apps inside the business phone', 'Proof-of-delivery workflows with the business camera', 'Activate workers across locations instantly', 'Cut device purchasing and replacement costs to zero'],
    'Put a business phone in every cab — without the phone')

uc_page('uc-contractors.html', 'Contractors &amp; Temp Workers — NPhones', 'Controlled business phone access for contractors and temporary workers, for exactly as long as needed.',
    'Use case · Contractors', 'Access for the project. Not forever.',
    'Provide contractors and seasonal workers with a complete business phone for exactly as long as they need it — then remove it in one click, with all company data intact.',
    ['Contractors', 'Freelancers', 'Seasonal workers', 'Outsourced teams', 'Project-based teams'],
    ['No phones purchased for 3-month engagements', 'Access activated the morning the project starts', 'Access removed the minute the work ends', 'Company data never leaves the business environment', 'Onboarding and offboarding become a checkbox, not a process'],
    'Stop buying phones for temporary people')

uc_page('uc-remote.html', 'Remote &amp; Global Teams — NPhones', 'A consistent business identity for distributed and international teams, accessible anywhere.',
    'Use case · Remote &amp; global', 'One business identity. Any location.',
    'Distributed employees get the same business phone wherever they operate — no locally shipped hardware, no number chaos across borders.',
    ['Remote employees', 'Hybrid teams', 'International teams', 'Traveling executives', 'Distributed support teams'],
    ['The same business phone from any location or device', 'No dependency on locally supplied hardware', 'Consistent business number across borders', 'International onboarding in minutes', 'Personal and business activity fully separate'],
    'Give your global team one identity')

uc_page('uc-government.html', 'Government &amp; Defense — NPhones', 'Managed mobile access for public sector and defense: nothing stored on personal devices, full central control.',
    'Use case · Government &amp; defense', 'Sensitive work. Zero device risk.',
    'Public-sector and defense organizations provide controlled mobile access to employees and contractors — while operational data never touches a personal device.',
    ['Federal &amp; state agencies', 'Municipalities', 'Defense organizations', 'Critical infrastructure', 'Emergency response'],
    ['Operational data remains inside the governed environment', 'Complete separation of official and personal activity', 'Temporary and emergency personnel activated in minutes', 'Remote revocation with nothing left behind', 'On-premises deployment available for closed networks'],
    'Discuss a secure deployment')

# ---------------- pricing ----------------
PAGES['pricing.html'] = page(
    'Pricing — NPhones',
    'NPhones pricing: one per-user subscription replaces the device, the plan, the MDM seat and the logistics. Get a custom quote.',
    'Pricing', 'One subscription. Zero hardware.',
    'A corporate phone means the device, the plan, the MDM seat, the IT hours — then replacement, repair and recovery. NPhones replaces the whole stack with one per-user subscription.',
    section(
        '<div class="grid-2">'
        + card('The old way', 'Device purchase + carrier plan + MDM licence + shipping + IT provisioning time + a replacement cycle every 2–3 years — <strong>per employee, forever</strong>. And when someone leaves, the number and WhatsApp history often leave too.')
        + card('The NPhones way', 'One per-user subscription. No hardware, no logistics, no MDM stack, nothing to replace. Onboarding in 30 seconds, offboarding in one click, the business line stays yours. <strong>Save thousands per employee, every year.</strong>')
        + '</div>'
    )
    + section(
        head('What’s included', 'Every seat gets the full phone')
        + '<div class="grid-3">'
        + card('The complete cloud phone', 'Dedicated business number, calls, SMS, WhatsApp Business, email and your enterprise apps.')
        + card('The admin console', 'Provisioning, policies, templates, audit logs and one-click offboarding for IT.')
        + card('Support &amp; onboarding', 'Guided rollout, admin training and support included — no professional-services surprise.')
        + '</div>', 'section-tint'
    )
    + section(
        head('Questions', 'The short version')
        + '<div class="grid-3">'
        + card('How is it priced?', 'Per user, per month, with volume tiers. Through telecom partners or directly — we’ll route you to the best option for your region.')
        + card('Minimum seats?', 'Pilots start small. Bring one team — sales, field, or contractors — and expand when the math proves itself.')
        + card('What about iOS?', 'Android today; iOS is on the roadmap. Mixed fleets can start with their Android population now.')
        + '</div>'
    )
    + cta_strip('Get a custom quote', 'Tell us your workforce size and we’ll show you the per-user math against your current device costs.', 'Get a custom quote')
)

# ---------------- partners ----------------
PAGES['partners.html'] = page(
    'Partners — NPhones',
    'Partner with NPhones: telecom operators, white-label distributors and strategic partners. Three tracks, dedicated teams.',
    'Partnerships', 'Build the next mobile category with us.',
    'Three partnership tracks for telecom operators, white-label distributors and strategic partners. Each has a dedicated team, commercial model and onboarding path.',
    section(
        '<div class="grid-3">'
        + card('Telecom', 'For Tier-1 operators &amp; MVNOs. White-label second-line service, wholesale per-user pricing, billing &amp; OSS API integration, carrier-grade SLAs, joint go-to-market.', '<a class="link-arrow" href="contact.html">Apply for this track →</a>')
        + card('White-label', 'For distributors, OEMs &amp; publishers. Full brand customization, scalable provisioning, an admin console under your brand, global distribution playbook.', '<a class="link-arrow" href="contact.html">Apply for this track →</a>')
        + card('Collaboration', 'For SIs, defense primes &amp; tech partners. Co-development, channel reselling, government &amp; defense programs, revenue sharing.', '<a class="link-arrow" href="contact.html">Apply for this track →</a>')
        + '</div>'
    )
    + section(
        head('Why partner', 'Monetize identities, not SIM cards')
        + '<div class="grid-3">'
        + card('A new revenue line', 'Sell complete business phones on top of your existing infrastructure — no devices, no logistics, high margin.')
        + card('Your brand, our platform', 'White-label everything: app, console, domain. Your customers never leave your ecosystem.')
        + card('Enterprise pull', 'BYOD security and device-cost pressure are board-level topics. NPhones answers both in one product.')
        + '</div>', 'section-tint'
    )
    + cta_strip('Tell us about your business', 'Share a few details and our partnerships team will reach out with a tailored proposal.', 'Start the conversation')
)

# ---------------- about ----------------
def team(name, role, bio, img=None):
    if img:
        avatar = (f'<div class="tphone"><div class="tscreen">'
                  f'<img src="assets/team/{img}.webp" alt="{name}" loading="lazy">'
                  f'</div></div>')
    else:
        avatar = ('<div class="tphone"><div class="tscreen" style="height:148px;display:flex;align-items:center;justify-content:center">'
                  '<svg width="56" height="70" viewBox="0 0 102 130" aria-hidden="true">'
                  '<rect x="10" y="10" width="50" height="78" rx="16" fill="#B9E7DE"/>'
                  '<rect x="24" y="24" width="52" height="82" rx="16" fill="#15B097"/>'
                  '<rect x="38" y="40" width="54" height="86" rx="16" fill="#0B6B5C"/>'
                  '<rect x="46" y="50" width="38" height="66" rx="8" fill="#F4F6F5"/></svg>'
                  '</div></div>')
    return (f'<div class="glass card team-card reveal" data-tilt>{avatar}'
            f'<h3>{name}</h3><span class="team-role">{role}</span>'
            f'<p style="margin-top:.6rem">{bio}</p></div>')

PAGES['about.html'] = page(
    'About — Team &amp; Mission | NPhones',
    'NPhones is building the cloud business phone: one device, many identities. Meet the team.',
    'About', 'One device. Many identities. Zero compromise.',
    'For decades the mobile industry forced a choice: one identity per device, or carry two phones. NPhones eliminates that trade-off with a cloud business phone any enterprise, operator or government can deploy.',
    section(
        head('Our vision', 'The second phone disappears')
        + '<div class="grid-3">'
        + card('Identity, not hardware', 'Just as the cloud redefined computing, NPhones decouples the phone from the device — turning every device into many.')
        + card('Carrier-grade scale', 'Designed from day one to run on telecom infrastructure worldwide, bringing secure business phones to millions of users.')
        + card('Security as a default', 'Isolation, compliance and zero-trust built into the platform’s fabric — not bolted on.')
        + '</div>'
    )
    + section(
        head('The people behind NPhones', 'A team built for telecom-scale ambition')
        + '<div class="grid-3">'
        + team('Tamir Fridman', 'CEO', '16+ years scaling B2B SaaS. Former exec at Similarweb, ZoomInfo, NYSE/ICE and Spot by NetApp.', 'tamir')
        + team('Arieh Ben Harush', 'Founder &amp; CTO', 'Serial entrepreneur with two decades in telecom, mobile security and large-scale infrastructure.', 'arieh')
        + team('Tali Freeman Shalev', 'Strategic Business Development', 'Global business development leader across telecom and enterprise partnerships.', 'tali')
        + team('Chen Altshuler', 'Senior Business Advisor', 'Business strategy expert in fundraising and scaling startups from concept to commercial scale.', 'chen')
        + team('Yair Shagi', 'Security Sector Lead — Defense', 'Former Deputy Head of the Israeli Security Agency (Shin Bet). 25+ years of national security leadership.', 'yair')
        + team('The engineering team', 'Cyber &amp; Telecom', 'Cyber-security and telecommunications veterans building the infrastructure layer of the next mobile category.')
        + '</div>', 'section-tint'
    )
    + section(
        head('Footprint', 'A greener mobile workforce')
        + '<div class="glass card reveal" style="max-width:640px;margin-inline:auto"><p>Every second device that isn’t manufactured, shipped and charged saves battery production, power and e-waste. It’s not why you’ll buy NPhones — but it’s a number your sustainability report will like. Ask us for the per-seat estimate methodology.</p></div>'
    )
    + cta_strip('Join our journey', 'Telecom alliances, strategic investment, or your first deployment — start a conversation.', 'Start a conversation')
)

# ---------------- contact ----------------
PAGES['contact.html'] = page(
    'Contact — Request a Demo | NPhones',
    'Request an NPhones demo or contact the team. We reply within 24 hours.',
    'Contact', 'Let’s put your phones on one device.',
    'Tell us about your workforce and we’ll show you a live NPhones deployment — from console to a working business phone in minutes. We reply within 24 hours.',
    '''<section class="section section-forest cta-panel" id="demo">
  <div class="blobs" aria-hidden="true">''' + blob('leaf', '0.05', 'width:400px;height:400px;top:-120px;right:-90px;') + blob('sage', '0.035', 'width:300px;height:300px;bottom:-90px;left:-60px;') + '''</div>
  <div class="section-inner">
    <span class="kicker">Request a demo</span>
    <h2 style="max-width:22ch;margin-inline:auto">Give your team their phones. On one device.</h2>
    <form class="glass cta-form" data-static>
      <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px" aria-hidden="true">
      <input type="text" name="name" placeholder="Full name *" aria-label="Full name" required>
      <input type="email" name="email" placeholder="Work email *" aria-label="Work email" required>
      <textarea name="message" placeholder="Tell us about your workforce (optional)" aria-label="Message" class="full"></textarea>
      <button class="btn btn-light full" type="submit">Request a demo</button>
    </form>
    <p class="form-note">We reply within 24 hours. Android today, iOS on the roadmap.</p>
    <p style="margin:1.6rem auto 0;text-align:center;font-size:14px;color:rgba(247,247,245,.7)">Prefer email? <a href="mailto:contact@nphones.com" style="color:var(--sage);font-weight:600">contact@nphones.com</a></p>
  </div>
</section>'''
    + section(
        head('What happens next', 'Three steps, no maze')
        + '<div class="grid-3">'
        + card('1 · Intro call', 'Thirty minutes on your workforce, device costs and security requirements.')
        + card('2 · Live demo', 'We provision a cloud phone in front of you and hand you the keys.')
        + card('3 · Pilot', 'One team, real usage, real numbers — then decide with data.')
        + '</div>', 'section-tint'
    ),
    cta_href='#demo'
)

# ---------------- legal placeholders ----------------
def legal(fname, title, h1):
    PAGES[fname] = page(
        f'{title} — NPhones', f'NPhones {title.lower()}.', 'Legal', h1,
        'Placeholder — replace with final counsel-approved text before launch.',
        section(
            '<div class="glass card reveal" style="max-width:720px;margin-inline:auto"><p>This page is a structural placeholder created during the website redesign. Before launch, insert the final ' + title.lower() + ' covering data processing, cookies, user rights (GDPR/CCPA), retention, and contact details for the data controller.</p><p style="margin-top:.8rem">NPhones Ltd · Beer Sheva, Israel · <a href="mailto:contact@nphones.com" style="color:var(--forest);font-weight:600">contact@nphones.com</a></p></div>'
        )
    )
legal('privacy.html', 'Privacy Policy', 'Privacy policy.')
legal('terms.html', 'Terms of Service', 'Terms of service.')

outdir = os.path.dirname(os.path.abspath(__file__))
for fname, html in PAGES.items():
    with open(os.path.join(outdir, fname), 'w') as f:
        f.write(html)
    print('wrote', fname)
print(f'{len(PAGES)} pages generated')
