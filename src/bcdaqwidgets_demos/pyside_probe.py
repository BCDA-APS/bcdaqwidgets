#!/usr/bin/env python

########### SVN repository information ###################
# $Date$
# $Author$
# $Revision$
# $URL$
# $Id$
########### SVN repository information ###################

# from Matt Newville, CARS, University of Chicago

import epics
import os
import sys
from PySide.QtGui import QWidget, QLabel, QLineEdit, QGridLayout, QApplication

sys.path.insert(0, os.path.abspath('..'))
import bcdaqwidgets

class PVProbe(QWidget):
    ''' '''
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        name_label  = QLabel("PV Name:")
        self.pvname = QLineEdit()
        value_label = QLabel("PV Value:")
        self.value  = QLabel(" "*4)

        self.pvname.returnPressed.connect(self.onPVNameReturn)
        self.pv = None

        grid = QGridLayout()
        grid.addWidget(name_label,   0, 0)
        grid.addWidget(self.pvname,  0, 1)
        grid.addWidget(value_label,  1, 0)
        grid.addWidget(self.value,   1, 1)

        self.setLayout(grid)
        self.setWindowTitle("PySide PV Probe:")

    def onPVNameReturn(self):
        if self.pv is not None:
            self.pv.remove_callback()
            self.pv.ca_disconnect()
        self.pv = epics.PV(self.pvname.text(), callback=self.onPVChange)

    def onPVChange(self, pvname=None, char_value=None, **kws):
        self.value.setText(char_value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    probe = PVProbe()
    probe.show()
    sys.exit(app.exec_())
