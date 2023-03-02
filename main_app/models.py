from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    wingspan = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    description = models.TextField(max_length=500)