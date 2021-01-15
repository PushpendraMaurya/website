from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return  render  (request, 'index.html')
    #return HttpResponse ("this is homepage")

def about(request):
    return HttpResponse ("this is aboutpage")

def services(request):
    return HttpResponse ("this is services")

def contact(request):
    return HttpResponse ("this is contact")
    

    


