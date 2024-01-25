from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
import RPi.GPIO as GPIO
from flask import Flask
import os

from .forms import CreateUserForm

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('admin')
        return render(request,"index.html")
    else:
        GPIO.cleanup()
        return render(request,"index.html")
    

def select(request):
    return render(request,"select.html")
    
@login_required(login_url='/index/')
def admin(request):
    users = User.objects.all()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso')
            return redirect('admin')
        else:
            for field in form.errors:
                for error in form.errors[field]:
                    if error == "A user with that username already exists.":
                        messages.error(request, "Um utilizador com esse nome á existe.")
                    else:
                        messages.error(request, f"{field}: {error}")
    else:
        form = CreateUserForm()

    return render(request, "admin.html", {'form': form, 'users': users})


def UserLogout(request):
    logout(request)
    return redirect('index')
    
def DeleteUser(request):    
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            duser = User.objects.get(username=username)
            duser.delete()
            messages.success(request, "O user foi apagado com sucesso")
        except User.DoesNotExist:
            messages.error(request, "User não encontrado")    
        return redirect('admin')

def desligar(request):
    os.system('sudo shutdown now')
    return 'A desligar o Raspberry Pi...'
    
def reboot(request):
    os.system('sudo reboot now')
    return 'A reiniciar o Raspberry Pi...'

