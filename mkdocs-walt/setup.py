from setuptools import setup, find_packages

VERSION = '0.1.0-dev'

with open('README.md', 'r') as f:
  LONG_DESCRIPTION = f.read()

setup(
    name='mkdocs-walt',
    version=VERSION,
    author='Suzen Fylke',
    author_email='codesue@users.noreply.github.com',
    description='A minimal theme for MkDocs',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/codesue/walt',
    license='MIT',
    classifiers = [
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
    ],
    keywords=['mkdocs', 'mkdocs-theme', 'walt'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=['mkdocs'],
    entry_points={
        'mkdocs.themes': [
            'walt = walt',
        ]
    },
    zip_safe=False
)
