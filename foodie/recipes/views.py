from django.shortcuts import render, get_object_or_404
from .models import Recipe  # import the Recipe model

def recipes_view(request):
    recipes = Recipe.objects.all()  # fetch all recipes
    context = {
        'recipes': recipes  # pass the queryset to the template
    }
    return render(request, 'recipes/recipes.html', context)

def recipe(request, recipe_id):
    # Fetch the specific recipe by ID
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    # Pass the recipe to the template
    context = {
        'recipe': recipe
    }
    return render(request, 'recipes/recipe.html', context)
