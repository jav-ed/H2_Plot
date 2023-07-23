/** @type {import('tailwindcss').Config} */


const defaultTheme = require("tailwindcss/defaultTheme");

module.exports = {
  content: ["./src/**/*.{astro,html,md, mdx,js,jsx,svelte,ts,tsx,vue}"],

  /* --------------------------------- theme -------------------------------- */
  theme: {
    extend: {

      /* --------------------------- theme extend --------------------------- */
      fontFamily: {
        sans: ["InterVariable", ...defaultTheme.fontFamily.sans],
      },
      colors: {
        primary: "var(--color-primary)",
        secondary: "var(--color-secondary)",
      },
      textColor: {
        default: "var(--color-text)",
        offset: "var(--color-text-offset)",
      },
      backgroundColor: {
        default: "var(--color-background)",
        offset: "var(--color-background-offset)",
      },
      borderColor: {
        default: "var(--color-border)",
      },

      /* --------------------------- theme extend --------------------------- */
      typography: {
        DEFAULT: {
          css: {
            // '--tw-prose-body': 'var(--tw-prose-invert-body)',
            // '--tw-prose-headings': 'var(--tw-prose-invert-headings)',
            '--tw-prose-body': 'var(--shiny_White)',
            '--tw-prose-headings': 'var(--cl_Neon_Green)',
            '--tw-prose-lead': 'var(--tw-prose-invert-lead)',
            '--tw-prose-links': 'var(--tw-prose-invert-links)',
            '--tw-prose-bold': 'var(--tw-prose-invert-bold)',
            '--tw-prose-counters': 'var(--tw-prose-invert-counters)',
            '--tw-prose-bullets': 'var(--tw-prose-invert-bullets)',
            '--tw-prose-hr': 'var(--tw-prose-invert-hr)',
            '--tw-prose-quotes': 'var(--tw-prose-invert-quotes)',
            '--tw-prose-quote-borders': 'var(--tw-prose-invert-quote-borders)',
            '--tw-prose-captions': 'var(--tw-prose-invert-captions)',
            '--tw-prose-code': 'var(--tw-prose-invert-code)',
            '--tw-prose-pre-code': 'var(--tw-prose-invert-pre-code)',
            '--tw-prose-pre-bg': 'var(--tw-prose-invert-pre-bg)',
            '--tw-prose-th-borders': 'var(--tw-prose-invert-th-borders)',
            '--tw-prose-td-borders': 'var(--tw-prose-invert-td-borders)',
          },
        },
      },

    },

  darkMode: 'media',

  },


  corePlugins: {
    fontSize: false,

    // If this is activated margins will be set to 0, see:
    // https://tailwindcss.com/docs/preflight
    // default bahaviour is: true
    // preflight: true, // this disables preflight
  },

  plugins: [
    require("tailwindcss-fluid-type"),
    require("@tailwindcss/typography"),
    require("daisyui")
    
],



  daisyui: {
    // themes: false, // disable all themes
    themes: ["", 
            // "light", "dark", "cupcake"
            ],
    },



};



