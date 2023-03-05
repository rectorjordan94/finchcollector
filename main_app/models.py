from django.db import models
from django.urls import reverse
# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.color} {self.name}"
    
    def get_absolute_url(self):
        return reverse('foods_detail', kwargs={'pk': self.id})

class Finch(models.Model):
    name = models.CharField(max_length=100)
    wingspan = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    foods = models.ManyToManyField(Food)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})

class Sighting(models.Model):
    date = models.DateField('sighting date')
    location = models.CharField(max_length=100)

    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"At {self.location} on {self.date}"
    
    class Meta:
        ordering = ['-date']

