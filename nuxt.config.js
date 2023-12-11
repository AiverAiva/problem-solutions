export default {
  // Target: https://go.nuxtjs.dev/config-target
  target: "static",

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: "Problem Solutions",
    link: [{ rel: "icon", type: "image/svg+xml", href: "/icon.svg" }],
    script: [
      process.env.NODE_ENV === "production"
        ? {
            src: "https://umami-zernonia.vercel.app/umami.js",
            async: true,
            defer: true,
            "data-website-id": "3616ea01-95e5-4770-b4ee-7c15911e941a",
          }
        : {},
    ],
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: ["~/assets/main.css"],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/typescript
    "@nuxt/typescript-build",
    "nuxt-windicss",
    ["unplugin-icons/nuxt"],
    "@nuxtjs/composition-api/module",
    "@nuxtjs/google-fonts",
    "nuxt-vite",
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/pwa
    "@nuxtjs/pwa",
    // https://go.nuxtjs.dev/content
    "@nuxt/content",
    "@nuxtjs/sitemap",
  ],

  // PWA module configuration: https://go.nuxtjs.dev/pwa
  pwa: {
    manifest: {
      lang: "en",
    },
    icon: false,
  },

  generate: { fallback: "404.html" },

  sitemap: {
    hostname: "https://solutions.weikuwu.me/",
    gzip: true,
    routes: async () => {
      let routes = [];
      let problems = [];
      const { $content } = require("@nuxt/content");
      if (problems === null || problems.length === 0)
        problems = await $content("problems").fetch();
      for (const problem of problems) {
        routes.push(`/${problem.slug}`);
      }
      return routes;
    },
  },

  // Content module configuration: https://go.nuxtjs.dev/config-content
  content: {
    fullTextSearchFields: () => ["title", "description"],
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    extend(config) {
      config.module.rules.push({
        test: /\.mjs$/,
        include: /node_modules/,
        type: "javascript/auto",
      });
    },
  },

  googleFonts: {
    display: 'swap',
    families: {
      Inter: [400, 600, 700],
      "DM Mono": true,
    },
  },
};
