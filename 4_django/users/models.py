from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    user_img = models.ImageField(upload_to="media/user-img/", default="media/avatar.png")
