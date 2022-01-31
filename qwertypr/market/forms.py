from django import forms

from .models import Client


class user_register_form(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'login', 'password', 'email', 'adress', 'phone']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'login': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'adress': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }
