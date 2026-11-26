# TAYP Foundation

Website for [TAYP Foundation Inc.](https://taypfoundation.com), a Georgia nonprofit. The site is a static [Astro](https://astro.build) build. Netlify builds it from GitHub using `netlify.toml`. No environment variables or secrets are required.

## Develop

Requires Node.js 22.

```bash
npm install
npm run dev
```

## Build

```bash
npm run build
```

The publish directory is `dist/`.

## Forms

The contact form (`contact`) and the sponsorship inquiry (`sponsor`) are Netlify Forms with a honeypot field. After the first production deploy, confirm both forms appear under Forms in the Netlify site settings. Submissions can be emailed to `support@taypfoundation.org` from that screen.

## Brand images

`public/brand`, the favicon, and `public/og.jpg` are web-sized derivatives of the official logo. `scripts/optimize-brand.py` rebuilds them when the master artwork is available locally.
