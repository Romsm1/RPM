class Coffee:
    @property
    def cost(self) -> float:
        return 120.0

    @property
    def description(self) -> str:
        return "Обычный кофе"


class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    @property
    def cost(self) -> float:
        return self._coffee.cost

    @property
    def description(self) -> str:
        return self._coffee.description


class MilkDecorator(CoffeeDecorator):
    @property
    def cost(self) -> float:
        return self._coffee.cost + 45.0

    @property
    def description(self) -> str:
        return self._coffee.description + ", молоко"


class SugarDecorator(CoffeeDecorator):
    @property
    def cost(self) -> float:
        return self._coffee.cost + 15.5

    @property
    def description(self) -> str:
        return self._coffee.description + ", сахар"


class SyrupDecorator(CoffeeDecorator):
    @property
    def cost(self) -> float:
        return self._coffee.cost + 65.0

    @property
    def description(self) -> str:
        return self._coffee.description + ", сироп"


def main() -> None:
    coffee: Coffee = Coffee()
    milk_added = False
    sugar_added = False
    syrup_added = False

    print("Добро пожаловать в онлайн-кофейню!")
    print("Базовый напиток: Обычный кофе (120.0 руб.)")

    while True:
        print("\nВыберите добавку:")
        print("1 - Молоко (+45.0 руб.)")
        print("2 - Сахар (+15.5 руб.)")
        print("3 - Сироп (+65.0 руб.)")
        print("0 - Завершить заказ")

        choice = input("Ваш выбор: ").strip()

        if choice == "0":
            break
        elif choice == "1":
            if milk_added:
                print("Молоко уже добавлено.")
            else:
                coffee = MilkDecorator(coffee)
                milk_added = True
                print("Добавлено: молоко")
        elif choice == "2":
            if sugar_added:
                print("Сахар уже добавлен.")
            else:
                coffee = SugarDecorator(coffee)
                sugar_added = True
                print("Добавлено: сахар")
        elif choice == "3":
            if syrup_added:
                print("Сироп уже добавлен.")
            else:
                coffee = SyrupDecorator(coffee)
                syrup_added = True
                print("Добавлено: сироп")
        else:
            print("Неверный выбор. Попробуйте снова.")

    print("\nВаш напиток готов!")
    print("Описание:", coffee.description)
    print("Итоговая цена:", coffee.cost, "руб.")


if __name__ == "__main__":
    main()
