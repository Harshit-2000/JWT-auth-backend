from django.forms import fields
from django.forms.models import ModelForm
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignUpForm(ModelForm):
    password = forms.CharField(
        max_length=128, min_length=8, widget=forms.PasswordInput(), label="Password")
    confirm_password = forms.CharField(
        max_length=128, min_length=8, widget=forms.PasswordInput(), label="Verify Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'address']

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match")
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
