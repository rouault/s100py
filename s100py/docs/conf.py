# -*- coding: utf-8 -*-
#
# Pydro documentation build configuration file, created by
# sphinx-quickstart on Tue Nov 28 16:43:03 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

import os
import sys
import types

import re
import sphinx
p, f = os.path.split(__file__)
root_p = os.path.normpath(p)
sys.path.insert(0, os.path.abspath(".."))
sys.path.insert(0, os.path.abspath("..\\.."))

# rst_prolog = """
# .. |DOCS_DIR| replace:: %s
# .. include:: %s\\_Globals\\substitutions.txt
# """ % (root_p.replace("\\", "/") + "/", root_p)

# rst_epilog = """
# .. include:: %s\\_Globals\\footer.rst
# """ % root_p

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = '%s/_static/pydro_sidebar.png' % root_p

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# html_favicon = '%s/_static/pydro.ico' % root_p

import inspect

top_classes = "s100py.s1xx.S1xxAttributesBase, s100py.s1xx.S1XXFile"

# watch out, used ratio (without reading spec) and it made the image go to two pages which fails with sphinx
inheritance_graph_attrs = dict(rankdir="TB", size='"24.0 36.0"')  # make the pictures bigger, default is "8.0 12.0"

def check_to_skip(app, what, name, obj, skip, options):
    """ The member is excluded if a handler returns True. It is included if the handler returns False.
    If more than one enabled extension handles the autodoc-skip-member event, 
    autodoc will use the first non-None value returned by a handler. 
    Handlers should return None to fall back to the skipping behavior of autodoc and other enabled extensions."""
    # print()
    # print()
    # if "Callable" in name or "FeatureContainer" in name or "s102.s102" in name:
    #     print(what, name, type(obj), obj, skip, options)
    #     print()
    # if isinstance(options, dict):
    #     if options.get("meth", "") == "run":
    #         modname = ""
    #         if isinstance(what, (list, tuple)):
    #             if len(what) == 2:
    #                 what, modname = what
    #         if options.get("cls", False) == True:
    #             if modname not in obj:
    #                 print("skipping")
    #                 print()
    #                 return True
    if isinstance(obj, property) or "property" in str(obj):
        # class bathymetry_coverage < property object at 0x0000019161C07278 > False {'members': <object object at 0x000001915FFC3110 >, 'undoc-members': True, 'show-inheritance': True}
        if name.endswith("_type") or name.endswith("_attribute_name"):  # re.search("_type", name):
            return True
    if "<class 'str'>" in str(obj):
        # class bathymetry_coverage < property object at 0x0000019161C07278 > False {'members': <object object at 0x000001915FFC3110 >, 'undoc-members': True, 'show-inheritance': True}
        if name.endswith("_attribute_name"):  # re.search("_type", name):
            return True

    if isinstance(obj, types.FunctionType) or "function" in str(obj):
        # class bathymetry_coverage < property object at 0x0000019161C07278 > False {'members': <object object at 0x000001915FFC3110 >, 'undoc-members': True, 'show-inheritance': True}
        if name.endswith("_remove") or name.endswith("_create"):  # re.search("_type", name):
            # print("True")
            return True


def source_read_handler(app, docname, source):
    # print("<source read handler>")
    # print(docname, source)
    # print("</source read handler>")
    pass

def setup(app):
    app.connect('source-read', source_read_handler)
    app.connect("autodoc-skip-member", check_to_skip)
    app.add_stylesheet('pydro_custom.css')  # may also be an URL


html_show_sourcelink = False
html_copy_source = False

html_sidebars = {'**': ['localtoc.html', 'relations.html', 'searchbox.html'], }  # , 'download_page.html'

# example of shortening urls
# :issue:`test`
extlinks = {'svnhtml':
            ('http://svn.pydro.noaa.gov/', '')}


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# http://www.sphinx-doc.org/en/stable/ext/ifconfig.html

try:
    import sphinxcontrib.fulltoc
    full_toc = 'sphinxcontrib.fulltoc'
except:
    # Giuseppe and I installed in different places
    try:
        import sphinxcontrib_fulltoc.fulltoc
        full_toc = 'sphinxcontrib_fulltoc.fulltoc'
    except:
        full_toc = ""

extensions = ['sphinx.ext.imgmath',
              'sphinx.ext.githubpages',
              'sphinx.ext.extlinks',
              'sphinx.ext.ifconfig',
              full_toc,
              'sphinx.ext.graphviz',
#              'sphinx.ext.autodoc',
#              'sphinx.ext.autosummary',
              'sphinx_automodapi.automodapi',
              'sphinx.ext.napoleon',
              'sphinx_autodoc_typehints',
              ]

automodsumm_inherited_members = False
automodapi_inheritance_diagram = True
numpydoc_show_class_members = False  # orevents duplication per automodapi docs
graphviz_dot = os.path.normpath(os.path.join(root_p, r"..\..\..\..\..\envs\Pydro367\Library\bin\graphviz\dot.exe"))
# autosummary_generate = True

autodoc_default_options = {
   # 'members': 'var1, var2',
   'member-order': 'bysource',
   'special-members': '__init__',
   'undoc-members': True,
   'exclude-members': '__weakref__',
#    'inherited-members': False,
}

# autodoc_default_flags = [
#         # Make sure that any autodoc declarations show the right members
#         "members",
#         #"inherited-members",
#         "private-members",
#         "show-inheritance",
# ]

# Napoleon settings
napoleon_google_docstring = False
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

# Add any paths that contain templates here, relative to this directory.
templates_path = ['templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 's100py'

# adds figure numbers automatically
numfig = True
# numfig_secnum_depth = (2)
# numfig_format = {'figure': 'Figure %s', 'table': 'Table %s', 'code-block': 'Code Block %s'}

# General information about the project.


def set_project_names(prj, auth=u'Hydrographic Systems and Technology Branch', g={}):
    if not g:
        g = globals()
    g['project'] = prj
    g['author'] = auth
    # Output file base name for HTML help builder.
    g['htmlhelp_basename'] = prj + '_doc'
    # Grouping the document tree into LaTeX files. List of tuples
    # (source start file, target name, title,
    #  author, documentclass [howto, manual, or own class]).
    g['latex_documents'] = [
        (g['master_doc'], prj + '.tex', prj + u' Documentation',
         u'Hydrographic Systems and Technology Branch', 'manual'),
    ]
    # -- Options for manual page output ---------------------------------------
    # One entry per manual page. List of tuples
    # (source start file, name, description, authors, manual section).
    g['man_pages'] = [
        (g['master_doc'], prj, prj + u' Documentation',
         [g['author']], 1)
    ]

    # -- Options for Texinfo output -------------------------------------------
    # Grouping the document tree into Texinfo files. List of tuples
    # (source start file, target name, title, author,
    #  dir menu entry, description, category)
    g['texinfo_documents'] = [
        (g['master_doc'], prj, prj + u' Documentation',
         g['author'], prj, 'One line description of project.',
         'Miscellaneous'),
    ]


set_project_names(u'Pydro')
html_show_copyright = False
copyright = u'None - %s is not subject to Copyrights (though other distributed pieces may be)' % project

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u''
# The full version, including alpha/beta/rc tags.
release = u''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["sphinx_dir_template/*", '_build', '_build_offline', '_build_online', 'Thumbs.db', '.DS_Store']


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'classic'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}
html_theme_options = {
    'sidebarbgcolor': "#054698",
    'relbarbgcolor': "#29318B",
    'footerbgcolor': "#29318B",
    'linkcolor': "#0098DA",
    'visitedlinkcolor': "#054698",
    'sidebarlinkcolor': "#E0F2FF",
    'body_max_width':'none',
    # 'relbarlinkcolor' : "#0098DA",
    # bgcolor
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}
