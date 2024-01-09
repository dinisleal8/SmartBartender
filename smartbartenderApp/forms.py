from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserForm
from .models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
# views.py


def criar_conta(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user, category='guest')  # Pode ser 'admin' para criar um admin
            return redirect('listar_usuarios')
    else:
        form = UserForm()
    return render(request, 'criar_conta.html', {'form': form})

def listar_usuarios(request):
    usuarios = UserProfile.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})
