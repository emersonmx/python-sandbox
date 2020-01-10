const mix = require('laravel-mix');

const purgecss = require('@fullhuman/postcss-purgecss');

mix.disableNotifications();
mix.setPublicPath('taskr/static');

mix.js('src/taskr/main.js', 'taskr');
mix.postCss('src/taskr/main.css', 'taskr', [
    require('postcss-import'),
    require('postcss-nested'),
    require('postcss-simple-vars'),
    require('tailwindcss'),
    require('autoprefixer'),
    ...(mix.inProduction()
        ? [purgecss({ content: ['./taskr/templates/**/*.html'] })]
        : []),
]);

if (mix.inProduction()) {
    mix.version();
}
