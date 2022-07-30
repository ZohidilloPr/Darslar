from django.shortcuts import render
from .models import Images
from django.views.generic.edit import CreateView
# Create your views here.
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
def Home(request):
    return render(request, "index.html", {"list":list})

def Resume_page(request):
    return render(request, "resume.html")

class AddImg(CreateView):
    model = Images
    template_name = 'add.html'
    fields = ['name', 'img']
    success_url = '/'

