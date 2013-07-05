#!/usr/bin/env python

'''
Python project installation setup for BcdaQWidgets
'''

########### SVN repository information ###################
# $Date$
# $Author$
# $Revision$
# $URL$
# $Id$
########### SVN repository information ###################


#from distutils.core import setup
from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

import os, sys

#sys.path.insert(0, os.path.abspath(os.path.join('src', 'APSpy')))
sys.path.insert(0, os.path.join('src', ))
import bcdaqwidgets

requires = ['Sphinx>=0.6']

setup(
        name=bcdaqwidgets.__project__,
        version=bcdaqwidgets.__version__,
        description=bcdaqwidgets.__description__,
        author=', '.join(bcdaqwidgets.__authors__),
        author_email=bcdaqwidgets.__author_email__,
        url=bcdaqwidgets.__url__,
        packages=bcdaqwidgets.__all__,
        license = bcdaqwidgets.__license__,
        long_description = bcdaqwidgets.__long_description__,
        package_dir={
                     'bcdaqwidgets':  os.path.join('src', 'bcdaqwidgets'),
                     },
        copyright = bcdaqwidgets.__copyright__,
        platforms='any',
        zip_safe=False,
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Environment :: Web Environment',
            'Intended Audience :: Science/Research',
            'License :: Free To Use But Restricted',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Scientific/Engineering',
            'Topic :: Software Development :: Embedded Systems',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Utilities',
        ],
     )
