from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe  # import the Recipe model
from comments.forms import CommentForm
from django.db.models import Q

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



    