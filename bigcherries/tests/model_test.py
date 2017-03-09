from django.test import TestCase

from bigcherries.models import (
    Conversion,
    Ingredient,
    IngredientRecipe,
    MeasurementUnit,
    Recipe,
)


class ModelTestCase(TestCase):
    def setUp(self):
        MeasurementUnit.objects.create(name="kilogram", symbol="kg")
        MeasurementUnit.objects.create(name="gram", symbol="g")
        MeasurementUnit.objects.create(name="liter", symbol="L")
        MeasurementUnit.objects.create(name="milliliter", symbol="mL")
        MeasurementUnit.objects.create(name="slice", symbol="slice")

    def test_model(self):
        g_unit = MeasurementUnit.objects.get(symbol="g")
        kg_unit = MeasurementUnit.objects.get(symbol="kg")

        moutarde = Ingredient.objects.create(name="Moutarde", preferred_unit=g_unit)
        IngredientConversion.objects.create(
            ingredient=moutarde,
            src_unit=g_unit,
            dst_unit=kg_unit,
            multiplicand=0.001,
        )

        r = Recipe.objects.create(name="Tarte a la moutarde", content="Stuff")
        IngredientRecipe.objects.create(
            recipe=r,
            ingredient=moutarde,
            unit=kg_unit,
            qty=10.5,
        )

        ingredients = r.get_ingredients()
        assert len(ingredients) == 1
        assert ingredients[0].ingredient.name == "Moutarde"
        assert ingredients[0].unit.name == "gram"
        assert ingredients[0].qty == 10.5
