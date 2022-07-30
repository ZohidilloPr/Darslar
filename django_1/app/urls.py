from django.urls import path
from .views import Home, About

urlpatterns = [
    path("", Home, name="Home"),
    path("about/", About, name="About")
]