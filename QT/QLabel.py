#  QLable控件
#  setAlignment() 设置文本的对齐方式
#  setIndent() 设置文本缩进
#  text() 获取文本内容
#  setBuddy() 设置伙伴关系
#  selectedText() 返回所选择的字符
#  setWordWrap() 设置是否允许运行

# QLable常用的信号（事件）：
# 1.当鼠标滑过QLable控件时触发： linkHovered
# 2.当鼠标单击QLable控件时触发： linkActivated


from cProfile import label
from tkinter import font
from turtle import color
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QMainWindow
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtCore import Qt
import sys

class QLableDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)
        
        label1.setText("<font color=yellow>这是一个文本标签.</font>")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, Qt.GlobalColor.blue) #设置背景色
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        label2.setText("<a herf='#'>欢迎使用Python GUI程序</a>")
        
        label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap("C:/Users/lei.gao/Pictures/1.jpg"))
        
        # 如果设为True， 用浏览器打开网页， 如果是False, 调用函数
        label4.setOpenExternalLinks(True)
        label4.setText("<a href='https:www.baidu.com'>百度搜索</a>")
        label4.setAlignment(Qt.AlignmentFlag.AlignRight)
        label4.setToolTip('这是一个超级链接')
        
        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(label1)
        vbox_layout.addWidget(label2)
        vbox_layout.addWidget(label3)
        vbox_layout.addWidget(label4)
        
        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClick)
        
        # main_frame = QMainWindow()
        # main_frame.setLayout(vbox_layout)
        self.setLayout(vbox_layout)
        self.setWindowTitle('QLabel控件演示')
        
        
    def linkHovered(self):
        print('当鼠标滑过lable2标签时')
    
    def linkClick(self):
        print('当鼠标单击label4标签时')
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QLableDemo()
    main.show()
    
    sys.exit(app.exec_())