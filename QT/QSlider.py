# 滑块控件(QSlider)

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class QSliderDemo(QWidget):
    def __init__(self):
        super(QSliderDemo, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('滑块控件演示')
        self.resize(300, 500)
        
        mainLayout = QVBoxLayout()
        self.label = QLabel('Hello PyQt5')
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        mainLayout.addWidget(self.label)
        
        # 添加一个水平滑块控件
        self.slider = QSlider(Qt.Orientation.Horizontal)
        # 设置最小值
        self.slider.setMinimum(1)
        # 设置最大值
        self.slider.setMaximum(100)
        # 设置步长
        self.slider.setSingleStep(3)
        # 设置当前值
        self.slider.setValue(15)
        # 设置刻度的位置，刻度在下方
        self.slider.setTickPosition(QSlider.TickPosition(3))
        # 设置刻度的间隔
        self.slider.setTickInterval(6)
        # 绑定槽
        self.slider.valueChanged.connect(self.valueChange)
        
        mainLayout.addWidget(self.slider)
        self.setLayout(mainLayout)
        
    def valueChange(self):
        print(self.slider.value())
        size = self.slider.value()
        self.label.setFont(QFont('Arial', size))
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSliderDemo()
    main.show()
    sys.exit(app.exec_())