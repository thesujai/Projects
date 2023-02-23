from django.db import models

# Create your models here.
class feedback(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    text=models.TextField(max_length=256)