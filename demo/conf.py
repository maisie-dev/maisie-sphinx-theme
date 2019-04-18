import sys, os, subprocess

from sphinx.highlighting import lexers
from pygments.lexers.web import PhpLexer


project = u"Demo"
copyright = u"2015, My Name"
master_doc = "index"
templates_path = ["_templates"]
extensions = []
source_suffix = ".rst"
version = "X.Y.Z"
exclude_patterns = ["_build"]

# -- HTML theme settings ------------------------------------------------

html_show_sourcelink = False
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

import maisie_sphinx_theme

extensions.append("maisie_sphinx_theme")
html_theme_path = maisie_sphinx_theme.html_theme_path()
html_theme = "maisie_sphinx_theme"

# Maisie theme options (see theme.conf for more information)
html_theme_options = {"base_url": "http://my-site.com/docs/"}
