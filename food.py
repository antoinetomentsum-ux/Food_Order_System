from abc import ABC, abstractmethod




class food(ABC):

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_price(self) -> int:
        pass

    @abstractmethod
    def get_ingredients(self) -> list[str]:
        pass


class Pizza(food):

    def get_name(self) -> str:
        return "Pizza Margherita"

    def get_price(self) -> int:
        return 850000

    def get_ingredients(self) -> list[str]:
        return ["dough","tomato","mozzarella","baizl"]


class Burger(food):

    def get_name(self) -> str:
        return "Burger Classic"

    def get_price(self) -> int:
        return 700000

    def get_ingredients(self) -> list[str]:
        return ["meat", "bread", "cheese"]


class Salad(food):

    def get_name(self) -> str:
        return "Salad Caesar"

    def get_price(self) -> int:
        return 480000

    def get_ingredients(self) -> list[str]:
        return ["romaine","croutons","parmesan","chicken"]
