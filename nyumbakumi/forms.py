from django import forms
from .models import Profile, Post

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']

class BlogPostForm(forms.ModelForm):
    class Meta:
        model=BlogPost
        exclude=['username','neighbourhood','avatar']        