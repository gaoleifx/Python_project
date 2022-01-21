from PyQt5.QtWidgets import QMainWindow,QPushButton,QApplication,QToolTip,QHBoxLayout,QWidget
import sys

class QuitApp(QMainWindow):
    def __init__(self):
        super(QuitApp, self).__init__()
        self.resize(300, 300)
        self.setWindowTitle('这是一个简单的测试窗口')
        self.initUI()
        
    def initUI(self):
        self.button0 = QPushButton('Close The Application')
        self.button0.setToolTip('this is a button for close the application')
        self.button0.clicked.connect(self.onClickedButton)
        
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.button0)
        
        mainFrame = QWidget()
        mainFrame.setLayout(main_layout)
        self.setCentralWidget(mainFrame)
        
    def onClickedButton(self):
        # sender = self.sender()
        # print(sender.text() + ' 按钮被按下')
        app = QApplication.instance()
        app.quit()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QuitApp()
    main.show()
    
    sys.exit(app.exec_())
        
        
        
        