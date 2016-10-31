'''
BCDA Qt Widgets for EPICS
'''

import os
from _version import git_release

import bcdaqwidgets


StyleSheet           = bcdaqwidgets.StyleSheet
BcdaQSignalDef	     = bcdaqwidgets.BcdaQSignalDef
BcdaQLabel           = bcdaqwidgets.BcdaQLabel
BcdaQLineEdit	     = bcdaqwidgets.BcdaQLineEdit
BcdaQPushButton      = bcdaqwidgets.BcdaQPushButton
BcdaQMomentaryButton = bcdaqwidgets.BcdaQMomentaryButton
BcdaQToggleButton    = bcdaqwidgets.BcdaQToggleButton
BcdaQLabel_RBV       = bcdaqwidgets.BcdaQLabel_RBV
RBV_BcdaQLabel       = BcdaQLabel_RBV       # legacy

__project__     = u'BcdaQWidgets'
__description__ = u"PyEpics-aware PyQt widgets for the APS."
__copyright__   = u'2009-2016, UChicago Argonne, LLC'
__authors__     = [u'Pete Jemian', u'Cayla Suarez']
__author__      = ', '.join(__authors__)
__institution__ = u"Advanced Photon Source, Argonne National Laboratory"
__author_email__= u"jemian@anl.gov"
__url__         = u"http://bcdaqwidgets.readthedocs.org"
__license__     = u"(c) " + __copyright__
__license__     += u" (see LICENSE file for details)"
__platforms__   = 'any'
__zip_safe__    = False

__package_name__ = __project__
__long_description__    = __description__

_path = os.path.dirname(__file__)
_vfile = os.path.join(_path, 'VERSION')
__version__ = open(_vfile, 'r').read()
__release__ = git_release(__package_name__, __version__)

__keywords__            = ['APS', 'EPICS', 'PyQt4']
#__requires__            = ['PyQt4', 'pyepics']
__requires__            = ['pyepics']
__install_requires__    = __requires__
__documentation_mocks__ = ['epics']       # do NOT mock PyQt4 here, big problems if you do

__classifiers__ = [
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
   ]

# create & install console_scripts in <python>/bin
__console_scripts__ = [
    'pvview = bcdaqwidgets.pvview:main',
    'motor_qt = motorqt_demo.motor_qt:main',
    'multimotor = motorqt_demo.multimotor:main',
   ]

__packages__ = {
    'bcdaqwidgets'      : 'src/bcdaqwidgets',
    'bcdaqwidgets_demos': 'src/bcdaqwidgets_demos',
    'motorqt_demo'      : 'src/motorqt_demo',
}

__package_data__ = {
                    'bcdaqwidgets': [
                                     'LICENSE',
                                     'VERSION',
                                     ],
                    }

__entry_points__  = {
    # create & install console_scripts in <python>/bin
    'console_scripts': __console_scripts__,
    #'gui_scripts': gui_scripts,
}
