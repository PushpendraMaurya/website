from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("form", views.form, name='form '),
    path("books", views.books, name='books'),
    path("contact", views.contact, name='contact'),
    path("pdf", views.pdf, name='pdf'),
<<<<<<< HEAD
    path("blog", views.blog, name='blog')
=======
>>>>>>> 28e88f75b086ceebc1a9a95b309a3924ffbd2fad
  
]