from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 

class CreateUserForm(UserCreationForm):
    is_admin = forms.BooleanField(required=False,initial=False,label='is_staff')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'is_staff']

    def save(self):
        user = super(CreateUserForm, self).save(commit=False)
        user.save()

        return user
