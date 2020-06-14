from django.contrib.auth.models import User
from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=50)


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ingredients = models.ManyToManyField(Ingredient, through='IngredientLine')
    photo = models.ImageField(upload_to='recipes/', null=True)

    def __str__(self):
        return self.title

    def get_ingredientList(self):
        return IngredientLine.objects.filter(recipe=self)

    def get_stepList(self):
        return Step.objects.filter(recipe=self)


class Step(models.Model):
    sequence = models.IntegerField()
    description = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='recipes/steps/', null=True)


class IngredientLine(models.Model):
    GRAMMES = 'gr'
    KILOGRAMMES = 'kg'
    LITRES = 'l'
    CENTILITRES = 'cl'
    MILLILITRES = 'ml'
    UNITE = ' '
    UNIT = [
        (GRAMMES, 'grammes'),
        (KILOGRAMMES, 'kilogrammes'),
        (LITRES, 'litres'),
        (CENTILITRES, 'centilitres'),
        (MILLILITRES, 'millilitres'),
        (UNITE, 'unité')
    ]
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unity = models.CharField(
        max_length=15,
        choices=UNIT,
        default=GRAMMES
    )
