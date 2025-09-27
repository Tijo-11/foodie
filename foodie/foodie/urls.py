

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('sandbox/', include('sandbox.urls')), # connect app
    path('', include('foodie_app.urls')),
     path('recipes/', include('recipes.urls')),   # include recipes app
     path("comments/", include("comments.urls")),
]
