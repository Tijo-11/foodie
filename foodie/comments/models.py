from django.db import models
from recipes.models import Recipe  # Import Recipe from recipes app

class Comment(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE
    )
    text = models.TextField()
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
