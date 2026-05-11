from abc import ABC, abstractmethod
from models.food import (food, Burger, Pizza, Salad)

class FoodFactory(ABC):

    @abstractmethod
    def create_food(self) -> food:
        pass


class PizzaFactory(FoodFactory):

    def create_food(self) -> food:
        return Pizza()


class BurgerFactory(FoodFactory):

    def create_food(self) -> food:
        return Burger()


class SaladFactory(FoodFactory):

    def create_food(self) -> food:
        return Salad()




