from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from random import randint
import sys


class Ui_MyGitWidget(object):
    def setupUi(self, MyGitWidget):
        if not MyGitWidget.objectName():
            MyGitWidget.setObjectName(u"MyGitWidget")
        
        MyGitWidget.resize(755, 528)
        self.centralwidget = QWidget(MyGitWidget)
        self.centralwidget.setObjectName(u"centralwidget")
        self.drawButton = QPushButton(self.centralwidget)
        self.drawButton.setObjectName(u"drawButton")
        self.drawButton.setGeometry(QRect(10, 490, 111, 23))
        MyGitWidget.setCentralWidget(self.centralwidget)
      
        self.retranslateUi(MyGitWidget)
        QMetaObject.connectSlotsByName(MyGitWidget)

    def retranslateUi(self, MyGitWidget):
        MyGitWidget.setWindowTitle(QCoreApplication.translate("MyGitWidget", u"MainWindow", None))
        self.drawButton.setText(QCoreApplication.translate("MyGitWidget", u"\u041d\u0430\u0440\u0438\u0441\u043e\u0432\u0430\u0442\u044c", None))


class YellowCircles(QMainWindow, Ui_MyGitWidget):
  def __init__(self):
    super(YellowCircles, self).__init__()
    self.setupUi()
    self.retranslateUi()

    self.drawButton.clicked.connect(self.draw_yellow_circle)

  def draw_yellow_circle(self):
    width, height = self.geometry().width(), self.geometry().height()
    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    random_position = (randint(0, width), randint(0, height))
    random_diameter = randint(30, 90)

    painter = QPainter(self)
    painter.setPen(QColor(*random_color))
    painter.drawEllipse(*random_position, random_diameter, random_diameter)


if __name__ == '__main__':
  application = QApplication(sys.argv)
  task = YellowCircles()
  task.show()
  sys.exit(application.exec_())
