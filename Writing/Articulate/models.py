from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .utils import *

# Create your models here.
class StoryModel(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    content = FroalaField()
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='story')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(StoryModel, self).save(*args, **kwargs)


class Profile(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    about_me = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='profile', null=True, blank=True)

    def __str__(self):
        return self.user.username


# class Genre(models.Model):

#     genre = models.CharField(max_length=100)
#     story = models.ForeignKey(StoryModel, on_delete=models.CASCADE)

class GenreModel(models.Model):
    genre = models.CharField(max_length=100)
    story = models.ManyToManyField(StoryModel)

    def __str__(self):
        return self.genre