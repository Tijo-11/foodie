from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.recipes_view, name='recipes'),
    path('<int:recipe_id>/', views.recipe, name='recipe_detail'),  # Detail page for a single recipe
]
