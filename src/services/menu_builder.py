import pandas as pd
from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str):
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    def get_main_menu(self, restriction=None) -> pd.DataFrame:
        data_main = self.menu_data.dishes

        if not data_main:
            return pd.DataFrame(
                columns=["dish_name", "price", "ingredients", "restrictions"]
            )

        carte_dict = [
            {
                "dish_name": plate.name,
                "price": plate.price,
                "ingredients": plate.get_ingredients(),
                "restrictions": plate.get_restrictions(),
            }
            for plate in data_main
            if restriction is None
            or restriction not in plate.get_restrictions()
        ]

        pillar = ["dish_name", "price", "ingredients", "restrictions"]
        return pd.DataFrame(carte_dict, columns=pillar)
