from django.shortcuts import render

from content.models import Recipe


def recipe_list(request):
    recipes = Recipe.objects.order_by('title')

    context = {
        'recipes': recipes,
    }

    return render(request, 'content/recipes.html', context)
