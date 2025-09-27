from django.shortcuts import render

def index(request):
    foods = ["pizza", "pasta", "bread", "salad"]
    context = {"foods": foods}
    return render(request, "index.html", context)

