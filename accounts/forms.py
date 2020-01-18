from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms

class UserRegistrationForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={
        'class':"form-control"
    }))
    first_name=forms.CharField(widget=forms.TextInput(attrs={
        'class':"form-control"
    }))
    last_name=forms.CharField(widget=forms.TextInput(attrs={
        'class':"form-control"
    }))
    email=forms.EmailField(widget=forms.EmailInput(attrs={
        'class':"form-control"
    }))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':"form-control"
    }))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':"form-control"
    }))

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']


class LoginForm(AuthenticationForm):
    def __init__(self,*args,**kwards):
        super(LoginForm,self).__init__(*args,**kwards)

    username=forms.CharField(widget=forms.TextInput(attrs={
        'class':"form-control"
    }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':"form-control"
    }))
