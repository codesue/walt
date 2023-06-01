# mkdocs-walt

🍃 Walt is a minimal documentation theme for MkDocs.

It has the following features:

- classless styles for semantic HTML based on [writ.css](https://writ.cmcenroe.me)
- light mode and dark mode based on system settings
- an emoji favicon for browsers that support svg site icons
- code syntax highlighting using highlight.js

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/codesue/walt/tree/main/assets/images/mkdocs-walt-dark.png" />
  <img src="https://github.com/codesue/walt/tree/main/assets/images/mkdocs-walt-light.png" alt="Screenshot of the Walt website" />
</picture>

## Installation

```sh
pip install mkdocs-walt
```

## Usage

Create a new MkDocs project with the `mkdocs` CLI and add the following your
project's `mkdocs.yml`:

```yaml
theme:
  name: walt
```

See the [end to end example](https://github.com/codesue/walt/tree/main/examples/mkdocs).

## Defaults

Walt sets the following configurations by default:

```yaml
site_emoji: 🍃
locale: en
theme_color: "hsl(0, 0%, 100%)"
theme_color_dark: "hsl(232, 23%, 18%)"
include_header: true
include_nav: true
highlightjs: true
```

## License

Copyright &copy; 2023 [Suzen Fylke](https://suzenfylke.com). Distributed under the MIT License.

## Acknowledgements

Walt uses [writ.css](https://github.com/programble/writ/tree/master) for styles
and [Catppuccin](https://github.com/catppuccin/catppuccin) for code block syntax
highlighting and dark mode color palettes.
