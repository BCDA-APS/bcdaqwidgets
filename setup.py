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

sys.path.insert(0, os.path.join('src', ))
import bcdaqwidgets

requires = ['Sphinx>=0.6']

packages = {}
for pkg in ('bcdaqwidgets', 'bcdaqwidgets_demos', 'motorqt_demo'):
    packages[pkg]       = os.path.join('src', pkg)

console_scripts = []
for launcher, method_path in {
    'pvview': 'bcdaqwidgets.pvview:main',
    #'pyside_probe': 'bcdaqwidgets_demos.pyside_probe:main',
    'motor_qt': 'motorqt_demo.motor_qt:main',
    'multimotor': 'motorqt_demo.multimotor:main',
                 }.items():
    console_scripts.append(launcher + ' = ' + method_path)

setup(
        name=bcdaqwidgets.__project__,
        version=bcdaqwidgets.__version__,
        description=bcdaqwidgets.__description__,
        long_description = bcdaqwidgets.__long_description__,
        author=', '.join(bcdaqwidgets.__authors__),
        author_email=bcdaqwidgets.__author_email__,
        url=bcdaqwidgets.__url__,
        packages=packages.keys(),
        license = bcdaqwidgets.__license__,
        package_dir=packages,
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
      entry_points={
          # create & install console_scripts in <python>/bin
          'console_scripts': console_scripts,
      },
     )
