from django.urls import path
from .views import Home, AddImg, Resume_page

urlpatterns = [
    path("", Home, name="HM"),
    path("resume/", Resume_page, name="RP"),
    path("add/", AddImg.as_view(), name="AI"),
]
