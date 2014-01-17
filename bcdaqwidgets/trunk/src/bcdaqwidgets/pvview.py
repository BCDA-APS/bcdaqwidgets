#!/usr/bin/env python

'''display one or more EPICS PVs in a PySide GUI window as a table'''

import os
import sys
from PySide.QtGui import QWidget, QLabel, QGridLayout, QApplication

sys.path.insert(0, os.path.abspath('..'))
import bcdaqwidgets

class PVView(QWidget):
    ''' '''
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.db = {}

        name_label  = QLabel("PV Name")
        value_label = QLabel("PV Value")
        for item in (name_label, value_label):
            sty = bcdaqwidgets.StyleSheet(item, {
                                   'background-color': 'gray',
                                   'color': 'white',
                                   'font': 'bold',
                                   })
            sty.updateStyleSheet()

        self.grid = QGridLayout()
        self.grid.addWidget(name_label,   0, 0)
        self.grid.addWidget(value_label,  0, 1)
        self.grid.setColumnStretch(0, 0)
        self.grid.setColumnStretch(1, 1)

        self.setLayout(self.grid)
        self.setWindowTitle("EPICS PV View")

    def add(self, pvname):
        '''add a PV to the table'''
        if pvname in self.db:
            return
        row = len(self.db) + 1
        label = QLabel(pvname)
        widget = bcdaqwidgets.BcdaQLabel(pvname=pvname)
        widget.useAlarmState = True
        self.db[pvname] = widget
        self.grid.addWidget(label, row, 0)
        self.grid.addWidget(widget, row, 1)


def main():
    app = QApplication(sys.argv)
    probe = PVView()
    if len(sys.argv) < 2:
        raise RuntimeError, "Must specify one or more EPICS PVs on command line"
    for pvname in sys.argv[1:]:
        probe.add(pvname)
    probe.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    txt = '${P}cr:{pwm11,ai{0,1,2}:mean,{rate,period},cmd}{.DESC,}'
    pvs = []
    _p = ['ino:cr:' + _ for _ in ('ai0', 'ai1', 'ai2')]
    for _ in _p:
        pvs.append(_)
        pvs.append(_ + ':mean')
    pvs.insert(0, 'ino:cr:pwm11')
    for _ in ('rate', 'period', 'cmd'):
        pvs.append('ino:cr:' + _)
    for _ in pvs:
        sys.argv.append(_)
        sys.argv.append(_ + '.DESC')
    main()


########### SVN repository information ###################
# $Date$
# $Author$
# $Revision$
# $URL$
# $Id$
########### SVN repository information ###################
