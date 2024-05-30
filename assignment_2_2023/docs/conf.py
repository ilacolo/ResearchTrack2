# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import subprocess
import sys
sys.path.insert(0, os.path.abspath('../'))

show_authors=True

project = 'Node A: action_client_node'
copyright = '2024, Ilaria Colomba, 4829201'
author = 'Ilaria Colomba, 4829201'
release = '0.01'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
'sphinx.ext.autodoc', 
'sphinx.ext.doctest', 
'sphinx.ext.intersphinx', 
'sphinx.ext.todo', 
'sphinx.ext.coverage', 
'sphinx.ext.mathjax', 
'sphinx.ext.ifconfig', 
'sphinx.ext.viewcode', 
'sphinx.ext.githubpages', 
"sphinx.ext.napoleon",
'sphinx.ext.inheritance_diagram',
'breathe'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


highlight_language = 'python' 
source_suffix = '.rst' 
master_doc = 'index'
html_theme = 'sphinx_rtd_theme'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


html_static_path = ['_static']


#  Extension configuration
# -- Options for intersphinx extension ---------------------------------------
# Example configuration for intersphinx: refer to the Python standard 
#library. 
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}
# -- Options for todo extension ----------------------------------------------
# If true, `todo` and `todoList` produce output, else they produce nothing. 
todo_include_todos = True
# -- Options for breathe
breathe_projects = {
"assignment_2_2023": "../build/xml/"
}
breathe_default_project = "assignment_2_2023"
breathe_default_members = ('members', 'undoc-members')
