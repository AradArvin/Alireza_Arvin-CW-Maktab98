from django.forms import ModelForm
from django import forms
from .models import CustomUser


class CreateUserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password"]

    def clean_data(self):
        cleaned_data = super(CustomUser, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Password confirmation failed")


class LoginUserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    # class Meta:
    #     model = CustomUser
    #     fields = ["username", "password"]
