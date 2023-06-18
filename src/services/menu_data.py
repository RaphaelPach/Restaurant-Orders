import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.load_dishes(source_path)

    def load_dishes(self, source_path: str) -> None:
        with open(source_path, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for x in reader:
                dish_name, dish_price, ingredient_name, ingredient_quantity = x
                dish = self.get_or_create_dish(
                    dish_name,
                    float(dish_price),
                )
                ingredient = Ingredient(ingredient_name)
                dish.add_ingredient_dependency(
                    ingredient,
                    int(ingredient_quantity),
                )

    def get_or_create_dish(self, name: str, price: float) -> Dish:
        for existing_dish in self.dishes:
            if existing_dish.name == name:
                return existing_dish

        new_dish = Dish(name, price)
        self.dishes.add(new_dish)
        return new_dish
