from django.db import models

# Create your models here.
class MeasurementUnit(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=20)


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    preferred_unit = models.ForeignKey(MeasurementUnit)


class IngredientConversion(models.Model):
    ingredient = models.ForeignKey(Ingredient)
    src_unit = models.ForeignKey(MeasurementUnit, related_name='+')
    dst_unit = models.ForeignKey(MeasurementUnit, related_name='+')
    multiplicand = models.FloatField()


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()

    def get_ingredients(self):
        return IngredientRecipe.objects.filter(recipe=self)


class IngredientRecipe(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingredient = models.ForeignKey(Ingredient)
    unit = models.ForeignKey(MeasurementUnit)
    qty = models.FloatField()
