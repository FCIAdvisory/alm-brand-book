# ALM Services — Brand & Web Program

Client studio for ALM Services (Airport Logistics Management).

**Start here:** https://fciadvisory.github.io/alm-brand-book/ — the studio dashboard linking to every deliverable.

| Deliverable | URL |
| --- | --- |
| Studio dashboard | https://fciadvisory.github.io/alm-brand-book/ |
| Brand book (ALM-BS-001, v3) | https://fciadvisory.github.io/alm-brand-book/brand-book/ |
| Website concept (draft 1) | https://fciadvisory.github.io/alm-brand-book/website/ |
| Brand book, single file | `brand-book.html` (download; images embedded) |

**Accent previews** (the one open brand decision): [All Blue](https://fciadvisory.github.io/alm-brand-book/brand-book/?accent=sky) · [Sunrise Orange](https://fciadvisory.github.io/alm-brand-book/brand-book/?accent=sunrise) · [Brick Red](https://fciadvisory.github.io/alm-brand-book/brand-book/?accent=brick) — also works on the website concept with the same `?accent=` parameter.

## Repo layout

- `index.html` — studio dashboard (the front page)
- `brand-book/index.html` — brand standards (source of truth)
- `website/index.html` — website concept
- `assets/` — shared imagery & logos
- `scripts/build-single.py` — regenerates `brand-book.html` (self-contained) from `brand-book/index.html`
- `site-archive/` — original almservices.com scrape (local only, gitignored)

`?noanim` on any page disables entrance animations (useful for print/PDF capture).
