# Generated by Django 4.0.4 on 2022-05-29 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0009_photos_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photos',
            old_name='image_name',
            new_name='name',
        ),
    ]
