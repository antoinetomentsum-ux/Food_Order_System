import unittest

from patterns.factory_method import (PizzaFactory,BurgerFactory,SaladFactory)


class TestFactoryMethod(unittest.TestCase):

    def test_pizza_factory(self):

        pizza = PizzaFactory().create_food()

        self.assertEqual(pizza.get_name(),"Pizza Margherita")

    def test_pizza_price(self):

        pizza = PizzaFactory().create_food()

        self.assertEqual( pizza.get_price(),850000)

    def test_burger_factory(self):

        burger = BurgerFactory().create_food()

        self.assertEqual(burger.get_name(),"Burger Classic")

    def test_salad_ingredients(self):

        salad = SaladFactory().create_food()

        self.assertIn("chicken",salad.get_ingredients())