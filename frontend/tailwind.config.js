/** @type {import('tailwindcss').Config} */

export default {
  content: [
      "./src/**/*.{html,js,ts,tsx,jsx,tsx}",
      "./index.html",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
  corePlugins: {
    preflight: false,
  },
}

