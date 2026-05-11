import unittest

from patterns.builder import OrderBuilder
from patterns.factory_method import PizzaFactory
from models.payment import OnlineCardPayment
from models.notification import SMSNotification


class TestBuilder(unittest.TestCase):

    def test_set_customer(self):

        builder = OrderBuilder()

        order = (builder.set_customer("Ali").set_address("Tehran, 20metry .St").add_item(PizzaFactory().create_food()).set_payment(OnlineCardPayment()).set_notification(SMSNotification()).calculate_total().build())

        self.assertEqual(order.customer_name,"Ali")

    def test_set_address(self):

        builder = OrderBuilder()

        order = (builder.set_customer("Ali").set_address("Tehran, 20metry .St").add_item(PizzaFactory().create_food()).set_payment(OnlineCardPayment()).set_notification(SMSNotification()).calculate_total().build())

        self.assertEqual(order.address,"Tehran, 20metry .St")

    def test_add_item(self):

        builder = OrderBuilder()

        pizza = PizzaFactory().create_food()

        order = (builder.set_customer("Ali").set_address("Tehran, 20metry .St").add_item(pizza).set_payment(OnlineCardPayment()).set_notification(SMSNotification()).calculate_total().build())

        self.assertEqual(len(order.items), 1)

    def test_discount_calculation(self):

        builder = OrderBuilder()

        pizza = PizzaFactory().create_food()

        order = (
            builder.set_customer("Ali").set_address("Tehran, 20metry .St").add_item(pizza).set_payment(OnlineCardPayment()).set_notification(SMSNotification()).apply_discount(0.2).calculate_total().build())


        self.assertEqual(order.total_price, 680000)

    def test_invalid_discount(self):

        builder = OrderBuilder()

        with self.assertRaises(ValueError):

            builder.apply_discount(1.5)

    def test_missing_customer(self):

        builder = OrderBuilder()

        with self.assertRaises(ValueError):

            (builder.set_address("Tehran, 20metry .St").add_item(PizzaFactory().create_food()).set_payment(OnlineCardPayment()).set_notification(SMSNotification()).calculate_total().build())

