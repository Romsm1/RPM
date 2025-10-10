class Component:
    def operation(self) -> str:
        pass


class TextPrinter(Component):
    def __init__(self, text: str) -> None:
        self.text = text

    def operation(self) -> str:
        return self.text


class Decorator(Component):
    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component

    def operation(self) -> str:
        return self._component.operation()


class UpperCaseDecorator(Decorator):
    def operation(self) -> str:
        return self.component.operation().upper()


class BorderDecorator(Decorator):
    def operation(self) -> str:
        text = self.component.operation()
        line = "+" * (len(text) + 4)
        return f"{line}\n| {text} |\n{line}"


class ExclamationDecorator(Decorator):
    def operation(self) -> str:
        return self.component.operation() + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"


test = TextPrinter("Текст для демонстрации работы")

print("Вывод оригинального текста: ")
print(test.operation())
print()

upper_text = UpperCaseDecorator(test)
print("Текст в верхнем регистре: ")
print(upper_text.operation())
print()

excl_text = ExclamationDecorator(test)
print("Текст с восклицательными знаками: ")
print(excl_text.operation())
print()

border_text = BorderDecorator(test)
print("Текст в рамке: ")
print(border_text.operation())
print()

combo1 = ExclamationDecorator(UpperCaseDecorator(test))
print("Текст с восклицательными знаками и в верхнем регистре: ")
print(combo1.operation())
print()

full_combo = BorderDecorator(UpperCaseDecorator(ExclamationDecorator(test)))
print("Текст со всеми декораторами: ")
print(full_combo.operation())
