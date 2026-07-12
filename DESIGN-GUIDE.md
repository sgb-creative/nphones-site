# NPhones Design Guide

The single source of truth for NPhones brand and web design. Use it to keep marketing materials, presentations and product surfaces consistent with nphones.com.

---

## 1. Brand core

**Wordmark:** NPhones (capital N, capital P) — always set in **Conthrax SemiBold**. Conthrax is used *nowhere else*.
**Icon:** three stacked phones (light → accent → dark, white screen) on a rounded tile. Never redraw; scale from `assets/favicon.svg`.
**Tagline:** *One device, Ndless phones.* Use as a signature, not body copy.

## 2. Color

| Role | Name | Hex | Usage |
|---|---|---|---|
| Text / dark surfaces | Ink | `#080808` | Headlines, body, dark sections, footer |
| Page background | Paper | `#F7F7F5` | Default page/base |
| Warm neutral | Cream | `#F1EFEA` | Alternating warm sections, subtle tints |
| Neutral tint | Gray-sage | `#D5DAD8` | Blobs, dividers, quiet fills |
| **Accent** | **Teal** | **`#15B097`** | CTAs, links, highlights, glows — the only color |
| Accent dark | Deep teal | `#0E7A69` | Accent text on light backgrounds (AA-safe), icon strokes |
| Accent tint | Teal mist | `#B9E7DE` | Light accent fills, icon back layers |

Rules: the site is black-and-white; **teal is scarce on purpose** — CTAs, key data, interactive states. Never use teal for body text or large surfaces. Accent text on light backgrounds uses Deep teal, not Teal (contrast).

## 3. Typography

**Inter** everywhere. Weights: 300 body, 400 UI text, 600 subheads/labels/buttons, 700 H1–H2.
Headings: `font-weight: 700; letter-spacing: -0.02em; line-height ~1.14`. Body: 17px / 1.65. Buttons: 15px / 600, sentence case (no uppercase).
**Conthrax appears only in the logo wordmark.** Never in headings, buttons or labels.

## 4. Layout

Full-width sections stacked edge-to-edge (no floating islands, no side gutters on sections). Content constrained inside via `.section-inner` padding (max ~1240px). Section rhythm alternates cool (white→Paper) and warm (white→Cream) automatically; dark Ink sections punctuate (intelligence, footer, CTA panels).
Cards and controls stay rounded: cards 24px, buttons 14px, pills for chips/inputs. Sections themselves are square (full-bleed).

## 5. Glass & atmosphere

Glass recipe: `rgba(255,255,255,.55)` + `backdrop-filter: blur(16px) saturate(160%)` + 1px `rgba(10,10,10,.14)` border + soft neutral shadow. Dark sections: `rgba(255,255,255,.06)` + white 12% border.
Blobs: large blurred circles (blur ~70px) in Gray-sage / Teal / Deep-teal / Cream, drifting slowly (16–24s) and shifting subtly toward the cursor. Neutral first; one teal blob per section maximum.

## 6. Buttons

Flat translucent glass, crisp 1.5px border, soft halo below in the fill color.
- **Primary:** teal glass fill (`rgba(21,176,151,.38)`), Ink-teal text `#063B33`.
- **Secondary:** near-clear warm glass, Deep teal text.
- **Disabled:** gray glass, no interactions.
States: hover = washed lighter + lift + breathing gradient (teal/neutral radials drifting, 4.5s alternate); press = squish (scale .965) + deeper fill. No color-only state changes.

## 7. Motion

- Sections animate in **and out** on scroll (lift + fade, spring ease, ~0.75s).
- Hero H1 types itself; homepage cycles "Your first… second… third… phones / On one device." — subpages type their headline once.
- Desktop scrolling glides via Lenis (`lerp 0.075`, wheel ×0.85); phones keep native scroll.
- Cursor orbit: the tagline circles at bottom-right (120px), one rotation / 20s, accelerating near interactive elements.
- Everything respects `prefers-reduced-motion`; content is never gated on JS.

## 8. Voice (summary)

Professional, direct, concrete; short declarative sentences; every claim followed by its mechanism. The product is a **cloud business phone** (never "virtual phone", "work profile", "second line"). No exclamation points, no "revolutionary". Numbers only when defensible.

## 9. Assets

- `assets/favicon.svg` — master icon (vector)
- `assets/style.css` — all tokens as CSS custom properties (`:root`)
- `assets/team/*.webp` — team headshots (optimized)
- `assets/media/deploy.mp4` — product video
- `build_pages.py` — page generator; edit template once, regenerate all pages

## 10. Do / Don't

**Do:** lots of white space · one teal moment per view · glass over blobs · rounded cards · sentence case.
**Don't:** green (legacy palette) · Conthrax outside the logo · uppercase button labels · more than one accent color · flat solid-teal surfaces · content hidden until animation.
