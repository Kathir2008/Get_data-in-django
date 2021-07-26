from django.db import models

# Create your models here.

class GK(models.Model):
    User_name = models.CharField(max_length=100)
    Age = models.IntegerField()
