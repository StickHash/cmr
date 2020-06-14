from django.shortcuts import render

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
