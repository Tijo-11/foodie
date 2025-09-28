from django import forms
from .models import Category
from recipes.models import Recipe

class CategoryForm(forms.ModelForm):   # ✅ use ModelForm
    class Meta:
        model = Category
        fields = ["name"]
        labels = {"name": "Category Name"}


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'ingredients', 'directions', 'category']

