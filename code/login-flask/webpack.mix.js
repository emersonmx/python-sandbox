const mix = require('laravel-mix');

const purgecss = require('@fullhuman/postcss-purgecss');

mix.setPublicPath('app/static');

mix.js('src/frontend/main.js', 'frontend');
mix.postCss('src/frontend/main.css', 'frontend', [
    require('postcss-import'),
    require('postcss-nested'),
    require('postcss-simple-vars'),
    require('tailwindcss'),
    require('autoprefixer'),
    ...(mix.inProduction()
        ? [purgecss({ content: ['./app/templates/**/*.html'] })]
        : []),
]);

if (mix.inProduction()) {
    mix.version();
}
