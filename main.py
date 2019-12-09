import sys
from random import randrange
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5.QtCore import QRectF


def draw_ellipse(qp):
    x = randrange(1000)
    y = randrange(1000)
    radius = randrange(1080)
    ellipse_x = x - radius // 2
    ellipse_y = y - radius // 2
    rectangle = QRectF(ellipse_x, ellipse_y, radius, radius)
    qp.setBrush(QColor(255, 255, 0))
    qp.drawEllipse(rectangle)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Git и желтые окружности')
        self.show()
        self.Ground.setPixmap(QPixmap(1000, 1000))
        self.DrawCircles.clicked.connect(self.draw)

    def draw(self):
        self.DrawCircles.hide()
        qp = QPainter(self.Ground.pixmap())
        qp.begin(self)
        for i in range(randrange(1, 21)):
            draw_ellipse(qp)
        qp.end()
        self.update()


app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
