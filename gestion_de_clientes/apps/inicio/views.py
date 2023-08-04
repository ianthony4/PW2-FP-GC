from django.shortcuts import render
from apps.user.models import ContadorProfile
# Create your views here.

def index(request, *args, **kwargs):
    queryset = ContadorProfile.objects.all()
    context = {
        'contador':queryset
    }
    return render(request, 'index.html',context)

def about(request, *args, **kwargs):
    return render(request, 'about.html',{})

def contact(request, *args, **kwargs):
    return render(request, 'contact.html',{})

def services(request, *args, **kwargs):
    return render(request, 'services.html',{})