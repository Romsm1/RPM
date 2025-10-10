class Observer:
    def update(self, rate: float) -> None:
        pass


class Bank(Observer):
    def update(self, rate: float) -> None:
        print(f"Банк получил актуальный курс: {rate}")


class ExchangeOffice(Observer):
    def update(self, rate: float) -> None:
        print(f"Обменник получил актуальный курс: {rate}")


class Investor(Observer):
    def update(self, rate: float) -> None:
        print(f"Инвестор получил актуальный курс: {rate}")


class CurrencyExchange:
    def __init__(self) -> None:
        self._rate: float = 0.0
        self._subscribers: list[Observer] = []

    def subscribe(self, subscriber: "Observer") -> None:
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber: "Observer") -> None:
        self._subscribers.remove(subscriber)

    def set_rate(self, new_rate: float) -> None:
        print(f"Новый курс валют: {new_rate}")
        self._rate = new_rate
        self._notify()

    def _notify(self) -> None:
        for subscriber in self._subscribers:
            subscriber.update(self._rate)


if __name__ == "__main__":
    exchange = CurrencyExchange()

    bank = Bank()
    office = ExchangeOffice()
    investor = Investor()

    exchange.subscribe(bank)
    exchange.subscribe(office)
    exchange.subscribe(investor)

    exchange.set_rate(69.9)

    exchange.unsubscribe(bank)
    exchange.set_rate(37.25)
