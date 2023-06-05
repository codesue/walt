# About

Walt is a minimal documentation theme based on [writ.css](https://writ.cmcenroe.me).
It features classless styles for semantic HTML and supports light and dark mode
based on system settings.

## Stylesheet

You can include the Walt stylesheet in your project in the following ways:

- Copy the stylesheet from [GitHub](https://github.com/codesue/walt/blob/main/walt.css)

- Install from npm:

    ```sh
    npm install --save walt.css
    ```

- Link to a CDN:

    ```html
    <link rel="stylesheet" href="https://unpkg.com/walt.css/walt.css" />
    ```

## MkDocs theme

Walt is available as an MkDocs theme that features:

- classless styles for semantic HTML based on [writ.css](https://writ.cmcenroe.me)
- light mode and dark mode based on system settings
- an emoji favicon for browsers that support svg site icons
- code syntax highlighting using highlight.js

### Installation

Installing with pip:

```sh
pip install mkdocs-walt
```

### Usage

Create a new MkDocs project with the `mkdocs` CLI and add the following your
project's `mkdocs.yml`:

```yaml
theme:
  name: walt
```

### Defaults

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
