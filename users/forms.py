from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .models import Profile


class OurRegistration(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileAvatar(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['avatar']

class ProfileDoc(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['user_file']
