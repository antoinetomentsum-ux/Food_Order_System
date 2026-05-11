import unittest

from patterns.singleton import RestaurantManager


class TestSingleton(unittest.TestCase):

    def setUp(self):
        manager = RestaurantManager.get_instance()
        manager.orders.clear()

    def test_single_instance(self):

        manager1 = RestaurantManager.get_instance()
        manager2 = RestaurantManager.get_instance()

        self.assertIs(manager1, manager2)

    def test_shared_orders(self):

        manager1 = RestaurantManager.get_instance()
        manager2 = RestaurantManager.get_instance()

        manager1.add_order("Pizza Order")

        self.assertEqual(len(manager2.list_orders()), 1)

    def test_instance_not_none(self):

        manager = RestaurantManager.get_instance()

        self.assertIsNotNone(manager)

