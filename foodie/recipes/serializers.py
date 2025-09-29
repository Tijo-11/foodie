from rest_framework import serializers
from .models import Recipe
class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe  # The model we want to serialize
        fields = [
            'id', 'name', 'description', 'ingredients', 
            'directions', 'date_added', 'category', 
            'user', 'image', 'favoured_by'
        ]  # Fields to include in the serialized output
        read_only_fields = ['image']  # Fields that should not be modified via API
