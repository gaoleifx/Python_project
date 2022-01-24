# QTextEdit

from PyQt5.QtWidgets import *
import sys

class QTextEditDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('QTextEdit控件演示')
        self.resize(300, 500)

        mainLayout = QGridLayout()
        
        self.textEdit = QTextEdit()
        self.btnText = QPushButton('显示text')
        self.btnHtm = QPushButton('显示htm')
        self.btnToText = QPushButton('获取文本')
        self.btnToHtm = QPushButton('获取htm')
        
        self.btnText.clicked.connect(self.on_clickedText)
        self.btnHtm.clicked.connect(self.on_clickedHtm)
        
        self.btnToText.clicked.connect(self.to_clickedText)
        self.btnToHtm.clicked.connect(self.to_clickedHtm)
        
        mainLayout.addWidget(self.textEdit)
        mainLayout.addWidget(self.btnText)
        mainLayout.addWidget(self.btnHtm)
        mainLayout.addWidget(self.btnToText)
        mainLayout.addWidget(self.btnToHtm)
        
        self.setLayout(mainLayout)
        
    def on_clickedText(self):
        self.textEdit.setPlainText('Show Text')
        
    def on_clickedHtm(self):
        self.textEdit.setHtml('<font color="blue" size="5">Hello World</font>')
        
    def to_clickedText(self):
        print(self.textEdit.toPlainText())
        
    def to_clickedHtm(self):
        print(self.textEdit.toHtml())
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QTextEditDemo()
    main.show()
    
    sys.exit(app.exec_())