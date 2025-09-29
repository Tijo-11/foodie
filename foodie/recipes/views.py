from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe  # import the Recipe model
from comments.forms import CommentForm

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


    