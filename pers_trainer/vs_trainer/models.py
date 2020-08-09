from django.db import models

# Create your models here.
class services(models.Model):
    serv_name = models.CharField(max_length=200)
    serv_desc = models.TextField()

class portfolio(models.Model):
    pt_photo = models.ImageField(upload_to='photos')