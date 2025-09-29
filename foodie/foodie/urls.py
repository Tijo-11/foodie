

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('home/', include('foodie_app.urls')),
    path('sandbox/', include(('sandbox.urls', 'sandbox'), namespace='sandbox')),
    path('recipes/', include('recipes.urls')),   # include recipes app
    path("comments/", include("comments.urls")),
    path("", include(('accounts.urls', 'accounts'), namespace='accounts')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#"accounts" (inside the tuple)
# This is the app name used for namespacing. It should match the app_name variable defined in 
# accounts/urls.py like this: app_name = "accounts"
#namespace="accounts"This defines a URL namespace, allowing you to refer to views in this app 
# using namespaced reverse lookups like: reverse("accounts:login")
