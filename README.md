# walt: a minimal documentation theme

[![GitHub][github_badge]][github_link]
[![PyPI][pypi_badge]][pypi_link]

[github_badge]: https://badgen.net/badge/icon/GitHub?icon=github&color=black&label
[github_link]: https://github.com/codesue/walt

[pypi_badge]: https://badgen.net/pypi/v/mkdocs-walt?icon=pypi&color=black&label
[pypi_link]: https://pypi.org/project/mkdocs-walt

Walt is a minimal documentation theme that is best suited for single page websites.

## MkDocs theme

Walt is available as an MkDocs theme. See [mkdocs-walt](mkdocs-walt) to learn how
to install and use `mkdocs-walt` in your MkDocs projects.

### Developing mkdocs-walt

#### Installing from source

```sh
git clone https://github.com/codesue/walt.git
cd walt/mkdocs-walt
pip install -e .
```

#### Running the example

```
cd ../examples/mkdocs  # if your current working directory is walt/mkdocs-walt
mkdocs serve
```

#### Building and distributing the package

1. Install the necessary packages:

```sh
pip install "clementine[rind]"
```

2. Build the package and verify the build:

```sh
python -m build
twine check dist/*
```

3. Upload the package to TestPyPI:

```sh
twine upload -r testpypi dist/*
```

Install the package from TestPYPI in a clean virtual environment and confirm
that the example runs as expected:

```sh
pip install -i https://test.pypi.org/simple/ mkdocs-walt
```

4. Upload the package to PyPI:

```sh
twine upload dist/*
```

## Acknowledgements

Walt uses [writ.css](https://github.com/programble/writ/tree/master) for styles
and examples use [writ's reference html page](https://github.com/programble/writ/blob/master/reference.html).

Walt also uses [Catppuccin](https://github.com/catppuccin/catppuccin) for code
block syntax highlighting and dark mode color palettes.
