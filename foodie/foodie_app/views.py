from django.shortcuts import render, redirect, get_object_or_404
from .models import Category  # Category model in foodie_app
from recipes.models import Recipe  # import Recipe from the recipes app
from .forms import CategoryForm, RecipeForm
from django.contrib.auth.decorators import login_required

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

@login_required
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

@login_required
def add_recipe(request, category_id=None):
    # Try to fetch category if category_id is provided
    category = get_object_or_404(Category, id=category_id) if category_id else None

    # Prepare initial data
    initial_data = {'category': category}

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, initial=initial_data)
        if form.is_valid():
            new_recipe = form.save(commit=False)
            new_recipe.user = request.user
            if category:
                new_recipe.category = category  # Explicitly set category if passed
            new_recipe.save()
            return redirect('foodie_app:recipes', category_id=new_recipe.category.id if new_recipe.category else '')
    else:
        form = RecipeForm(initial=initial_data)

    return render(request, 'foodie_app/add_recipe.html', {
        'form': form,
        'category': category,
    })

