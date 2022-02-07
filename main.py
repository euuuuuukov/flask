from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from random import randint
import sys


class Main(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btn.clicked.connect(self.update)

    def paintEvent(self, event):
       painter = QPainter()
       painter.begin(self)
       painter.setBrush(QColor('yellow'))
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