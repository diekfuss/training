from django.contrib.auth.models import User
from django import forms
from django.forms.models import inlineformset_factory
from .models import Album, Song


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password']


AlbumSongFormSet = inlineformset_factory(Album,Song)

