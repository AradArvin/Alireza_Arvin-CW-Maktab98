from django.forms import ModelForm
from django import forms
from .models import CustomUser


class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
