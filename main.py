from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

from random import randint
import sys


class YellowCircles(QMainWindow):
    def __init__(self):
        super(YellowCircles, self).__init__()
        uic.loadUi('UI.ui', self)

        self.go_draw = False

        self.drawButton.clicked.connect(self.draw_yellow_circle)

    def draw_yellow_circle(self):
        self.go_draw = True
        self.update()

    def paintEvent(self, event):
        if self.go_draw:
            self.go_draw = False
            width, height = self.geometry().width(), self.geometry().height()
            random_position = [randint(0, width), randint(0, height)]
            random_diameter = randint(64, 90)

            painter = QPainter(self)
            painter.setBrush(QColor(255, 255, 0))
            painter.drawEllipse(*random_position, random_diameter, random_diameter)

        return super(YellowCircles, self).paintEvent(event)


if __name__ == '__main__':
  application = QApplication(sys.argv)
  task = YellowCircles()
  task.show()
  sys.exit(application.exec_())
