# NPhones — website v1

Redesigned marketing site for [NPhones](https://nphones.com) — cloud business phones for enterprises.
Static site: no build step, no dependencies. Open `index.html` or serve the folder.

## Structure
- `index.html` — homepage (typewriter hero, scroll-scrubbed video, glass design system)
- `demo.html` — interactive Android → NPhones OS demo
- `platform / how-it-works / security / insights` — platform cluster
- `use-cases.html` + `uc-*.html` — use-case hub and children
- `pricing / partners / about / contact` — commercial & company pages
- `assets/style.css` — design system (brand tokens, glassmorphism, blobs, buttons)
- `assets/main.js` — typewriter, cursor-reactive blobs, scroll animations, cursor orbit, video scrub
- `build_pages.py` — regenerates all subpages from a shared template (`python3 build_pages.py`)

## Before launch
- Wire the demo/contact forms to a real endpoint (they're static placeholders)
- Replace `privacy.html` / `terms.html` placeholder text with counsel-approved copy
- License Conthrax webfont (currently loaded from a third-party CDN copy)
- 301 redirects from old URLs: `/solutions → /use-cases`, `/company → /about`, old `/pricing → /partners`
