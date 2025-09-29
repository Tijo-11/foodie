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
]
