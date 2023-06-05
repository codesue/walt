# DEVELOPMENT

This guide is internal and a work in progress. It assumes familiarity with `npm`,
`pip`, `git`, `mkdocs`, and typical development workflows.

## Getting Started

1. Clone this repository

   ```sh
   git clone https://github.com/codesue/walt.git
   ```

2. Navigate to the directory

   ```sh
   cd walt
   ```

3. Install dependencies

   If you're making updates to [`walt.css`](https://github.com/codesue/walt/blob/main/walt.css), run:

   ```sh
   npm install
   ```

   If you're making changes to [`mkdocs-walt`](https://github.com/codesue/walt/blob/main/mkdocs),
   run the following in a Python virtual environment:

   ```sh
   cd mkdocs
   pip install -e .
   ```

## Developing walt.css

Open [reference.html](https://github.com/codesue/walt/blob/main/reference) in a browser.
Make changes to [walt.css](https://github.com/codesue/walt/blob/main/walt.css) and
refresh the tab with reference.html to preview your changes.

Lint your changes to make sure they follow style guidelines:

```sh
npm run test
```

When you're satisfied with your changes, run:

```sh
npm run build
```

## Developing mkdocs-walt

Run the mkdocs development server:

```sh
mkdocs serve
```

Make changes to [mkdocs-walt](https://github.com/codesue/walt/blob/main/mkdocs)
and preview them in a browser.

## Folder Structure

- `/`: various config and informational files
- `.github/`: GitHub Actions workflows
- `assets/`: assets such as preview images for the project
- `docs/`: project documentation, mkdocs example
- `mkdocs/`: Walt theme for MkDocs Python package
