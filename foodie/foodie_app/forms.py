from django import forms
from .models import Category
from recipes.models import Recipe

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'Category Name'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Category Name'
            })
        }


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'ingredients', 'directions', 'category']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',   # for CSS styling (e.g., Bootstrap)
                'placeholder': 'Recipe Title'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Description',
                'rows': 5
            }),
            'ingredients': forms.Textarea(attrs={
                'placeholder': 'Ingredients',
                'rows': 5
            }),
            'directions': forms.Textarea(attrs={
                'placeholder': 'Directions',
                'rows': 5
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            })
        }

