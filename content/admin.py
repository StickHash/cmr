from django.contrib import admin

from content.models import Recipe, IngredientLine, Ingredient, Step

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(IngredientLine)
admin.site.register(Step)