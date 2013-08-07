
import os
import sys
from PySide.QtGui import *            #@UnusedWildImport
from PySide.QtCore import *           #@UnusedWildImport
from PySide.QtUiTools import *        #@UnusedWildImport
from pprint import pprint             #@UnusedImport


# TODO: closeEvent() is never called here with the event argument.  Why?


MAIN_WINDOW_UI_FILE = "simple_main_ui.ui"
MOTORX_UI_FILE = "motorx.ui"
ORG_NAME = 'SimpleMainUi'
APP_NAME = 'simple main window from a ui file'


def loadUiFile(uifilename):
    '''load a user interface specification from a .ui file'''
    if not os.path.exists(uifilename):
        msg = "file not found: %s", uifilename
        raise IOError, msg
    uifile = QFile(uifilename)
    uifile.open(QFile.ReadOnly)
    loader = QUiLoader()
    myWidget = loader.load(uifile, None)
    uifile.close()
    #print myWidget.findChild(QAction, "actionAboutQt")
    return myWidget


class RunMainWindow:
    
    def __init__(self, app = None):
        self.mainWin = loadUiFile(MAIN_WINDOW_UI_FILE)
        self.assignActions(self.mainWin)
        #pprint(dir(myWidget))
        self.mainWin.statusBar().showMessage(self.mainWin.tr('Ready'))
        self.mainWin.closeEvent = self.closeEvent
        app.aboutToQuit.connect(self.closeEvent)
        
        if True:
            self.m1 = loadUiFile(MOTORX_UI_FILE)
            self.mainWin.setCentralWidget(self.m1)
        else:
            widg = QWidget()
            self.mainWin.setCentralWidget(widg)
            
            layout = QHBoxLayout()
            widg.setLayout(layout)
            
            self.m1 = loadUiFile(MOTORX_UI_FILE)
            layout.addWidget(self.m1, 0, 1)
    
    def show(self):
        self.mainWin.show()

    def assignActions(self, parent):
        '''connect actions on the UI components with methods'''
        parent.actionNew.triggered.connect(self.doNew)
        parent.actionExit.triggered.connect(parent.close)
        parent.actionExit.setShortcuts(QKeySequence.Quit)
        #parent.closeEvent = self.closeEvent

    def doNew(self):
        print "selected: New"
    
    def closeEvent(self, event = None):
        print "closeEvent", event
#        if self.maybeSave(self.mainWin):
#            self.writeSettings()
#            event.accept()
#        else:
#            event.ignore()
    
    def save(self):
        if len(self.curFile) == 0:
            return self.saveAs()
        return self.saveFile(self.curFile)
    
    def saveAs(self):
        fileName = QFileDialog.getSaveFileName(self)
        if len(fileName) == 0:
            return False
        return self.saveFile(fileName)

    def writeSettings(self):
        self.settings = QSettings(ORG_NAME, APP_NAME)
        self.settings.setValue('pos', self.pos)
        self.settings.setValue('size', self.size)

    def maybeSave(self, parent):
        if parent.textEdit.document().isModified():
            ret = QMessageBox().warning(parent, parent.tr('Application'),
                                         parent.tr("The document has been modified.\n Do you want to save your changes?"),
                                         QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
                                        )
            if ret == QMessageBox.Save:
                return self.save()
            elif ret == QMessageBox.Cancel:
                return False
        return True

    def saveFile(self, fileName): pass


def main():
    qapp = QApplication(sys.argv)
    mainWin = RunMainWindow(qapp)
    mainWin.show()
    sys.exit(qapp.exec_())


if __name__ == '__main__':
    main()
