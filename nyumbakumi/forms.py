from django import forms
from .models import Profile, Post

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        exclude=['username','neighbourhood','avatar']        