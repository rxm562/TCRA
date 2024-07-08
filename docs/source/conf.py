# Configuration file for the Sphinx documentation builder.
#
# For a full list of options, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import glob

# Ensure the project's root directory is in sys.path
sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------
project = 'TCRA'
copyright = '2024, Ram Krishna Mazumder'
author = 'Ram Krishna Mazumder'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
]

add_function_parentheses = True
add_module_names = False
python_display_short_literal_types = True

toc_object_entries = True
toc_object_entries_show_parents = 'hide'
# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

autodoc_default_options = {
    'undoc-members': True,
    'private-members': False,
    'special-members': False,
    'inherited-members': True,
    'show-inheritance': True,
    'member-order': 'groupwise',
}

autodoc_class_signature = 'separated'
autodoc_typehints = 'description'
autodoc_typehints_format = 'short'
autodoc_typehints_description_target = 'documented'
autodoc_type_aliases = {'DataFrame': 'pandas DataFrame',}

autoclass_content = 'class'

numfig=True
numfig_format = {'figure':  'Figure %s', 'table': 'Table %s', 'code-block': 'Listing %s'}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

viewcode_import = True
autodoc_member_order = 'bysource'
autoclass_content = 'both'

numfig = True
numfig_format = {'figure': 'Figure %s', 'table': 'Table %s', 'code-block': 'Listing %s'}

math_numfig = True
math_eqref_format = "Eq.{number}"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# autosummary
autosummary_generate = glob.glob("apidocs/*.rst")
autosummary_generate_overwrite = True
# The suffix(es) of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'content'

# List of patterns, relative to source directory, that match files and directories to ignore.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_theme_options = {'body_max_width': '100%'}
html_static_path = ['_static']  # Ensure this directory exists
html_show_sphinx = False

# -- Options for HTMLHelp output ---------------------------------------------
htmlhelp_basename = 'tcradoc'

# -- Options for LaTeX output ------------------------------------------------
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',

    # Latex figure (float) alignment
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'TCRA.tex', 'TCRA Documentation', 'Ram Krishna Mazumder', 'manual'),
]

# -- Options for manual page output ------------------------------------------
man_pages = [
    (master_doc, 'TCRA', 'TCRA Documentation', [author], 1)
]

# -- Options for Texinfo output ----------------------------------------------
texinfo_documents = [
    (master_doc, 'TCRA', 'TCRA Documentation', author, 'TCRA', 'One line description of project.', 'Miscellaneous'),
]
