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
__description__ = u"PyEpics-aware PySide widgets for the APS."
__copyright__   = u'2009-2014, UChicago Argonne, LLC'
__authors__     = [u'Pete Jemian', u'Cayla Suarez']
__author__      = ', '.join(__authors__)
__institution__ = u"Advanced Photon Source, Argonne National Laboratory"
__author_email__= u"jemian@anl.gov"
__url__         = u"will be but not yet: http://subversion.xray.aps.anl.gov/admin_bcdaext/BcdaQWidgets"
__license__     = u"(c) " + __copyright__
__license__     += u" (see LICENSE file for details)"

__long_description__ = __description__

__version__       = u"0.1.4"
__minor_version__ = u""
__svnid__         = u"$Id$"
__revision__       = __svnid__.split(" ")[2]
#__full_version__ = u"%s.%s-r%s" % (__version__, __minor_version__, __revision__) 
__full_version__  = u"v%s.%s" % (__version__, __minor_version__)
__install_requires__ = ['pyepics>=3.2.2', ]
__all__ = ['bcdaqwidgets', ]

__platforms__        = 'any'
__zip_safe__         = False


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

__package_data__ = {'bcdaqwidgets': ['LICENSE',],}

__entry_points__  = {
    # create & install console_scripts in <python>/bin
    'console_scripts': __console_scripts__,
    #'gui_scripts': gui_scripts,
}


########### SVN repository information ###################
# $Date$
# $Author$
# $Revision$
# $URL$
# $Id$
########### SVN repository information ###################
