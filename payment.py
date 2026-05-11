from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount: int) -> str:
        pass


class OnlineCardPayment(Payment):

    def pay(self, amount: int) -> str:
        return f"Paid {amount:} T using Online Card."


class CashPayment(Payment):

    def pay(self, amount: int) -> str:
        return f"Cash payment selected for {amount:} T."