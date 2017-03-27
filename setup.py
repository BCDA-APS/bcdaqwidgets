#!/usr/bin/env python

'''packaging for BcdaQWidgets'''

from setuptools import setup, find_packages
import os
import sys
import versioneer

sys.path.insert(0, os.path.join('src', ))
import bcdaqwidgets

setup(
    author           = bcdaqwidgets.__author__,
    author_email     = bcdaqwidgets.__author_email__,
    classifiers      = bcdaqwidgets.__classifiers__,
    description      = bcdaqwidgets.__description__,
    entry_points     = bcdaqwidgets.__entry_points__,
    license          = bcdaqwidgets.__license__,
    long_description = bcdaqwidgets.__long_description__,
    install_requires = bcdaqwidgets.__install_requires__,
    name             = bcdaqwidgets.__project__,
    #platforms        = bcdaqwidgets.__platforms__,
    packages         = bcdaqwidgets.__packages__.keys(),
    package_dir      = bcdaqwidgets.__packages__,
    package_data     = bcdaqwidgets.__package_data__,
    url              = bcdaqwidgets.__url__,
    version          = versioneer.get_version(),
    cmdclass         = versioneer.get_cmdclass(),
    zip_safe         = bcdaqwidgets.__zip_safe__,
 )
