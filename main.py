from patterns.singleton import RestaurantManager
from patterns.factory_method import PizzaFactory
from patterns.abstract_factory import EconomyMealFactory
from patterns.builder import OrderBuilder, OrderDirector


def print_separator():
    print("=" * 45)


def main():

    print_separator()
    print("FOOD ORDER SYSTEM")
    print("(Design Patterns Demo)")
    print_separator()


    print("\n=== STEP 1: Singleton Pattern ===")

    manager1 = RestaurantManager.get_instance()
    manager2 = RestaurantManager.get_instance()

    print(f"Instance 1 == Instance 2: {manager1 is manager2}")


    print("\n=== STEP 2: Factory Method Pattern ===")

    pizza_factory = PizzaFactory()
    burger_factory = BurgerFactory()
    salad_factory = SaladFactory()

    pizza = pizza_factory.create_food()
    burger = burger_factory.create_food()
    salad = salad_factory.create_food()

    foods = [pizza, burger, salad]

    for food in foods:

        print(f"\n{food.get_name()}: {food.get_price():,} IRR")

        print("Ingredients:",", ".join(food.get_ingredients()))


    print("\n=== STEP 3: Abstract Factory Pattern ===")

    economy_factory = EconomyMealFactory()

    economy_food = economy_factory.create_food()
    economy_drink = economy_factory.create_drink()

    economy_total = (economy_food.get_price() + economy_drink.price())

    print("\n[ECONOMY PACKAGE]")
    print(f"Food: {economy_food.get_name()} - {economy_food.get_price():} T")

    print(f"Drink: {economy_drink.name} - {economy_drink.price:,} T")


    print(f"Total: {economy_total:,} T")

    luxury_factory = LuxuryMealFactory()

    luxury_food = luxury_factory.create_food()
    luxury_drink = luxury_factory.create_drink()

    luxury_total = (luxury_food.get_price() + luxury_drink.price )

    print("\n[LUXURY PACKAGE]")

    print(f"Food: {luxury_food.get_name()} {luxury_food.get_price():} T")

    print(f"Drink: {luxury_drink.name} - {luxury_drink.price:,} T")

    print(f"Total: {luxury_total:,} T")



    print("\n=== STEP 4: Builder Pattern ===")

    builder = OrderBuilder()

    director = OrderDirector(builder)

    order = director.create_simple_order(pizza)

    print("\nOrder Created Successfully")

    print(f"Customer: {order.customer_name}")

    print(f"Address: {order.address}")

    print("\nItems:")

    for item in order.items:

        print(f"- {item.get_name()} {item.get_price():,} T.")

    print(f"\nPayment Method: {type(order.payment_method).__name__}")

    print(f"Notification Method: {type(order.notification_method).__name__}")

    print(f"Special Note: {order.special_note}")

    print(f"Final Price: {order.total_price:,} T")


    print("\n=== STEP 5: Processing ===")

    manager1.add_order(order)

    print("\nOrder submitted successfully!")

    print(order.payment_method.pay(order.total_price))

    print(order.notification_method.send("Your order has been accepted."))

    print(f"\nTotal Orders in Restaurant: {len(manager1.list_orders())}")



if name == "__main__":
    main()