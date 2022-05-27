from unicodedata import category
from django.db import models

# Create your models here.
class Photos(models.Model):
    image_name = models.CharField(max_length=30)
    description = models.TextField()
    photo_category = models.ForeignKey('Category',on_delete=models.CASCADE,default='')
    photo_location = models.ForeignKey('Location', on_delete=models.SET_NULL,default = '', null = True)

    def __str__(self):
        return self.image_name

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name

class Location(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location
