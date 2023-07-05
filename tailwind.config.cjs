/** @type {import('tailwindcss').Config} */


const defaultTheme = require("tailwindcss/defaultTheme");

module.exports = {
  content: ["./src/**/*.{astro,html,md, mdx,js,jsx,svelte,ts,tsx,vue}"],

  /* --------------------------------- theme -------------------------------- */
  theme: {
    extend: {
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
    },

  // darkMode: 'class',

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
],
};



