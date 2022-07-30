from django.shortcuts import render
from .models import Human
from django.views.generic import DetailView, CreateView
# Create your views here.

list = [1, 2, 3, 4, 5, 6, 7, 8]
def Home(request):
    humans = Human.objects.all()
    context = {
        "human":humans
    }
    return render(request, "home.html", context)

def About(request):
    return render(request, "about.html")

# def Human_Info(request, pk):
#     human = Human.objects.filter(pk=pk)
#     context = {
#         "object":human
#     }
#     return render(request, "human_info.html", context)

class OnePersonView(DetailView):
    model = Human
    template_name = "human_info.html"
    
    
    
    
    
    
   
class AddHuman(CreateView):
    model = Human
    template_name = "add_human.html"
    success_url = '/'
    fields = ('full_name', 'profile_img', 'age', 'address', 'info')