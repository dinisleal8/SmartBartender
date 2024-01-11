from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django import forms

class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = User
        fields = []

class UserAdmin(BaseUserAdmin):
    delete_form = UserDeleteForm
    actions = ['delete_selected_users']

    def delete_selected_users(self, request, queryset):
        for user in queryset:
            user.delete()
        self.message_user(request, f'User apagado com sucesso.')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
