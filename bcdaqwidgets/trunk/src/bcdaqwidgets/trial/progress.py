from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_(QtGui.QWidget):
    def __init__(self, name, parent=None):
        super(QtGui.QWidget,self).__init__(parent)
        self.layoutWidget = QtGui.QWidget()
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 611, 31))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.progressBar = QtGui.QProgressBar(self.layoutWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 0, 1, 1, 1)
        self.timer = QtCore.QBasicTimer()
        self.step = 0
        self.timer.start(100,self)

        QtCore.QMetaObject.connectSlotsByName(self)
        self.label.setText(_translate("", name, None))
        self.setLayout(self.gridLayout)

    def timerEvent(self, e):
        if self.step>= 100:
            self.timer.stop()
            return
        self.step = self.step + 1
        self.progressBar.setValue(self.step)   
