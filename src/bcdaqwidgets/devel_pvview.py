#!/usr/bin/env python

'''display one or more EPICS PVs in a PySide GUI window as a table'''

import os
import sys
import pvview

sys.path.insert(0, os.path.abspath('..'))

# txt = '${P}cr:{pwm11,ai{0,1,2}:mean,{rate,period},cmd}{.DESC,}'
# pvs = []
# _p = ['ino:cr:' + _ for _ in ('ai0', 'ai1', 'ai2')]
# for _ in _p:
#     pvs.append(_)
#     pvs.append(_ + ':mean')
# pvs.insert(0, 'ino:cr:pwm11')
# for _ in ('rate', 'period', 'cmd'):
#     pvs.append('ino:cr:' + _)
# for _ in pvs:
#     sys.argv.append(_)
#     sys.argv.append(_ + '.DESC')
sys.argv.append( 'S:SRcurrentAI' )
pvview.main()


########### SVN repository information ###################
# $Date$
# $Author$
# $Revision$
# $URL$
# $Id$
########### SVN repository information ###################
