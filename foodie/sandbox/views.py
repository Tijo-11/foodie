from django.views.generic import ListView, DetailView
from recipes.models import Recipe
from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback
# from django.http import HttpResponse

class RecipeListView(ListView):
    model = Recipe                       # which model to fetch data from
    template_name = "sandbox/index.html" # which template to render
    context_object_name = "recipes"      # variable name in the template
    
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "sandbox/recipe_detail.html"
    context_object_name = "recipe"

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Save data to the database
            Feedback.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                feedback=form.cleaned_data['feedback'],
                satisfaction=form.cleaned_data['satisfaction']
            )
            return redirect('sandbox:thank_you')  # Redirect after submission
    else:
        form = FeedbackForm()  # GET request → empty (unbound) form

    context = {'form': form}
    return render(request, 'sandbox/feedback_form.html', context)

def thank_you(request):
    return render(request, 'sandbox/thank_you.html')