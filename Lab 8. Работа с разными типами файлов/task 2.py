import sys

from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
    QHBoxLayout, QFileDialog, QTextEdit, QLineEdit
)


class TextEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Text Editor")

        self.filename_edit = QLineEdit()
        self.text_edit = QTextEdit()

        self.char_label = QLabel("Всего символов: ")
        self.word_label = QLabel("Всего слов: ")
        self.longest_label = QLabel("Самое длинное слово: ")
        self.shortest_label = QLabel("Самое короткое слово: ")
        self.freq_label = QLabel("Самое частое слово: ")

        open_btn = QPushButton("Открыть")
        open_btn.clicked.connect(self.open_file)

        save_btn = QPushButton("Сохранить")
        save_btn.clicked.connect(self.save_file)

        save_as_btn = QPushButton("Сохранить как")
        save_as_btn.clicked.connect(self.save_file_as)

        self.text_edit.textChanged.connect(self.update_stats)

        top_layout = QHBoxLayout()
        top_layout.addWidget(QLabel("Имя файла:"))
        top_layout.addWidget(self.filename_edit)

        stats_layout = QVBoxLayout()
        stats_layout.addWidget(self.char_label)
        stats_layout.addWidget(self.word_label)
        stats_layout.addWidget(self.longest_label)
        stats_layout.addWidget(self.shortest_label)
        stats_layout.addWidget(self.freq_label)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(open_btn)
        btn_layout.addWidget(save_btn)
        btn_layout.addWidget(save_as_btn)

        layout = QVBoxLayout()
        layout.addLayout(top_layout)
        layout.addWidget(self.text_edit)
        layout.addLayout(stats_layout)
        layout.addLayout(btn_layout)
        self.setLayout(layout)

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Текстовые файлы (*.txt)")
        if path:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    text = f.read()
                self.text_edit.setPlainText(text)
                self.filename_edit.setText(path)
                self.update_stats()
            except Exception:
                self.text_edit.setPlainText("Ошибка при загрузке файла.")
                self.filename_edit.setText("")

    def save_file(self):
        path = self.filename_edit.text()
        if path:
            try:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(self.text_edit.toPlainText())
            except Exception:
                pass

    def save_file_as(self):
        path, _ = QFileDialog.getSaveFileName(self, "Сохранить как", "", "Текстовые файлы (*.txt)")
        if path:
            self.filename_edit.setText(path)
            self.save_file()

    def update_stats(self):
        text = self.text_edit.toPlainText()
        raw_words = text.replace('\n', ' ').split()
        words = []

        for w in raw_words:
            if any(c.isalpha() for c in w):
                cleaned = ''.join(c for c in w if c.isalpha() or c == '-')
                words.append(cleaned)

        self.char_label.setText(f"Всего символов: {len(text)}")
        self.word_label.setText(f"Всего слов: {len(words)}")

        if words:
            self.longest_label.setText(f"Самое длинное слово: {max(words, key=len)}")
            self.shortest_label.setText(f"Самое короткое слово: {min(words, key=len)}")

            freq = {}
            for word in words:
                freq[word] = freq.get(word, 0) + 1
            most_common_word = max(freq, key=freq.get)
            self.freq_label.setText(f"Самое частое слово: {most_common_word}")
        else:
            self.longest_label.setText("Самое длинное слово: ")
            self.shortest_label.setText("Самое короткое слово: ")
            self.freq_label.setText("Самое частое слово: ")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = TextEditor()
    editor.resize(400, 600)
    editor.show()
    sys.exit(app.exec())
