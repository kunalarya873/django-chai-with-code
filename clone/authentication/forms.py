from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']
        widgets={
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'username'}),
            'password1': forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'password'}),
            'password2': forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'repeat password'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)