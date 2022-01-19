# Generated by Django 3.2.8 on 2021-11-05 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articulate', '0005_storymodel_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenreModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=100)),
                ('story', models.ManyToManyField(to='Articulate.StoryModel')),
            ],
        ),
    ]