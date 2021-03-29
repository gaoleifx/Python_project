#Run compiled PySide2 UI
# This is the better option (then running *.ui files, see below)!
# Create with QT Designer interface.ui file and save it somewhere where Houdini Python will see it (or add the path to the file to os.environ['PYTHONPATH']). Name main widget object (QWidget) "MyInterface". Create compile_ui.bat file:

# set UIFILE=%1
# set UIDIR=%~dp$PATH:1
# set FILENAME=%~n1
# set SNAME=%UIDIR%%FILENAME%.py


# CALL C:\Python27\Scripts\pyside2-uic.exe %UIFILE% -o %SNAME%
# Drag and drop interface.ui on compile_ui.bat to get interface.py
# In Houdini run this code in Python Source Editor window:

import os
import hou

os.environ['PYTHONPATH']  = 'path to compiled interface.py'

from PySide2 import QtCore, QtUiTools, QtWidgets
import interface


class Window(QtWidgets.QDialog, interface.Ui_MyInterface):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.setParent(hou.ui.mainQtWindow(), QtCore.Qt.Window)

        self.pushButton.clicked.connect(self.prn)

    def prn(self):
        print 'OLA'


win = Window()
win.show()