from django.forms import modelformset_factory, inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render

from content.forms import RecipeForm, IngredientLineForm
from content.models import Recipe, IngredientLine


def recipe_list(request):
    recipes = Recipe.objects.order_by('title')

    context = {
        'recipes': recipes,
    }

    return render(request, 'content/recipes.html', context)


def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    context = {
        'recipe': recipe,
    }
    return render(request, 'content/detail.html', context)


def new_recipe(request):
    form = RecipeForm()
    ingFormSet = modelformset_factory(IngredientLine, fields=('ingredient', 'quantity', 'unity'))
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        ingForm = ingFormSet(request.POST, request.FILES)
        if form.is_valid() & ingForm.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            ingredientList = ingForm.save(commit=False)
            for ingredient in ingredientList:
                ingredient.recipe = recipe
                ingredient.save()
            return HttpResponseRedirect('/recettes/')
    else:
        form = RecipeForm()
        ingForm = ingFormSet(queryset=IngredientLine.objects.none())
    return render(request, 'content/new_recipe.html', {'form': form, 'ingForm': ingForm})
