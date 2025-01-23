# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PCREC'
#copyright = '2025, Bruce Frederiksen'
author = 'Bruce Frederiksen'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
#html_theme_options = {
#   #'logo': 
#    'github_user': 'dangyogi',
#    'github_repo': 'RPOF-CMC',
#    'fixed_sidebar': True,
#    'show_related': True,
#   #'sidebar_collapse': True,
#    'extra_nav_links': {
#        'Table of Contents': 'index.html',
#        'Index': 'genindex.html',
#    }
#}
#html_sidebar_width = '300px'   # alabaster default 220px, sphinx default 230
#html_page_width = '940px'      # alabaster default 940px
#html_sidebar_collapse = True
#html_sidebars = {
## alabaster default: about.html, searchfield.html, navigation.html, relations.html, donate.html
#  "**": ['indexlink.html', 'localtoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html',],
#}

#html_theme = 'sphinxdoc'
#html_theme = 'python_docs_theme'

html_theme = 'furo'
html_sidebars = {
# furo default:  sidebar/brand.html, sidebar/search.html, sidebar/scroll-start.html,
#                sidebar/navigation.html, sidebar/ethical-ads.html, sidebar/scroll-end.html,
#                sidebar/variant-selector.html
  "**": [
       # 'sidebar/brand.html',
         'sidebar/search.html',
         'toplinks.html', 
         'sidebar/scroll-start.html',
         'sidebar/navigation.html',
         'sidebar/ethical-ads.html',            # READTHEDOCS
         'sidebar/scroll-end.html',
         'relations.html',
         'sourcelink.html', 
         'sidebar/variant-selector.html',       # READTHEDOCS
        ]
}

html_static_path = ['_static']
html_use_index = True
html_show_copyright = False
html_show_sphinx = True

#html_sidebars = {
#  "**": ['indexlink.html', 'localtoc2.html', 'relations.html', 'sourcelink.html', 'searchbox.html',],
#}

html_css_files = [
    'custom.css',
]
