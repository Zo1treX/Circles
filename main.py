import random
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Drawer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('circles')
        self.btn = QPushButton('Draw', self)
        self.btn.move(70, 150)
        self.btn.resize(60, 40)
        self.paint = False
        self.btn.clicked.connect(self.painting)

    def paintEvent(self, event):
        if self.paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def painting(self):
        self.paint = True
        self.repaint()

    def draw(self, qp):
        radius = random.randint(0, 200)
        r = 255
        g = 255
        b = 0
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(random.randint(0, 200), random.randint(0, 200), radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Drawer()
    ex.show()
    sys.exit(app.exec())