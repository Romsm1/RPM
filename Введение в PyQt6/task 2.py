import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class Clicker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Кликер")
        self.setFixedSize(250, 100)

        self.counter = 0

        self.label = QLabel(str(self.counter), self)
        self.label.setFont(QFont("Arial", 24))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button = QPushButton("Кликни", self)
        self.button.clicked.connect(self.increment)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def increment(self):
        self.counter += 1
        self.label.setText(str(self.counter))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Clicker()
    window.show()
    sys.exit(app.exec())
