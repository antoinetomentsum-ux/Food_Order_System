from threading import Lock
from models.order import Order

class RestaurantManager:

    _instance = None
    _lock = Lock()

    def __new__(cls):

        if cls._instance is None:

            with cls._lock:

                if cls._instance is None:

                    cls._instance = super().__new__(cls)

                    cls._instance.orders = []

        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls()

    def add_order(self, order: Order):
        self.orders.append(Order)

    def list_orders(self):
        return self.orders