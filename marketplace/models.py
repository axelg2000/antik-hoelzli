from django.db import models

# Create your models here.
from django.db import models

class Furniture(models.Model):
    title = models.CharField(max_length=200)
    age = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dimensions = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='furniture_images/')

    

    def __str__(self):
        return self.title