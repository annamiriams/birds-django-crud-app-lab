from django.db import models
from django.urls import reverse

# Create your models here.

class Bird(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('bird-detail', kwargs={'bird_id': self.id})