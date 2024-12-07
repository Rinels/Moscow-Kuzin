import sys
import random
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QPainter, QColor

MIN_RADIUS = 10
MAX_RADIUS = 100
MIN_CIRCLE_COUNT = 2
MAX_CIRCLE_COUNT = 10

class CircleDrawer(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Git и окружности .ui', self)
        self.should_draw = False
        self.pushButton.clicked.connect(self.trigger_drawing)

    def trigger_drawing(self):
        self.should_draw = True
        self.repaint()

    def paintEvent(self, event):
        if self.should_draw:
            painter = QPainter()
            painter.begin(self)
            self.draw_circles(painter)
            painter.end()

    def draw_circles(self, painter: QPainter):
        yellow_color = QColor('#ffff00')
        painter.setPen(yellow_color)
        painter.setBrush(yellow_color)

        for _ in range(random.randint(MIN_CIRCLE_COUNT, MAX_CIRCLE_COUNT)):
            canvas_width = self.label.width()
            canvas_height = self.label.height()
            radius = random.randint(MIN_RADIUS, MAX_RADIUS)

            x_position = random.randint(0, canvas_width - radius)
            y_position = random.randint(0, canvas_height - radius)

            painter.drawEllipse(x_position, y_position, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = CircleDrawer()
    main_window.show()
    sys.exit(app.exec())