from django.db import models

# Create your models here.
class Images(models.Model):
    name = models.CharField(verbose_name="F.I.O", max_length=50)
    img = models.ImageField(upload_to='media/user_img/')
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name