from django.shortcuts import render, redirect
from .models import Category  # Category model in foodie_app
from recipes.models import Recipe  # import Recipe from the recipes app
from .forms import CategoryForm, RecipeForm

def index(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'foodie_app/index.html', context)

def recipes(request, category_id):
    # get all recipes with the passed category id
    recipes_qs = Recipe.objects.filter(category=category_id)
    # get the category object so we can show its name in the template
    category = Category.objects.get(pk=category_id)
    context = {
        'recipes': recipes_qs,
        'category': category,
    }
    return render(request, 'foodie_app/recipes.html', context)


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)  # bind form with submitted data
        # later: we’ll save it if valid
        if form.is_valid():
            form.save()
            return redirect("foodie_app:index")  # redirect to homepage
        else:
            # Invalid form → re-render the page with error messages
            return render(request, "foodie_app/add_category.html", {"form": form})
        
    else:
        form = CategoryForm()  # empty form for GET requests

    context = {"form": form}
    return render(request, "foodie_app/add_category.html", context)


def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipes:recipes')  # back to homepage
    else:
        form = RecipeForm()  # empty form for GET request

    return render(request, 'foodie_app/add_recipe.html', {'form': form})

