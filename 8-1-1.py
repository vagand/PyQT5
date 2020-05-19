## Ex 8-1-1. 점 그리기1 (drawPoint).

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Points')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_point(qp)
        qp.end()

    def draw_point(self, qp):
        qp.setPen(QPen(Qt.blue, 8))
        qp.drawPoint(self.width() / 2, self.height() / 2)
        qp.setPen(QPen(Qt.green, 12))
        qp.drawPoint(self.width() / 4, 3 * self.height() / 4)
        qp.setPen(QPen(Qt.red, 16))
        qp.drawPoint(3 * self.width() / 4, self.height() / 4)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())