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
    path('book/', views.selectedBook, name='book'),
    path('book/reserve/', views.reserveBook, name='reserve'),
    path('user/mybooks/', views.myBooks, name='my-books'),
    path('user/mybooks/remove/', views.removeBook, name='remove-books'),
]