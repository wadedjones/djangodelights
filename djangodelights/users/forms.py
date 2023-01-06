from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'id':'password1-form',
        })
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'id':'password2-form',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class':'form-control',
                'id':'username-form',
            }),
            'email': forms.TextInput(attrs={
                'class':'form-control',
                'id':'email-form',
            }),
        }