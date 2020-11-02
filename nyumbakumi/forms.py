from django import forms
from .models import Profile, Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        exclude=['username','neighbourhood','avatar']        