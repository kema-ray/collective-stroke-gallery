from django.test import TestCase
from .models import Photos,Category,Location

# Create your tests here.
class PhotosTestClass(TestCase):
    def setUp(self):
        self.new_location = Location(location = 'Nairobi')
        self.new_location.save()

        self.new_category = Category(category_name = 'Photography')
        self.new_category.save()

        self.new_food = Photos(name = 'Pizza', description = 'stress reliever',photo_location=self.new_location,photo_category=self.new_category, image='image.jpeg')
        self.new_food.save()

    def tearDown(self):
        Photos.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_food, Photos))

    def test_save_food(self):
        self.new_food.save_photo()
        image = Photos.objects.all()

    def test_delete_food(self):
        self.new_food.save_photo()
        self.new_food.delete_photo()

class CategoryTestClass(TestCase):
    def setUp(self):
        self.Hike = Category(category_name = 'Hike')
        self.Hike.save_category_name()

    def tearDown(self):
        Category.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.Hike, Category))

    def test_save_category(self):
        self.test_category = Category(category_name = 'Travel')
        self.test_category.save_category_name()
        self.test_category.delete_category_name()

class LocationTestClass(TestCase):

    def setUp(self):
        self.Mombasa = Location(location='Mombasa')
        self.Mombasa.save_location()

    def tearDown(self):
        Location.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.Mombasa,Location))

    def test_save_method(self):
        self.Mombasa.save_location()
        Locations = Location.objects.all()
        print(Locations)
        self.assertTrue(len(Locations)==1)

    def test_delete_method(self):
        self.Mombasa.delete_location()
        Destination = Location.objects.all()
        print(Destination)
        self.assertTrue(len(Destination)==0)

    def test_update_location(self):
        updated_location = Location.objects.filter(location='Nairobi')
        self.assertFalse(len(updated_location)> 0)
