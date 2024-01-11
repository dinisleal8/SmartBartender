from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User


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
        return render(request,"index.html")
    

def select(request):
    return render(request,"select.html")

def admin(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin') 
    else:
        form = CreateUserForm()

    context = {'form': form}
    return render(request, "admin.html", context)
