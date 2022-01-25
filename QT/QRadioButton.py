# 单选按钮控件(QDadioButton)

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
# from PyQt5.QtCore import *
import sys

class QDadioButtonDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('QDadioButton控件演示')
        self.resize(300, 500)
        
        mainLayout = QVBoxLayout()
        
        self.btn1 = QRadioButton('button01')
        self.btn1.toggled.connect(lambda:self.buttonInfo(self.btn1))
        
        self.btn2 = QRadioButton('button02')
        self.btn2.toggled.connect(lambda:self.buttonInfo(self.btn2))
        
        mainLayout.addWidget(self.btn1)
        mainLayout.addWidget(self.btn2)
        
        self.setLayout(mainLayout)
        
    def buttonInfo(self, btn):
        btnStatus = btn.isChecked()
        if btnStatus:
            print('{0}被选中'.format(btn.text()))
        else:
            print('{0}未被选中'.format(btn.text()))
            
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDadioButtonDemo()
    main.show()
    sys.exit(app.exec_())
    