from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('login', views.login, name='login'),
    path('profile', views.profile, name= 'profile'),
]