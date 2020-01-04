const mix = require('laravel-mix');

const purgecss = require('@fullhuman/postcss-purgecss');

mix.disableNotifications();
mix.setPublicPath('app/static');

mix.js('src/app/main.js', 'app');
mix.postCss('src/app/main.css', 'app', [
    require('postcss-import'),
    require('postcss-nested'),
    require('postcss-simple-vars'),
    require('tailwindcss'),
    require('autoprefixer'),
    ...(mix.inProduction()
        ? [purgecss({ content: ['./dist/**/*.html'] })]
        : []),
]);

if (mix.inProduction()) {
    mix.version();
}
