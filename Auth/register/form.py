from typing import __all__
from django import forms
from .models import *

class registerForm(forms.ModelForm):
  class Meta:
    model = register
    fields = '__all__'
    label = {
      'full_name' : 'Full Name',
      'email' : 'Email Address',
      'user_name' : 'Username',
      'password' : 'Password',
      'confirm_password' : 'Confirm Password'
    }
    widgets = {
      'full_name': forms.TextInput(attrs={
          'class': 'form-control',
          'placeholder': 'Enter your full name'
      }),
      'email': forms.EmailInput(attrs={
          'class': 'form-control',
          'placeholder': 'Enter your email'
      }),
      'user_name': forms.TextInput(attrs={
          'class': 'form-control',
          'placeholder': 'Enter a username'
      }),
      'password': forms.PasswordInput(attrs={
          'class': 'form-control',
      }),
      'confirm_password': forms.PasswordInput(attrs={
          'class': 'form-control',
      })}
    error_messages={
      "full_name" : {
        'required' : "Your full name must not be empty.",
        'max_length': "Your name is too long."
      },
      "email" : {
        'required' : "Your email must not be empty.",
        'invalid': 'Please enter a valid email address.',
      },
      "user_name" : {
        'required' : "Your user name must not be empty.",
        'max_length': "Your user name is too long."
      },
      "password" : {
        'required' : "Your password  must not be empty.",
        'max_length': "Your password should be in max lenght : 128"
      },
      "confirm_password" : {
        'required' : "Your confirm password  must not be empty.",
        'max_length': "Your confirm password should be in max lenght : 128"
      },
    }
    