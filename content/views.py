from django.http import HttpResponseRedirect
from django.shortcuts import render

from content.forms import RecipeForm, IngredientLineForm
from content.models import Recipe


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
    ingForm = IngredientLineForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            ingline = ingForm.save(commit=False)
            ingline.recipe_id = recipe.id
            ingline.ingredient_id = request.POST["ingredient"]
            ingline.quantity = request.POST["quantity"]
            ingline.save()
            return HttpResponseRedirect('/recettes/')
    else:
        form = RecipeForm()
    return render(request, 'content/new_recipe.html', {'form': form, 'ingForm': ingForm})
