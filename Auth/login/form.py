from typing import __all__
from django import forms 
from .models import login

class loginForm(forms.ModelForm):
  class Meta:
    model = login
    fields = "__all__"
    label = {
      "email" : "Email",
      "password" : "Password"
    }
    widgets = {
      'email': forms.TextInput(attrs={
          'class': 'form-control',
          'placeholder': 'Enter your email'
      }),
      'password': forms.PasswordInput(attrs={
          'class': 'form-control',
          'placeholder': 'Enter your password'
      }),
    }
    error_messages ={
       "email" : {
        'required' : "Email should not be empty",
      },
      "password" : {
        'required' : "Password should not be empty",
      },
    }