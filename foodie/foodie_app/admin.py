from django.contrib import admin
from .models import Category



class CategoryAdmin(admin.ModelAdmin):
    # Which fields to show in the list view
    list_display = ('id', 'name', 'date_added')
    


admin.site.register(Category, CategoryAdmin)

