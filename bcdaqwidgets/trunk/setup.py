#!/usr/bin/env python

'''packaging for BcdaQWidgets'''

from setuptools import setup, find_packages
import os
import sys

sys.path.insert(0, os.path.join('src', ))
import local_config

setup(
    author           = local_config.__author__,
    author_email     = local_config.__author_email__,
    classifiers      = local_config.__classifiers__,
    description      = local_config.__description__,
    entry_points     = local_config.__entry_points__,
    license          = local_config.__license__,
    long_description = local_config.__long_description__,
    install_requires = local_config.__install_requires__,
    name             = local_config.__project__,
    platforms        = local_config.__platforms__,
    packages         = local_config.__packages__.keys(),
    package_dir      = local_config.__packages__,
    package_data     = local_config.__package_data__,
    url              = local_config.__url__,
    version          = local_config.__version__,
    zip_safe         = local_config.__zip_safe__,
 )


########### SVN repository information ###################
# $Date$
# $Author$
# $Revision$
# $URL$
# $Id$
########### SVN repository information ###################
