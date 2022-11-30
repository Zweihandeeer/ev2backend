from django import forms
from django.forms import ModelForm

from velasquezluis.models import Chat

# Formulario de ingreso de datos de los chats.
class ChatForm(ModelForm):
    class Meta:
        model = Chat
        fields = ['id','chat', 'user']

# Formulario de inicio de sesión.
class LoginForm(forms.Form):
    email = forms.CharField(
        max_length=250, min_length=3, label='Ingrese su nombre de usuario')
    password = forms.CharField(min_length=8, max_length=16,
                               label='Ingrese su contraseña', widget=forms.PasswordInput())
