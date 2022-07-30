from django.shortcuts import render, HttpResponse

# Create your views here.
def Home(request):
    return HttpResponse("<h1>Hello Django</h1>")

def About(request):
    return HttpResponse("<h1>Welcome to About Page</h1>")

