from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from random import randint
import sys
from UI import Ui_Form


class Main(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.update)

    def paintEvent(self, event):
       painter = QPainter()
       painter.begin(self)
       painter.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
       x = randint(40, 533)
       y = randint(40, 366)
       r = randint(1, 40)
       painter.drawEllipse(x, y, r, r)
       painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())