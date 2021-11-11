from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.getBooks, name='search'),
    path('help/', views.help, name='help'),
    path('info/', views.info, name='info'),
    path('donate/', views.donate, name='donate'),
    path('category/', views.category, name='category'),
]