from src.models.ingredient import Ingredient


# Req 1
def test_ingredient():
    fish = Ingredient("salmão")
    picles = Ingredient("pepino")
    rice = Ingredient("arroz")
    fish2 = Ingredient("salmão")

    assert hash(fish) == hash('salmão')
    assert fish == fish2
    assert picles.name == 'pepino'
    assert picles.restrictions == set()
    assert repr(rice) == "Ingredient('arroz')"
