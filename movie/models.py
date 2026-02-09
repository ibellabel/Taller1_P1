from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    AGE_CHOICES = [
        ('kids', 'Niños'),
        ('teens', 'Jóvenes'),
        ('adults', 'Adultos'),  
    ]
    age_group = models.CharField(max_length=10, choices = AGE_CHOICES, default='teens')
    image = models.ImageField(upload_to= 'movie/images/')
    url = models.URLField(blank=True)