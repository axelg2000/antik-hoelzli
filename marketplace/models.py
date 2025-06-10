from django.db import models

class Furniture(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=200, default='Haus & Garten > Dekoration')
    price = models.DecimalField(max_digits=10, decimal_places=0)
    
    # Images handled via related FurnitureImage model

    # Contact details
    contact_name = models.CharField(max_length=100, default='Axel')
    contact_phone = models.CharField(max_length=20, default='15563056052')
    contact_zipcode = models.CharField(max_length=20, default='80331')  # Munich postal code

    # Optional Kleinanzeigen metadata
    content_hash = models.CharField(max_length=100, blank=True, null=True)

    # Track posting status
    is_posted = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class FurnitureImage(models.Model):
    furniture = models.ForeignKey(Furniture, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='furniture_images/')

    def __str__(self):
        return f"Image for {self.furniture.title}"