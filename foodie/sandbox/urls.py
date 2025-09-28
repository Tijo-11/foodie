from django.urls import path
from .views import RecipeDetailView, feedback, RecipeListView, thank_you

urlpatterns = [
    path("", RecipeListView.as_view(), name="recipe-list"),
    path("<int:pk>/", RecipeDetailView.as_view(), name="recipe-detail"),
    path('feedback/', feedback, name='feedback'),
     path("thank-you/", thank_you, name="thank_you"),
]
