import sys
import random
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QLineEdit, QPushButton, QMessageBox
)

class RandomNumberApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300, 200)
        self.setWindowTitle("Генератор случайных чисел")

        central = QWidget()
        layout = QVBoxLayout()

        self.start_input = QLineEdit()
        self.start_input.setPlaceholderText("Начало диапазона")
        self.end_input = QLineEdit()
        self.end_input.setPlaceholderText("Конец диапазона")

        generate_btn = QPushButton("Сгенерировать")
        generate_btn.clicked.connect(self.show_random_number)

        layout.addWidget(self.start_input)
        layout.addWidget(self.end_input)
        layout.addWidget(generate_btn)
        central.setLayout(layout)
        self.setCentralWidget(central)

    def show_random_number(self):
        try:
            start = int(self.start_input.text())
            end = int(self.end_input.text())
            if start > end:
                raise ValueError("Начало должно быть меньше или равно концу.")
            number = random.randint(start, end)
            QMessageBox.information(self, "Результат", f"Результат: {number}")
        except ValueError as e:
            QMessageBox.warning(self, "Ошибка", f"Неверный ввод! {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RandomNumberApp()
    window.show()
    sys.exit(app.exec())