import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";

export default defineConfig({
  site: "https://taypfoundation.com",
  trailingSlash: "always",
  build: {
    inlineStylesheets: "never",
  },
  vite: {
    build: {
      // Keep page scripts as files so the site CSP can stay script-src 'self'.
      assetsInlineLimit: 0,
    },
  },
  integrations: [
    sitemap({
      filter: (page) => !page.includes("/thank-you"),
    }),
  ],
});
