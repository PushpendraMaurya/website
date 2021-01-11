from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    #retrun render (request, 'index.html')
    return HttpResponse ("this is homepage")

def about(request):
    return HttpResponse ("this is aboutpage")

def services(request):
    return HttpResponse ("this is services")

def contact(request):
    return HttpResponse ("this is contact")
    

    


