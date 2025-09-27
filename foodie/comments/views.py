from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def comments(request):
    return HttpResponse("Hello from comments")
