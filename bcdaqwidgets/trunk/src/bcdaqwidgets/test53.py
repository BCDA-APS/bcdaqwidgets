#!/usr/bin/env python

########### SVN repository information ###################
# $Date: 2013-07-16 17:08:49 -0500 (Tue, 16 Jul 2013) $
# $Author: csuarez $
# $Revision: 1417 $
# $URL: https://subversion.xray.aps.anl.gov/bcdaext/bcdaqwidgets/trunk/src/bcdaqwidgets/bcdaqwidgets.py $
# $Id: bcdaqwidgets.py 1417 2013-07-16 22:08:49Z csuarez $
########### SVN repository information ###################

'''
Test code for TRAC ticket #53.
'''


import epics
from PySide import QtGui, QtCore
import bcdaqwidgets
import sys


class DemoView(QtGui.QWidget):
    '''
    Show the BcdaQWidgets using an EPICS PV connection.

    Allow it to connect and ca_disconnect.
    This is a variation of EPICS PV Probe.

    '''

    def __init__(self, parent=None, rbv='', dmov=''):
        QtGui.QWidget.__init__(self, parent)

        layout = QtGui.QGridLayout()
        layout.addWidget(QtGui.QLabel('BcdaQLabel'), 0, 0)
        self.value = bcdaqwidgets.BcdaQLabel(pvname=rbv)
        layout.addWidget(self.value, 0, 1)
        self.setLayout(layout)

        self.colorPV = False

        self.ca_connect(rbv)
        self.ca_connect(dmov)

    def ca_connect(self, pvname):
        self.value.ca_connect(pvname, ca_callback=self.SetBackgroundColor)

    def SetBackgroundColor(self, *args, **kw):
        '''changes the background color when the motor is moving or not moving'''          
        if self.connect==False:     # white and displayed text is ' '
            self.updateStyleSheet({'background-color': 'white'})
        else:
            self.colorPV = not self.colorPV
            if dmov == 1:
                self.colorPV = False
            else:   # motor is moving
                self.colorPV = True
            color = {False: "transparent", True: "green",}[self.colorPV]
            self.updateStyleSheet({'background-color': color})

#------------------------------------------------------------------

def main():
    '''command-line interface to test this GUI widget'''
    app = QtGui.QApplication(sys.argv)
    view = DemoView(rbv='prj:m1.RBV', dmov='prj:m1.DMOV')
    view.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
