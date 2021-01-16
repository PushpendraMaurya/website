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
<<<<<<< HEAD

def blog(request):
       return  render  (request, 'blog.html')
=======
<<<<<<< HEAD

def blog(request):
       return  render  (request, 'blog.html')
=======
>>>>>>> 28e88f75b086ceebc1a9a95b309a3924ffbd2fad
>>>>>>> 0e958f9eecc155a4ae4967d90f45f998f869c7f3
    

    


