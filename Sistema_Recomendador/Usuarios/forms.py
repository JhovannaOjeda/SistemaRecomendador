from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class SuscribirForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo@gmail.com'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
        }

# class SuscribirForm(UserCreationForm):
#     pass
#     labels = {
#         'username': 'Nombre de Usuario',
#         'password1': 'Contraseña',
#         'password2': 'Confirme Contraseña',
#     }
#     widgets = {
#         'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}),
#         'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
#         'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
#     }
