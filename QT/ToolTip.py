# 显示控件提示消息

from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QToolTip, QPushButton, QWidget
from PyQt5.QtGui import QFont
import sys

class ToolTipFrom(QMainWindow):
    def __init__(self):
        super(ToolTipFrom, self).__init__()
        self.initUI()
        
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 12))
        self.setToolTip('今天是<b>星期五</b>')
        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle('设置窗口提示消息')
        
        self.button0 = QPushButton('点击关闭窗口')
        # self.button0.clicked.connect(self.CloseWin())
        self.button0.setToolTip('This is a button for close window')
        
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.button0)
        
        mainFrame = QWidget()
        mainFrame.setLayout(main_layout)
        self.setCentralWidget(mainFrame)        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ToolTipFrom()
    main.show()
    
    sys.exit(app.exec_())