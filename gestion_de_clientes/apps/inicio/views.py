from django.shortcuts import render

# Create your views here.

def index(request, *args, **kwargs):
    return render(request, 'index.html',{})

def about(request, *args, **kwargs):
    return render(request, 'about.html',{})

def contact(request, *args, **kwargs):
    return render(request, 'contact.html',{})

def services(request, *args, **kwargs):
    return render(request, 'services.html',{})