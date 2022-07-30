from .forms import NewUserForm
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
# Create your views here.

def CreateUser(request):
    form = NewUserForm
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Muaffaqiyatli bajarildi :) ")
            return redirect("accounts:LI")
    context = {
        "form":form,
    }
    return render(request, "register/signup.html", context)

def Login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Xush kelibsiz {user.username}!")
                return redirect("blog:BV")
            messages.error(request, "Username yoki parol xato Afsus :( ")
        messages.error(request, "Username yoki parol xato Afsus :( ")
        
    form = AuthenticationForm
    return render(request, "register/login.html", {"form": form})
        
def LogOut(request):
    logout(request)
    messages.info(request, "Ko'rishguncha")
    return redirect("blog:BV")