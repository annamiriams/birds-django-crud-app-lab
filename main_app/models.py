from django.db import models
from django.urls import reverse

# Create your models here.

FOOD_OPTIONS = (
    ('Su', 'Suet'),
    ('Se', 'Seeds'),
    ('F', 'Fruit'),
    ('B', 'Berries'),
    ('I', 'Insects'),
    ('O', 'Other'),
    
)

class Bird(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('bird-detail', kwargs={'bird_id': self.id})

# Model for tracking when a bird is observed eating a certain kind of food.
class Meal(models.Model):
    date = models.DateField('Date of observed meal')
    meal = models.CharField(max_length=2, choices=FOOD_OPTIONS, default=FOOD_OPTIONS[0][0])
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)
        # Delete all meals in db if bird is deleted
    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}."