from django.contrib import admin
from .models import UserProfile

# class RecipeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'date_added', 'image')

# Register your models here.
admin.site.register(UserProfile)
