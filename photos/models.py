from django.db import models

# Create your models here.
class Photos(models.Model):
    image_name = models.CharField(max_length=30)
    description = models.TextField(max_length=100, blank=False)
