# 复选框控件(QCheckBox)
# 三种状态1.未选中0 2.选中2 3.半选中1

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys

class QCheckBoxDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('QCheckBox控件演示')
        self.resize(300, 500)
        
        mainLayout = QVBoxLayout()
        
        self.cbt1 = QCheckBox('button1')
        self.cbt1.setChecked(True)
        self.cbt1.stateChanged.connect(lambda:self.buttonStatus(self.cbt1))
        
        self.cbt2 = QCheckBox('button2')
        self.cbt2.stateChanged.connect(lambda:self.buttonStatus(self.cbt2))
        
        self.cbt3 = QCheckBox('button3')
        self.cbt3.setTristate(True)
        self.cbt3.setCheckState(Qt.CheckState.PartiallyChecked)
        self.cbt3.stateChanged.connect(lambda:self.buttonStatus(self.cbt3))
        
        mainLayout.addWidget(self.cbt1)
        mainLayout.addWidget(self.cbt2)
        mainLayout.addWidget(self.cbt3)
        
        self.setLayout(mainLayout)
        
        
    def buttonStatus(self, btn):
        if btn.checkState() == 0:
            print('{0}是未选中状态{1}'.format(btn.text(), btn.isChecked()))
        if btn.checkState() == 1:
            print('{0}是半选中状态{1}'.format(btn.text(), btn.isChecked()))
        if btn.checkState() == 2:
            print('{0}是选中状态{1}'.format(btn.text(), btn.isChecked()))
            
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QCheckBoxDemo()
    main.show()
    sys.exit(app.exec_())