from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def index(request):
    return render(request,"index.html")

def select(request):
    return render(request,"select.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/admin/')  # Redireciona para o painel de administração após o login bem-sucedido
        else:
            return render(request, 'login.html', {'error': 'Credenciais inválidas.'})

    return render(request, 'login.html')

def admin_view(request):
    return render(request, 'admin.html')

