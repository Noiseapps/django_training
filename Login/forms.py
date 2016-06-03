from django import forms
from django.core.exceptions import ValidationError


class MyLoginForm(forms.Form):
    username = forms.CharField(max_length=25, label="Username", widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}), label="Password")

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not username or len(username) == 0:
            raise ValidationError("Username cannot be empty")
        return username

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if not password or len(password) == 0:
            raise ValidationError("Password cannot be empty")
        return password
