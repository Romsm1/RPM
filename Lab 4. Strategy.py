from abc import ABC, abstractmethod


class DeliveryStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, weight: float, distance: float) -> float:
        pass

    def name(self):
        pass


class CourierDelivery(DeliveryStrategy):
    def calculate_cost(self, weight: float, distance: float) -> float:
        return 150 + 15 * weight + 15 * distance

    def name(self) -> str:
        return "Доставка курьером"


class PostalDelivery(DeliveryStrategy):
    def calculate_cost(self, weight: float, distance: float) -> float:
        return 50 + 10 * weight + 0.2 * distance

    def name(self) -> str:
        return "Доставка почтой"


class DroneDelivery(DeliveryStrategy):
    def calculate_cost(self, weight: float, distance: float) -> float:
        return 300 + 25 * weight + 10 * distance

    def name(self) -> str:
        return "Доставка дроном"


class DeliveryContext:
    def __init__(self, strategy: DeliveryStrategy):
        self._strategy = strategy

    def set_stratedy(self, strategy: DeliveryStrategy):
        self._strategy = strategy

    def get_strategy_name(self) -> None:
        return self._strategy.name()

    def calculate(self, weight: float, distance: float) -> float:
        return self._strategy.calculate_cost(weight, distance)


def main():
    print("Выберите номер желаемой стратегии доставки: ")
    print("1 - Доставка курьером")
    print("2 - Доставка почтой")
    print("3 - Доставка дроном")

    choice = input("Введите номер стратегии: ")
    weight = float(input("Введите вес товара (кг) - "))
    distance = float(input("Введите расстояние (км) - "))

    if choice == "1":
        strategy = CourierDelivery()
    elif choice == "2":
        strategy = PostalDelivery()
    elif choice == "3":
        strategy = DroneDelivery()
    else:
        print("Неверный выбор. Повторите еще раз.")
        return

    context = DeliveryContext(strategy)
    cost = context.calculate(weight, distance)
    strategy_name = context.get_strategy_name()
    print(f'Стоимость доставки: {cost:.2f} руб. Выбранный способ доставки: {strategy_name}')


if __name__ == "__main__":
    main()
