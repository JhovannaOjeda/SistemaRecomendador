from django import forms
from .models import Suscriptor

class SuscribirForm(forms.ModelForm):
    class Meta:
        model = Suscriptor
        fields = "__all__"
        labels = {
            'name': 'Nombre',
            'lastname': 'Apellidos',
            'username': 'Nombre de Usuario',
            'email': 'Correo',
            'password': 'Contraseña'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo@gmail.com'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
        }
