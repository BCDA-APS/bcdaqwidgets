import sys
try:
    from PyQt4 import QtCore, QtGui
except ImportError:
    from PySide import QtCore, QtGui
from main_ui import Ui_MainWindow
import progress
import random

reload(progress)
class MyForm(QtGui.QMainWindow):
  def __init__(self, parent=None):
    QtGui.QMainWindow.__init__(self, parent)
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    self.ui.pushButton.clicked.connect(self.progress)

  def progress(self):
    item = QtGui.QListWidgetItem(self.ui.listWidget)
    item_widget = progress.Ui_("It works")
    item.setSizeHint(item_widget.sizeHint())
    self.ui.listWidget.addItem(item)
    self.ui.listWidget.setItemWidget(item,item_widget)

if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  myapp = MyForm()
  myapp.show()
  sys.exit(app.exec_())
