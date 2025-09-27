from django.shortcuts import render

def index(request):
    data = {
        "name": "Paolo",
        "age": 123
    }
    context = {"data": data}
    return render(request, "index.html", context)
