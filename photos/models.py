from django.db import models

# Create your models here.
class Photos(models.Model):
    image_name = models.CharField(max_length=30)
    description = models.TextField()
    photo_category = models.ForeignKey('Category',on_delete=models.CASCADE,default='')
    photo_location = models.ForeignKey('Location', on_delete=models.SET_NULL,default = '', null = True)
    pub_date = models.DateTimeField(auto_now_add=False,auto_now= True)

    def save_photo(self):
        self.save()

    def __str__(self):
        return self.image_name

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def save_category_name(self):
        self.save()

    def __str__(self):
        return self.category_name

class Location(models.Model):
    location = models.CharField(max_length=30)

    def save_location(self):
        self.save()
        
    def __str__(self):
        return self.location
