from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)  # New field
    
    class Meta:
        verbose_name = "Category"
        ordering = ['name']   # default order by name ascending

    def __str__(self):
        return self.name
    
    

