from abc import ABC, abstractmethod
from models.food import Burger, Pizza

class Drink:
    def __init__ (self, name, price):
        self.name = name
        self.price = price


class MealPackageFactory (ABC):
    @abstractmethod
    def create_food(self):
        pass

    def creat_drink(self):
        pass

class EconomyMealFactory(MealPackageFactory):
    def create_food (self):
        return Burger()
    
    def create_drink(self):
        return Drink("Coca", 20000)


class LuxuryMealFactory(MealPackageFactory):
    def create_food(self):
        return Pizza()
    
    def create_drink(self):
    
        return Drink("Soda", 50000)