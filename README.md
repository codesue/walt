# walt

[![License][license_badge]][license_link]
[![npm][npm_badge]][npm_link]
[![PyPI][pypi_badge]][pypi_link]
[![Repo Size][repo_size_badge]][repo_size_link]
[![Docs][docs_badge]][docs_link]

Walt is a minimal documentation theme based on [writ.css](https://writ.cmcenroe.me).
It features classless styles for semantic HTML and supports light and dark mode
based on system settings.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/images/mkdocs-walt-dark.png" />
  <img src="assets/images/mkdocs-walt-light.png" alt="Screenshot of the Walt website" />
</picture>

## Stylesheet

You can include the Walt stylesheet in your project in the following ways:

- Copy the stylesheet from GitHub:

  https://github.com/codesue/walt/blob/main/walt.css

- Install from npm:

  ```sh
  npm install --save walt.css
  ```

- Link to a CDN:

  ```html
  <link rel="stylesheet" href="https://unpkg.com/walt.css/walt.css" />
  ```

### Code syntax highlighting

For code syntax highlighting in Walt, I recommend using [highlight.js](https://github.com/highlightjs/highlight.js) with [Catppuccin palettes](https://github.com/catppuccin/highlightjs).
Use Macchiato for the dark color scheme and Latte for the light color scheme.
For example, you may add the following to your HTML files:

```html
<link rel="stylesheet" href="//unpkg.com/@catppuccin/highlightjs/css/catppuccin-macchiato.css" media="(prefers-color-scheme: dark)">
<link rel="stylesheet" href="//unpkg.com/@catppuccin/highlightjs/css/catppuccin-latte.css" media="(prefers-color-scheme: light)">
```

In a stylesheet or style tag, unset the background in code blocks styled by
highlight.js to maintain uniform background colors in code blocks and inline code:

```css
.hljs,
code.hljs {
  background: unset;
}
```

You may also want to update the text color of comments if they no longer have enough
contrast with their backgrounds:

```css
code .hljs-comment {
  color: var(--color-secondary-text);
}
```
## MkDocs theme

Walt is available as an MkDocs theme that features:

- classless styles for semantic HTML based on [writ.css](https://writ.cmcenroe.me)
- light mode and dark mode based on system settings
- an emoji favicon for browsers that support svg site icons
- code syntax highlighting using highlight.js

You can install it from PyPI using:

```sh
pip install mkdocs-walt
```

See the [`mkdocs`](https://github.com/codesue/walt/blob/main/mkdocs)
directory to learn how to install and use Walt in your MkDocs projects.

## Contributing

Coming soon!

## License

Copyright &copy; 2023 [Suzen Fylke](https://suzenfylke.com). Distributed under the MIT License.

## Acknowledgements

Walt uses [writ.css](https://github.com/programble/writ/) for styles
and examples use [writ's reference html page](https://github.com/programble/writ/blob/master/reference.html).

Walt also uses [Catppuccin](https://github.com/catppuccin/catppuccin) for code
block syntax highlighting and dark mode color palettes.

[docs_badge]: https://img.shields.io/github/actions/workflow/status/codesue/walt/publish-docs.yml?label=docs&colorA=363a4f&colorB=b7bdf8&style=flat
[docs_link]: https://github.com/codesue/walt/actions/workflows/publish-docs.yml

[license_badge]: https://img.shields.io/github/license/codesue/walt?colorA=363a4f&colorB=b7bdf8&style=flat
[license_link]: https://github.com/codesue/walt/tree/main/LICENSE

[npm_badge]: https://img.shields.io/npm/v/walt.css?colorA=363a4f&colorB=b7bdf8&style=flat
[npm_link]: https://www.npmjs.com/package/walt.css

[pypi_badge]: https://img.shields.io/pypi/v/mkdocs-walt?colorA=363a4f&colorB=b7bdf8&style=flat
[pypi_link]: https://pypi.org/project/mkdocs-walt

[repo_size_badge]: https://img.shields.io/github/repo-size/codesue/walt?colorA=363a4f&colorB=b7bdf8&style=flat
[repo_size_link]: https://github.com/codesue/walt
