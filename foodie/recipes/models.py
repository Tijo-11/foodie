from django.db import models
from foodie_app.models import Category  # Import Category from foodie_app
from django.contrib.auth.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    ingredients = models.TextField()
    directions = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes', null=True, default=1)

    
    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return self.name
