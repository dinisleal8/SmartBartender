from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
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
    
@login_required(login_url='/index/')
def admin(request):
    users = User.objects.all()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin') 
    else:
        form = CreateUserForm()

    return render(request, "admin.html", {'form': form,'users': users})

def UserLogout(request):
    logout(request)
    return redirect('index')
    
def DeleteUser(request, username):    
    try:
        duser = User.objects.get(username = username)
        duser.delete()
        messages.sucess(request, "The user is deleted")
    except:
      messages.error(request, "The user not found")    
    return render(request, 'front.html')
