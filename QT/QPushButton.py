# QPushButton
# 父类QAbstractButton

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class QPushButtonDemo(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('QPushButton控件演示')
        self.resize(300, 400)
        
        mainLayout = QVBoxLayout()
        
        self.btn1 = QPushButton('First Button')
        self.btn1.setText('第一个按钮')
        self.btn1.setCheckable(True)
        self.btn1.toggle()
        self.btn1.clicked.connect(lambda:self.btnInfo(self.btn1))
        self.btn1.clicked.connect(self.btnStatus)
        
        mainLayout.addWidget(self.btn1)
        
        self.btn2 = QPushButton('图标按钮')
        self.btn2.setIcon(QIcon(QPixmap('E:/0.ART_houdini/HDAS/icons/pilot.png')))
        
        mainLayout.addWidget(self.btn2)
        
        self.btn3 = QPushButton('不可用按钮')
        self.btn3.setEnabled(False)
        
        mainLayout.addWidget(self.btn3)
        
        self.btn4 = QPushButton('&MyButton')
        self.btn4.setDefault(True)
        self.btn4.clicked.connect(lambda:self.btnInfo(self.btn4))
        
        mainLayout.addWidget(self.btn4)
        
        self.setLayout(mainLayout)
        
    def btnStatus(self):
        if self.btn1.isChecked():
            print('按钮被选中状态')
        else:
            print('按钮未被选中状态')
            
    def btnInfo(self, btn):
        print('{0}'.format(btn.text()))
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QPushButtonDemo()
    main.show()
    sys.exit(app.exec_())