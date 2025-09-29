from django.shortcuts import render, redirect

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import UserProfileForm

def register(request):
    if request.method != "POST":
        # Display empty form for GET requests
        form = UserCreationForm()
    else:
        # Fill form with submitted POST data
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            # Save the new user to the database
            new_user = form.save()
            # Log in the new user immediately
            login(request, new_user)
            return redirect("foodie_app:index")
        # If not POST or form invalid, show registration form
    context = {"form": form}
    return render(request, "registration/register.html", context)


def edit_user_profile(request):
    if request.method == "POST":
        form = UserProfileForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if form.is_valid():
            form.save()
            return redirect("foodie_app:index")
    else:
        form = UserProfileForm(instance=request.user.profile)

    return render(
        request,
        "accounts/edit_profile.html",
        {"form": form}
    )
