import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class RandomNumberApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Генератор случайных чисел")
        self.setFixedSize(250, 100)

        self.label = QLabel("Нажмите кнопку", self)
        self.label.setFont(QFont("Arial", 16))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button = QPushButton("Сгенерировать число", self)
        self.button.setFont(QFont("Arial", 12))
        self.button.clicked.connect(self.generate_number)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def generate_number(self):
        number = random.randint(1, 1000)
        self.label.setText(f"Случайное число: {number}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RandomNumberApp()
    window.show()
    sys.exit(app.exec())
