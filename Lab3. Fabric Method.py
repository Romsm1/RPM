from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def save(self, filename: str):
        pass

class PDFDocument(Document):
    def save(self, filename: str):
        with open(f"{filename}.pdf", "w", encoding="utf-8") as file:
            file.write("PDF-документ создан.\n")
        print(f"Сохранено: {filename}.pdf")

class WordDocument(Document):
    def save(self, filename: str):
        with open(f"{filename}.docx", "w", encoding="utf-8") as file:
            file.write("Word-документ создан.\n")
        print(f"Сохранено: {filename}.docx")

class ExcelDocument(Document):
    def save(self, filename: str):
        with open(f"{filename}.xlsx", "w", encoding="utf-8") as file:
            file.write("Excel-документ создан.\n")
        print(f"Сохранено: {filename}.xlsx")

class DocumentFactory(ABC):
    @abstractmethod
    def create_document(self) -> Document:
        pass

class PDFDocumentFactory(DocumentFactory):
    def create_document(self) -> Document:
        print("Создание PDF-документа...")
        return PDFDocument()

class WordDocumentFactory(DocumentFactory):
    def create_document(self) -> Document:
        print("Создание Word-документа...")
        return WordDocument()

class ExcelDocumentFactory(DocumentFactory):
    def create_document(self) -> Document:
        print("Создание Excel-документа...")
        return ExcelDocument()

if __name__ == "__main__":
    print("Добро пожаловать! Выберите тип документа: pdf, word или excel.")

    factories = {
        "pdf": PDFDocumentFactory(),
        "word": WordDocumentFactory(),
        "excel": ExcelDocumentFactory()
    }

    while True:
        choice = input("Ваш выбор: ").strip().lower()

        if choice in factories:
            factory = factories[choice]
            document = factory.create_document()
            filename = input("Введите имя файла (без расширения): ").strip()
            document.save(filename)
            break
        else:
            print("Неизвестный тип. Попробуйте снова.")

