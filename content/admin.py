from django.contrib import admin

from content.models import Recipe, IngredientLine, Ingredient

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(IngredientLine)