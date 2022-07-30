from django.urls import path
from .views import (
    Home, 
    About, 
    OnePersonView, 
    AddHuman,
)

urlpatterns = [
    path("", Home, name="Home"),
    path("about/", About, name="About"),
    path("one_person/<pk>/", OnePersonView.as_view(), name="OPV"), 
    path("add/", AddHuman.as_view(), name="AH")
]

