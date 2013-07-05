

########### SVN repository information ###################
# $Date$
# $Author$
# $Revision$
# $URL$
# $Id$
########### SVN repository information ###################

__project__     = u'BcdaQWidgets'
__description__ = u"PyEpics-aware PySide widgets for the APS."
__copyright__   = u'2013, Argonne National Laboratory'
__authors__     = [u'Pete Jemian', u'Cayla Suarez']
__institution__ = u"Advanced Photon Source, Argonne National Laboratory"
__author_email__= u"jemian@anl.gov"
__url__         = u"will be but not yet: http://subversion.xray.aps.anl.gov/admin_bcdaext/BcdaQWidgets"
__license__     = u"(c) 2009-2013, UChicago Argonne, LLC"
__license__     += u" (see LICENSE file for details)"

__long_description__ = __description__

import datetime

__yyyymmdd__      = str(datetime.datetime.now()).split()[0]
__version__       = u"0.1"
__minor_version__ = u""
__svnid__         = u"$Id$"
__revision__       = __svnid__.split(" ")[2]
#__full_version__ = u"%s.%s-r%s" % (__version__, __minor_version__, __revision__) 
__full_version__  = u"v%s.%s, %s" % (__version__, __minor_version__, __yyyymmdd__) 
