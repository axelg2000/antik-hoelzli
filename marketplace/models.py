from django.db import models

class Furniture(models.Model):
    title = models.CharField(max_length=200)
    age = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    dimensions = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='furniture_images/', null=True, blank=True)

    def __str__(self):
        return self.title

class FurnitureImage(models.Model):
    furniture = models.ForeignKey(Furniture, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='furniture_images/')

    def __str__(self):
        return f"Image for {self.furniture.title}"