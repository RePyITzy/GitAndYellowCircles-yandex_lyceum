from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter, Qt
from PyQt5 import uic

from random import randint


class YellowCircles(QMainWindow):
  def __init__(self):
    super(YellowCircles, self).__init__()
    uic.loadUi('UI.ui', self)

    self.drawButton.clicked.connect(self.draw_yellow_circle)

  def draw_yellow_circle(self):
    width, height = self.geometry().width(), self.geometry().height()
    random_position = (randint(0, width), randint(0, height))
    random_diameter = randint(30, 90)

    painter = QPainter(self)
    painter.setPen(Qt.Yellow)
    painter.drawEllipse(*random_position, *random_diameter)
