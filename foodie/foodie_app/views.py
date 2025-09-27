from django.shortcuts import render

def index(request):
    return render(request, 'foodie_app/index.html')