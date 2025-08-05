from django import forms
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Añadimos los atributos que ya tienes en tu HTML a cada campo
        self.fields['username'].widget.attrs.update({
            'id': 'login-user',
            'placeholder': 'Usuario'
        })
        self.fields['password'].widget.attrs.update({
            'id': 'login-password',
            'placeholder': 'Contraseña',
            'type': 'password'
        })