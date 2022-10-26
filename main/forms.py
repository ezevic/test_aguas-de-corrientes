from dataclasses import fields
from django import forms

from .models import Palindromo


# class to define the form
class PalindromoForm(forms.ModelForm):


    class Meta:
        model=Palindromo
        fields = ['palabra']

        labels={
            'palabra': ''
        }

        widgets = {

            'palabra': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingresa una palabra' , 'required': True})
        }