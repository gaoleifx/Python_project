from msilib.schema import Icon
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
from PySide2.QtGui import QIcon

class IconForm(QMainWindow):
    def __init__(self):
        super(IconForm, self).__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口大小
        self.setGeometry(300, 300, 250, 250)
        # 设置窗口标题
        self.setWindowTitle('设置窗口图标')
        # 设置窗口图标
        self.setWindowIcon(QIcon())