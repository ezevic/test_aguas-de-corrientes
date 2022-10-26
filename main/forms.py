from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Palindromo


# class to define the form
class PalindromoForm(forms.ModelForm):

    class Meta:
        model = Palindromo
        fields = ['palabra']

        labels = {
            'palabra': ''
        }

        widgets = {

            'palabra': forms.TextInput(attrs={'class': 'form-control-lg w-100', 'placeholder': 'Ingresa una palabra o frase', 'required': True})
        }


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
