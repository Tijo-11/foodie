from django.shortcuts import render
from .models import Category  # Category model in foodie_app
from recipes.models import Recipe  # import Recipe from the recipes app




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

