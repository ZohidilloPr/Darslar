from django.db import models

# Create your models here.
class Human(models.Model):
    """Inson objectlarini"""
    full_name = models.CharField(max_length=100)
    profile_img = models.ImageField(upload_to="media/user-img/")
    age = models.IntegerField()
    address = models.CharField(max_length=150)
    # email = models.EmailField(max_length=250)
    info = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name
    