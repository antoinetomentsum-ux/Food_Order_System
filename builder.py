from models.order import Order
from models.food import food
from models.payment import Payment
from models.notification import Notification

class OrderBuilder:

    def __init__(self):
        self.reset()

    def reset(self):
        self._order = Order()
        return self

    def set_customer(self, name: str):
        self._order.customer_name = name
        return self

    def set_address(self, address: str):
        self._order.address = address
        return self

    def add_item(self, item: food):
        self._order.items.append(item)
        return self

    def set_payment(self, payment: Payment):
        self._order.payment_method = payment
        return self

    def set_notification(self, notification: Notification):
        self._order.notification_method = notification
        return self

    def apply_discount(self, discount: float):
        """
        Example:
        20% => 0.2
        """
        if not 0 <= discount <= 1:
            raise ValueError("Discount must be between 0 and 1.")

        self._order.discount = discount
        return self

    def set_special_note(self, note: str):
        self._order.special_note = note
        return self

    def calculate_total(self):

        total = sum(
            item.get_price()
            for item in self._order.items
        )

        total *= (1 - self._order.discount)

        self._order.total_price = int(total)

        return self

    def build(self) -> Order:

        if not self._order.customer_name:
            raise ValueError("Customer name is required.")

        if not self._order.address:
            raise ValueError("Address is required.")

        if not self._order.items:
            raise ValueError("At least one item is required.")

        if self._order.payment_method is None:
            raise ValueError("Payment method is required.")

        if self._order.notification_method is None:
            raise ValueError("Notification method is required.")

        return self._order


class OrderDirector:

    def __init__(self, builder: OrderBuilder):
        self.builder = builder

    def create_simple_order(self, item: food) -> Order:

        return (self.builder.reset().set_customer().set_address().add_item(item).set_payment().set_notification().apply_discount().set_special_note().calculate_total().build())
