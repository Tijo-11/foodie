from rest_framework import viewsets
from .models import Recipe
from .serializers import RecipeSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()  # Get all recipe objects
    serializer_class = RecipeSerializer  # Use the serializer we created earlier
def perform_create(self, serializer):
    serializer.save(user=self.request.user)