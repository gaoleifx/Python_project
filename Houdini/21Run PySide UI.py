#Run PySide UI
#Create and save a UI file with QT Designer. It could be just a blank widget (but not Main Window). In Houdini run this code in Python Source Editor window:
# Run *ui file in Houdini

import hou
from PySide2 import QtCore, QtUiTools, QtWidgets

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super(MyWidget,self).__init__()
        ui_file = 'C:/path/to/file.ui'
        self.ui = QtUiTools.QUiLoader().load(ui_file, parentWidget=self)
        self.setParent(hou.ui.mainQtWindow(), QtCore.Qt.Window)

win = MyWidget()
win.show()