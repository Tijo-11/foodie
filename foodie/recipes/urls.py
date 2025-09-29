from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.recipes_view, name='recipes'),
    path('<int:recipe_id>/', views.recipe, name='recipe_detail'),  # Detail page for a single recipe
    path('search/', views.search_results, name='search_results'),
    path(
        "recipes/<int:recipe_id>/toggle_favorite/",
        views.toggle_favorite,
        name="toggle_favorite"
    ),
    path("my-favorites/", views.favorite_recipes, name="favorite_recipes"),
    path('recipe/<int:recipe_id>/delete/', views.delete_recipe, name='delete_recipe'),
    path('recipe/<int:recipe_id>/edit/', views.edit_recipe, name='edit_recipe'),
]
