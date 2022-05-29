from django.db import models

# Create your models here.
class Photos(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to = 'pictures/', default='No image')
    photo_category = models.ForeignKey('Category',on_delete=models.CASCADE,default='')
    photo_location = models.ForeignKey('Location', on_delete=models.SET_NULL,default = '', null = True)
    pub_date = models.DateTimeField(auto_now_add=False,auto_now= True)

    def save_photo(self):
        self.save()

    @classmethod
    def search_by_photo_category(cls,search_term):
        image = cls.objects.filter(name__icontains = search_term)
        return image

    def update_image(self,Name=None,category=None):
        self.name = Name if Name else self.Name
        self.photo_category = category if category else self.photo_category
        self.save()

    def __str__(self):
        return self.name

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
