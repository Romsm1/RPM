import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
    QHBoxLayout, QFileDialog, QSlider, QComboBox
)
from PyQt6.QtGui import QPixmap, QImage, QTransform, QColor
from PyQt6.QtCore import Qt, QPoint


class ImageEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Image Editor")
        self.image = None
        self.original_image = None

        self.label = QLabel("Загрузите изображение")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.load_btn = QPushButton("Открыть файл")
        self.load_btn.clicked.connect(self.load_image)

        self.rotate_right_button = QPushButton("По часовой")
        self.rotate_right_button.clicked.connect(lambda: self.rotate_image(90))

        self.rotate_left_button = QPushButton("Против часовой")
        self.rotate_left_button.clicked.connect(lambda: self.rotate_image(-90))

        self.opacity_slider = QSlider(Qt.Orientation.Horizontal)
        self.opacity_slider.setRange(0, 255)
        self.opacity_slider.setValue(255)
        self.opacity_slider.valueChanged.connect(self.update_image)

        self.channel_selector = QComboBox()
        self.channel_selector.addItems(["RGB", "R", "G", "B"])
        self.channel_selector.currentTextChanged.connect(self.update_image)

        controls = QHBoxLayout()
        controls.addWidget(self.load_btn)
        controls.addWidget(self.rotate_left_button)
        controls.addWidget(self.rotate_right_button)

        sliders = QHBoxLayout()
        sliders.addWidget(QLabel("Прозрачность"))
        sliders.addWidget(self.opacity_slider)
        sliders.addWidget(QLabel("Цветовой канал"))
        sliders.addWidget(self.channel_selector)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addLayout(controls)
        layout.addLayout(sliders)
        self.setLayout(layout)

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "", "Изображения (*.png *.jpg *.bmp)")
        if file_path:
            self.original_image = QImage(file_path).convertToFormat(QImage.Format.Format_ARGB32)
            if self.original_image.width() > 3000 or self.original_image.height() > 3000:
                self.original_image = self.original_image.scaled(1920, 1080, Qt.AspectRatioMode.KeepAspectRatio)
            self.image = self.original_image.copy()
            self.update_image()

    def rotate_image(self, angle):
        if self.image:
            transform = QTransform().rotate(angle)
            self.image = self.image.transformed(transform)
            self.update_image()

    def update_image(self):
        if not self.image:
            return

        image = self.image.copy()
        channel = self.channel_selector.currentText()
        opacity = self.opacity_slider.value()

        for y in range(image.height()):
            for x in range(image.width()):
                point = QPoint(x, y)
                color = image.pixelColor(point)
                r, g, b = color.red(), color.green(), color.blue()

                if channel == "R":
                    color = QColor(r, 0, 0, opacity)
                elif channel == "G":
                    color = QColor(0, g, 0, opacity)
                elif channel == "B":
                    color = QColor(0, 0, b, opacity)
                else:
                    color.setAlpha(opacity)

                image.setPixelColor(point, color)

        pixmap = QPixmap.fromImage(image)
        self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.AspectRatioMode.KeepAspectRatio))

    def resizeEvent(self, event):
        self.update_image()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = ImageEditor()
    editor.resize(800, 600)
    editor.show()
    sys.exit(app.exec())
