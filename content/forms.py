from django import forms

from content.models import Recipe, IngredientLine


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'photo')


class IngredientLineForm(forms.ModelForm):
    class Meta:
        model = IngredientLine
        fields = ('ingredient', 'quantity', 'unity')

