from django.contrib import admin
from django.urls import path
from . import views
from . import drinks
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("index/", views.index, name='index'),
    path("select/", views.select),
    path("ferrar/", drinks.ferrar),
    path("drink1/", drinks.drink1),
    path("drink2/", drinks.drink2),
    path("drink3/", drinks.drink3),
    path("drink4/", drinks.drink4),
    path("drink5/", drinks.drink5),
    path("drink6/", drinks.drink6),
    path('admin/', views.admin, name='admin'),
    path('logout/', views.UserLogout, name='logout'),
    path('delete_user/', views.DeleteUser, name='delete_user'),
    path('desligar/', views.desligar, name='desligar'),
	path('reiniciar/', views.reboot, name='reboot')
]
