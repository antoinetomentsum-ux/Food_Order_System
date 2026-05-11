import unittest

from patterns.abstract_factory import (EconomyMealFactory,LuxuryMealFactory)


class TestAbstractFactory(unittest.TestCase):

    def test_economy_drink(self):

        factory = EconomyMealFactory()

        drink = factory.create_drink()

        self.assertEqual(drink.name,"Coca")



    def test_luxury_drink(self):

        factory = LuxuryMealFactory()

        drink = factory.create_drink()

        self.assertEqual(drink.name,"Soda")


    def test_package_consistency(self):

        factory = EconomyMealFactory()

        drink = factory.create_drink()

        self.assertLess(drink.price,30000)
