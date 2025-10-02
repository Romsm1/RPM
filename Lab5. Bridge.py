from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass

class CreditCardPayment(PaymentMethod):
    def pay(self, amount: float) -> str:
        return f"Оплата {amount} CHF с помощью кредитной карты."

class EWalletPayment(PaymentMethod):
    def pay(self, amount: float) -> str:
        return f"Оплата {amount} CHF через электронный кошелёк."

class PaymentPlatform:
    def __init__(self, method: PaymentMethod) -> None:
        self.method = method

    def make_payment(self, amount: float) -> str:
        pass

class MobileAppPlatform(PaymentPlatform):
    def make_payment(self, amount: float) -> str:
        return f"Мобильное приложение: {self.method.pay(amount)}"

class WebPlatform(PaymentPlatform):
    def make_payment(self, amount: float) -> str:
        return f"Веб-сайт: {self.method.pay(amount)}"

def client_code(platform: PaymentPlatform, amount: float) -> None:
    print(platform.make_payment(amount))

if __name__ == "__main__":
    credit_card = CreditCardPayment()
    ewallet = EWalletPayment()

    mobile_credit = MobileAppPlatform(credit_card)
    web_credit = WebPlatform(credit_card)

    mobile_ewallet = MobileAppPlatform(ewallet)
    web_ewallet = WebPlatform(ewallet)

    print("Мобильное приложение + Кредитная карта:")
    client_code(mobile_credit, 100.0)

    print("Веб-сайт + Кредитная карта:")
    client_code(web_credit, 150.0)

    print("Мобильное приложение + Электронный кошелёк:")
    client_code(mobile_ewallet, 75.5)

    print("Веб-сайт + Электронный кошелёк:")
    client_code(web_ewallet, 200.0)
