from django.contrib import admin
from django.urls import path
from . import views
from . import drinks

urlpatterns = [
    path("index/", views.index, name='index'),
    path("select/", views.select),
    path("drink1/", drinks.drink1),
    path("drink2/", drinks.drink2),
    path("drink3/", drinks.drink3),
    path("drink4/", drinks.drink4),
    path("drink5/", drinks.drink5),
    path("drink6/", drinks.drink6),
    path('admin/', views.admin, name='admin'),
    
]
