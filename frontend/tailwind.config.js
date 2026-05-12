/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'primary-red': '#C1121F',
        'dark-red': '#780000',
        'light-gray': '#F5F5F5',
        'white': '#FFFFFF',
      },
      fontFamily: {
        'sans': ['AnthorpicSerif', 'serif'],
      }
    },
  },
  plugins: [],
}
