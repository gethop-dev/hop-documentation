# Configuration file for the Sphinx documentation builder.

# -- Changes needed after "Read the Docs Addons" were enabled by
# -- default. See
# -- https://about.readthedocs.com/blog/2024/07/addons-by-default/
# -- for additional eetails.
import os

# Define the canonical URL if you are using a custom domain on Read the Docs
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")

# Tell Jinja2 templates the build is running on Read the Docs
if os.environ.get("READTHEDOCS", "") == "True":
    if "html_context" not in globals():
        html_context = {}
    html_context["READTHEDOCS"] = True

# -- Project information

project = 'HOP'
copyright = '2024 Biotz, SL. This website is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License. To view a copy of this license, visit https://creativecommons.org/licenses/by-sa/4.0/'
author = 'Biotz, SL'

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
