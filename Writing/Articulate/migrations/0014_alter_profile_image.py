# Generated by Django 3.2.8 on 2021-11-10 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articulate', '0013_auto_20211109_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='profile/default_image.png', null=True, upload_to='profile'),
        ),
    ]
