from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe  # import the Recipe model
from comments.forms import CommentForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseNotAllowed
from foodie_app.forms import RecipeForm

def recipes_view(request):
    recipes = Recipe.objects.all()  # fetch all recipes
    context = {
        'recipes': recipes  # pass the queryset to the template
    }
    return render(request, 'recipes/recipes.html', context)

def recipe(request, recipe_id):
    # Fetch the specific recipe by ID
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    comments = recipe.comments.all()
    comments = recipe.comments.all()
    
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.recipe = recipe
            new_comment.user = request.user
            new_comment.save()
            return redirect(recipe.get_absolute_url())
    else:
        comment_form = CommentForm()

    context = {
        "recipe": recipe,
        "comments": comments,
        "comment_form": comment_form,
    }
    return render(request, "recipes/recipe.html", context)


def search_results(request):
    query = request.GET.get('query', '')  # Get the search query
    results = []

    if query:
        # Filter recipes by multiple fields using Q objects with OR conditions
        results = Recipe.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(ingredients__icontains=query) |
            Q(directions__icontains=query) |
            Q(category__name__icontains=query)
        )

        # Remove duplicates if needed
        seen_ids = set()
        unique_results = []
        for result in results:
            if result.id not in seen_ids:
                unique_results.append(result)
                seen_ids.add(result.id)

        results = unique_results

    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'recipes/search_results.html', context)


@login_required
def toggle_favorite(request, recipe_id):
    # Get the recipe or return 404 if not found
    recipe = get_object_or_404(Recipe, id=recipe_id)

    # Check if current user already favorited this recipe
    if request.user in recipe.favorited_by.all():
        # If yes → remove (unfavorite)
        recipe.favorited_by.remove(request.user)
    else:
        # If not → add to favorites
        recipe.favorited_by.add(request.user)

    # Redirect back to the recipe detail page
    return redirect("recipes:recipe_detail", recipe_id=recipe.id)


@login_required
def favorite_recipes(request):
    user = request.user
    # Access the related name from Recipe model
    favorites = user.favorite_recipes.all()

    context = {
        "recipes": favorites
    }

    return render(request, "recipes/favorites.html", context)


@login_required
def delete_recipe(request, recipe_id):
    # Get the recipe to delete
    recipe = get_object_or_404(Recipe, id=recipe_id)
    
    # Check if the user is allowed to delete
    if not (request.user == recipe.user or request.user.is_superuser):
        return HttpResponseForbidden()  # 403 if not owner/admin

    if request.method == 'POST':
        recipe.delete()
        return redirect('recipes:recipes')  # Redirect to recipe index

    # GET request: show confirmation page
    context = {'recipe': recipe}
    return render(request, 'recipes/recipe_confirmation_delete.html', context)

@login_required
def edit_recipe(request, recipe_id):
    # Get the recipe object
    recipe = get_object_or_404(Recipe, id=recipe_id)

    # Check if user is authorized
    if not (request.user == recipe.user or request.user.is_superuser):
        return HttpResponseNotAllowed()  # Could also use HttpResponseForbidden()

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipes:recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)  # Prepopulate form with existing data

    context = {'form': form, 'recipe': recipe}
    return render(request, 'recipes/recipe_form.html', context)

    