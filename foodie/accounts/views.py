from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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
            return HttpResponse("Registration successful! You are now logged in.")
        # If not POST or form invalid, show registration form
    context = {"form": form}
    return render(request, "registration/register.html", context)

