# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# autosummary
import os
import sys
import glob
sys.path.insert(0, os.path.abspath('..'))  # Ensure your module is found

autosummary_generate = True  # Turn on autosummary
autodoc_mock_imports = []  # Add any modules you want to mock if they can't be imported

# source_suffix = ['.rst', '.md']
source_suffix = '.rst'


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'TCRA'
copyright = '2024, Ram Krishna Mazumder'
author = 'Ram Krishna Mazumder'
release = '1.1.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autosummary',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon'  # For Google style docstrings
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Enable numpydoc for parsing numpy-style docstrings
numpydoc_show_class_members = False


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Enable autosummary
autosummary_generate = glob.glob("apidocs/*.rst")

# Include Python modules for autodoc
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

# Add paths for custom static files
html_static_path = ['_static']
