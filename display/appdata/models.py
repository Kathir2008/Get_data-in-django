from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class demo(models.Model):
    Mail = models.CharField(max_length=100)
    password = models.CharField(max_length=100)