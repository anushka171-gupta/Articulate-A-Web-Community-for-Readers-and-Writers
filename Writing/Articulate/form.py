from django import forms
from froala_editor.widgets import FroalaEditor
from .models import *



options = (
    ("Fantasy","Fantasy"),
    ("Science Fiction","Science Fiction"),
    ("Dystopian", "Dystopian"),
    ("Adventure", "Adventure"),
    ("Romance", "Romance"),
    ("Mystery", "Mystery"),
    ("Horror", "Horror"),
    ("Thriller", "Thriller"),
    ("Historical Fiction", "Historical Fiction"),
    ("Young Adult", "Young Adult"),
    ("Children's Fiction", "Children's Fiction"),
    ("Memoir & Autobiography", "Memoir & Autobiography"),
    ("Biography", "Biography"),
    ("Cooking", "Cooking"),
    ("Art & Photography", "Art & Photography"),
    ("Self-Help/Personal Development", "Self-Help/Personal Development"),
    ("Motivational/Inspirational", "Motivational/Inspirational"),
    ("Health & Fitness", "Health & Fitness"), 
    ("History", "History"),
    ("Crafts, Hobbies & Home", "Crafts, Hobbies & Home"),
    ("Family & Relationships", "Family & Relationships"),
    ("Humor & Entertainment", "Humor & Entertainment"),
    ("Business & Money", "Business & Money"),
    ("Law & Criminology", "Law & Criminology"),
    ("Politics & Social Sciences", "Politics & Social Sciences"),
    ("Religion & Spirituality", "Religion & Spirituality"),
    ("Education & Teaching", "Education & Teaching"),
    ("Travel", "Travel")
)


class StoryForm(forms.ModelForm):
    
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=options)
    class Meta:
        model = StoryModel
        fields = ['content']
        genres = ['genre']
