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

    # Req 4


def get_main_menu(self, restriction=None) -> pd.DataFrame:
    menu_data = self.menu_data.dishes

    if not menu_data:
        empty_df = pd.DataFrame(
            columns=["dish_name", "price", "ingredients", "restrictions"]
        )
        return empty_df

    menu_dict = []
    for dish in menu_data:
        if restriction is None or restriction not in dish.get_restrictions():
            dish_info = {
                "dish_name": dish.name,
                "price": dish.price,
                "ingredients": dish.get_ingredients(),
                "restrictions": dish.get_restrictions(),
            }
            menu_dict.append(dish_info)

    columns = ["dish_name", "price", "ingredients", "restrictions"]
    menu_df = pd.DataFrame(menu_dict, columns=columns)
    return menu_df
