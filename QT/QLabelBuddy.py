# QLabelBuddy

from cgitb import text
from PyQt5.QtWidgets import *
import sys

class QLabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        textLabel = QLabel("&Name", self) #&Name 是将热键设置为alt+N
        textLineEdit = QLineEdit(self)
        
        textLabel.setBuddy(textLineEdit)
        
        passwordLabel = QLabel('&Password', self)
        passwordLineEdit = QLineEdit(self)
        
        passwordLabel.setBuddy(passwordLineEdit)
        
        btnOK = QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')
        
        mainLayout = QGridLayout(self)
        mainLayout.addWidget(textLabel, 0, 0)
        mainLayout.addWidget(textLineEdit, 0, 1, 1, 2)
        
        mainLayout.addWidget(passwordLabel, 1, 0)
        mainLayout.addWidget(passwordLineEdit, 1, 1, 1, 2)
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelBuddy()
    main.show()
    
    sys.exit(app.exec_())