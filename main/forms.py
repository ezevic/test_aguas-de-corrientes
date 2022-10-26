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

            'palabra': forms.TextInput(attrs={'class': 'form-control-lg w-100','placeholder': 'Ingresa una palabra o frase' , 'required': True})
        }