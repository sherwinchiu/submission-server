// js/markdoc-render.js

const Markdoc = require('@markdoc/markdoc');

const source = '# Markdoc';

const ast = Markdoc.parse(source);
const content = Markdoc.transform(ast, /* config */);

const html = Markdoc.renderers.html(content);

console.log(html);