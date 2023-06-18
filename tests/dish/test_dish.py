from src.models.dish import Dish
from src.models.ingredient import Ingredient
import pytest


def test_dish():
    sushi = Dish("Sushi de salmão", 25.00)
    sushi2 = Dish("Sushi de salmão", 25.00)
    ramen = Dish("Ramen", 20.00)
    ingredient_arroz = Ingredient("Arroz")
    ingredient_salmao = Ingredient("Salmão")

    sushi.add_ingredient_dependency(ingredient_arroz, 1)
    sushi.add_ingredient_dependency(ingredient_salmao, 1)

    assert sushi.name == "Sushi de salmão"
    assert sushi.price == 25.00
    assert repr(sushi) == "Dish('Sushi de salmão', R$25.00)"
    assert sushi == sushi2
    assert sushi != ramen
    assert type(hash(sushi)) == int
    assert hash(sushi) == hash(sushi2)
    assert hash(sushi) != hash(ramen)
    assert sushi.get_ingredients() == {ingredient_arroz, ingredient_salmao}
    assert ramen.get_restrictions() == set()

    with pytest.raises(TypeError):
        Dish("Ramen", "20.00")

    with pytest.raises(ValueError):
        Dish("Ramen", -1)
