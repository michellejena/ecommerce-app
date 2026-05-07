from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = models.CharField(max_length=100)
    image_url = models.URLField(default="https://via.placeholder.com/200x150?text=Delicious+Cake")

    def __str__(self):
        return self.name

# Create your models here.
