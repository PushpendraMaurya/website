from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return  render  (request, 'index.html')
    #return HttpResponse ("this is homepage")

def form(request):
   return  render  (request, 'form.html')

def books(request):
       return  render  (request, 'books.html')

def contact(request):
       return  render  (request, 'contact.html')

def pdf(request):
       return  render  (request, 'pdf.html')

def blog(request):
       return  render  (request, 'blog.html')


    

    


