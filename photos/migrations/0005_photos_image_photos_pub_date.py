# Generated by Django 4.0.4 on 2022-05-27 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_photos_photo_category_photos_photo_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='photos',
            name='pub_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
