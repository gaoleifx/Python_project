# 下拉列表控件(QCombobox)

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class QComboBoxDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('下拉列表控件演示')
        self.resize(300, 500)
        
        mainLayout = QVBoxLayout()
        
        self.label = QLabel('请选择名字')
        
        self.combox = QComboBox()
        self.combox.addItem('xiaoming')
        self.combox.addItem('xiaogang')
        self.combox.addItem('lidan')
        self.combox.addItems(['wangwei', 'liguo', 'xiaoqiang'])
        
        # 设置连接方式
        self.combox.currentIndexChanged.connect(self.selectedChange)
        
        mainLayout.addWidget(self.label)
        mainLayout.addWidget(self.combox)
        
        self.setLayout(mainLayout)
        
    def selectedChange(self, i):
        self.label.setText(self.combox.currentText())
        self.label.adjustSize()
        for index in range(self.combox.count()):
            print(self.combox.itemText(index))
            print(self.combox.currentText())      
               
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QComboBoxDemo()
    main.show()
    sys.exit(app.exec_())
        