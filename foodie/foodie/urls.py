

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('home', include('foodie_app.urls')),
    path('sandbox/', include('sandbox.urls')),
    path('recipes/', include('recipes.urls')),   # include recipes app
    path("comments/", include("comments.urls")),
]
