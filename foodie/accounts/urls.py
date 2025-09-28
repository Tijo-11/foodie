from django.urls import path, include
from . import views 

app_name = 'accounts'

urlpatterns = [
    # Use Django’s built-in authentication system (login/logout/password management)
    path("accounts/", include("django.contrib.auth.urls")),
    # Custom register page
    path("register/", views.register, name="register"),
]