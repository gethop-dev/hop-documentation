# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'HOP'
copyright = 'This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.'
author = 'Magnet S. Coop'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_logo = 'img/logo.svg'

html_theme_options = {
    'logo_only': True,
    'display_version': False
}

html_static_path = ['_static']

html_css_files = ['css/style.css']

# -- Options for EPUB output
epub_show_urls = 'footnote'
