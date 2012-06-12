#!/usr/bin/env python

from distutils.core import setup

import os

# Sets what directory to crawl for files to include
# Relative to location of setup.py; leave off trailing slash
includes_dir = 'stanford-corenlp-2012-04-09/'

# Set the root directory for included files
# Relative to the bundle's Resources folder, so '../../' targets bundle root
includes_target = 'stanford-corenlp-2012-04-09/'

# Initialize an empty list so we can use list.append()
includes = []

# Walk the includes directory and include all the files
for root, dirs, filenames in os.walk(includes_dir):
    if root is includes_dir:
        final = includes_target
    else:
        final = includes_target + root[len(includes_dir)+1:] + '/'
    files = []
    for file in filenames:
        if (file[0] != '.'):
            files.append(os.path.join(root, file))
    includes.append((final, files))

# Add a extra files to include in the root directory
includes = includes+[('',['default.properties'])]

setup(name='stanford-corenlp-python',
      version='1.0',
      description='Standford Core NLP for Python',
      author='Dustin Smith',
      author_email='dustin@media.mit.edu',
      url='https://github.com/dasmith/stanford-corenlp-python',
      py_modules=['corenlp','client','progressbar'],
      data_files = includes,
      requires=['jsonrpc','pexpect','unidecode'],
     )
