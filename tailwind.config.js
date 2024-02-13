/** @type {import('tailwindcss').Config} */
module.exports = {
  content: {
  relative: true,
  files: [
    "./src/**/*.html,js",
    "./node_modules/flowbite/**/*.js",
    "./src/**/forms.py",
  ]
  },
  theme: {
    extend: {},
  },
  plugins: [
      require('flowbite/plugin')
  ]
}
