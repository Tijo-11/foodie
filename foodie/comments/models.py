from django.db import models
from recipes.models import Recipe  # Import Recipe from recipes app
from django.contrib.auth.models import User

class Comment(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE, related_name='comments'  # 👈 This enables recipe.comments
    )
    text = models.TextField()
    added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', default='1')

    def __str__(self):
        return f"Comment by {self.user.username} on {self.recipe.name}"
