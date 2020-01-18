from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import UserRegistrationForm,LoginForm
from django.contrib.auth.views import LoginView ,LogoutView
from django.contrib import messages


def register(request):
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f"{username} created sucessfully")
            return redirect("login")
    else:
        form=UserRegistrationForm()
    return render(request,"accounts/register.html",{'form':form})

class Login(LoginView):
    model = User
    template_name="accounts/login.html"
    authentication_form=LoginForm

class Logout(LogoutView):
    model = User
    template_name="accounts/logout.html"