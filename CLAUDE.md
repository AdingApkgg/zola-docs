# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Bilingual (Chinese primary, English secondary) translation of the official Zola static site generator documentation. Live at https://zola.docs.saop.cc/.

## Build & Development Commands

```bash
zola serve              # Local dev server (default: http://127.0.0.1:1111/)
zola build              # Production build → public/
zola check --skip-external-links  # Validate internal links
```

Requires Zola v0.22.1. The `build.sh` script handles auto-downloading Zola on Linux for Cloudflare Pages deploys.

## Content & Language Convention

- Default language: `zh` (Chinese). Secondary: `en` (English).
- Chinese content: `filename.md`. English: `filename.en.md`. Both live in the same directory.
- UI strings are translated via `trans()` calls in templates, with keys defined in `config.toml` under `[languages.zh.translations]` and `[languages.en.translations]`.
- `scripts/sync_check.py` compares local `.en.md` files against upstream getzola/zola to detect out-of-sync translations.

## Template Architecture

Tera template engine. Inheritance chain:

```
index.html              ← Base layout (header, footer, Swup, analytics, SEO)
├── documentation.html  ← Docs with sidebar navigation
│   └── page.html       ← Individual doc pages
├── themes.html         ← Theme gallery
│   └── theme.html      ← Individual theme page
├── search.html         ← Full-text search (Fuse.js)
├── comments.html       ← Artalk comment system
└── 404.html
```

Key blocks: `{% block title %}`, `{% block head %}`, `{% block content %}`, `{% block extra_content_class %}`.

## Client-Side Architecture

Page transitions managed by **Swup v4** (replaces full page reloads with AJAX navigation):
- Container: `<div id="swup">` in `index.html`
- Plugins: HeadPlugin, PreloadPlugin, ScrollPlugin, FadeTheme, A11yPlugin, ProgressPlugin
- All JS files in `static/js/swup*.js` (UMD builds from jsDelivr)

**Event system** — use DOM events for lifecycle hooks:
- `swup:page:view` — after page content is rendered (equivalent to DOMContentLoaded for navigated pages)
- `swup:visit:start` — before navigation begins (use for cleanup)
- Initial page load is NOT covered by swup events; call init functions directly.

Pattern used across `search.js` and `comments.html`:
```js
initSomething();                                    // initial load
document.addEventListener("swup:page:view", initSomething);  // subsequent navigations
```

## External Services

- **Artalk** (comments): `artalk.saop.cc` — config in `comments.html`
- **Analytics**: `bsz.saop.cc/api` — page/site view counts in footer
- **IndexNow**: `scripts/submit_indexnow.py` submits URLs to Bing after deploy

## Sass Structure

Entry point: `sass/site.scss` imports partials (`_base`, `_layout`, `_header`, `_docs`, `_search`, `_themes`, `_index`, `_pattern`, `_normalize`). Dark theme by default (#191919), with `prefers-color-scheme: light` overrides. Syntax highlighting: catppuccin-mocha.

## Deployment

- **Primary**: Cloudflare Pages via `build.sh` + `wrangler.toml`
- **Secondary**: GitHub Pages via `.github/workflows/docs.yml` (pushes to `gh-pages` branch, then runs IndexNow submission)
