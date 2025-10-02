from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass


class CreditCardPayment(PaymentMethod):
    def pay(self, amount: float) -> str:
        return f"Оплата {amount} с помощью кредитной карты"


class EWalletPayment(PaymentMethod):
    def pay(self, amount: float) -> str:
        return f"Оплата {amount} через электронный кошелек"


class PaymentPlatform:
    def __int__(self, method: PaymentMethod) -> None:
        self._method = method

    def make_payment(self, amount: float) -> str:
        pass


class MobileAppPlatform(PaymentPlatform):
    def make_payment(self, amount: float) -> str:
        return f"Мобильное приложение: {self._method.pay(amount)}"


class WebPlatform(PaymentPlatform):
    def make_payment(self, amount: float) -> str:
        return f"Веб-сайт: {self._method.pay(amount)}"


def client_voice(platform: PaymentPlatform, amount: float) -> None:
    print(platform.make_payment(amount))

if __name__ == "__main__":
    credit_card = CreditCardPayment()
    ewallet = EWalletPayment()

    mobile_credit = MobileAppPlatform(credit_card)
    web_credit = WebPlatform(credit_card)

    mobile_ewallet = MobileAppPlatform(ewallet)
    web_ewallet = WebPlatform(ewallet)

    print("Мобильное приложение + Кредитная карта:")
    client_voice(mobile_credit, 100.00)