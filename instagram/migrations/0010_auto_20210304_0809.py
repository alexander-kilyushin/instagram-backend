# Generated by Django 3.1.7 on 2021-03-04 05:09

from django.db import migrations, models
import instagram.models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0009_auto_20210228_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='media/static/default_avatar.jpg', upload_to=instagram.models.avatar_upload_path),
        ),
    ]
