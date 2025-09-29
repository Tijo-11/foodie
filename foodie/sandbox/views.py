from django.views.generic import ListView, DetailView
from recipes.models import Recipe
from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback
# from django.http import HttpResponse
# from django.contrib import messages

class RecipeListView(ListView):
    model = Recipe                       # which model to fetch data from
    template_name = "sandbox/index.html" # which template to render
    context_object_name = "recipes"      # variable name in the template
    
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "sandbox/recipe_detail.html"
    context_object_name = "recipe"

def thank_you(request):
    return render(request, 'sandbox/thank_you.html')

# def feedback(request):
#     # get the current visit count, default to 0 if not set
#     feedback_visits = request.session.get('feedback_visits', 0)
#     # increment for the current visit
#     request.session['feedback_visits'] = feedback_visits + 1

#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             # Save data to the database manually
#             Feedback.objects.create(
#                 name=form.cleaned_data['name'],
#                 email=form.cleaned_data['email'],
#                 feedback=form.cleaned_data['feedback'],
#                 satisfaction=form.cleaned_data['satisfaction']
#             )
#             # Add success message
#             messages.success(request, 'Thank you! Your feedback has been submitted.')
#             return redirect('sandbox:thank_you')  # or 'sandbox:index' if preferred
#     else:
#         form = FeedbackForm()

#     context = {'form': form, 'visits': request.session['feedback_visits'],}
#     return render(request, 'sandbox/feedback_form.html', context)


def feedback(request):
    form = FeedbackForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        # Save form data into session instead of database
        request.session['feedback_data'] = form.cleaned_data

        # Redirect user to the review page
        return redirect('sandbox:feedback_review')

    # Render feedback form as usual
    return render(request, 'sandbox/feedback.html', {'form': form})


def feedback_review(request):
    # Retrieve data from session
    feedback_data = request.session.get('feedback_data', {})

    if request.method == "POST":
        # Save to database
        Feedback.objects.create(**feedback_data)

        # Delete session data after saving
        del request.session['feedback_data']

        # Redirect to homepage or confirmation
        return redirect('sandbox:recipe-list')

    # If GET request → show form prefilled with session data
    form = FeedbackForm(initial=feedback_data)

    return render(request, 'sandbox/feedback_review.html', {'form': form})