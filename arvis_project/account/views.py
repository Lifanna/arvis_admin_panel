from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, logout
from account import forms

from account.models import CustomUser


def login(request):
    form=forms.LoginForm()
    msg = []
    if request.method == 'POST':
        form=forms.LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    if user.is_staff:
                        print("djhfjhsdfj")
                        return redirect('choice') 
                    else:
                        auth.login(request, user)
                        msg.append("login successful")
                        return redirect('home')
                else:
                    msg.append("disabled account")
            else:
                msg.append("invalid login")

    return render(request, 'account/login.html')
    

def my_logout(request):
    logout(request)
    return redirect('home')


def register(request):
    form = forms.CustomUserForm()
    if request.method == 'POST':
        print('ddd', request.POST)
        form = forms.CustomUserForm(request.POST)
        if form.is_valid():
            print("fdgdf")
            user = form.save(commit=False)  
            user.save()
            return redirect('login')
        else:
            print("xfdds")
    return render(request, "account/register.html", { 'form': form})