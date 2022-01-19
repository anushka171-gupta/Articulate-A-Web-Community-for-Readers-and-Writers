from django.contrib import admin
from .models import StoryModel, Profile, GenreModel

# Register your models here.
admin.site.register(StoryModel)
admin.site.register(Profile)
admin.site.register(GenreModel)
# admin.site.register(Genre)