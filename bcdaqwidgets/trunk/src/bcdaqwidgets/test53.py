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

    def __init__(self, parent=None, rbv='', dmov=None):
        '''constructor'''
        QtGui.QWidget.__init__(self, parent)

        layout = QtGui.QGridLayout()
        layout.addWidget(QtGui.QLabel('BcdaQLabel'), 0, 0)
        self.value = bcdaqwidgets.BcdaQLabel(pvname=rbv)
        layout.addWidget(self.value, 0, 1)
        self.setLayout(layout)

        if dmov is not None:
            self.dmov = epics.PV(pvname=dmov, callback=self.onDmovChanged)

        self.dmov_bg_clut = {'not connected': 'white', '0': '#88ff88', '1': 'transparent'}
        self.dmov_bg_color = None

        self.dmovSignal = bcdaqwidgets.BcdaQSignalDef()
        self.dmovSignal.newBgColor.connect(self.SetBackgroundColor)

    def onDmovChanged(self, *args, **kw):
        '''epics pv callback when motor starts or stops moving'''          
        if not self.dmov.connected:     # white and displayed text is ' '
            self.dmov_bg_color = self.dmov_bg_clut['not connected']
        else:
            value = str(self.dmov.get())
            if value in self.dmov_bg_clut:
                self.dmov_bg_color = self.dmov_bg_clut[value]
        # trigger the background color to change
        self.dmovSignal.newBgColor.emit()

    def SetBackgroundColor(self, *args, **kw):
        '''changes the background color of the widget'''
        if self.dmov_bg_color is not None:
            self.value.updateStyleSheet({'background-color': self.dmov_bg_color})
            self.dmov_bg_color = None

            
#------------------------------------------------------------------


def main():
    '''command-line interface to test this GUI widget'''
    app = QtGui.QApplication(sys.argv)
    view = DemoView(rbv='prj:m1.RBV', dmov='prj:m1.DMOV')
    view.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
