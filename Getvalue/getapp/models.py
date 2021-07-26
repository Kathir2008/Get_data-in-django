from django.db import models

# Create your models here.
class data(models.Model):
    Name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=100)