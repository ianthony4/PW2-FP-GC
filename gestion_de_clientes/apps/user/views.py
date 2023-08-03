from django.shortcuts import render
from django.views.generic import View,DetailView
from .models import ClienteProfile,ContadorProfile

# Create your views here.

class ClienteDetailView(DetailView):
    model = ClienteProfile
    template_name = 'cliente_perfil.html'
    context_object_name = 'cliente'
    pk_url_kwarg = 'cliente_id'

class ContadorDetailView(DetailView):
    model = ContadorProfile
    template_name = 'contador_perfil.html'
    context_object_name = 'contador'
    pk_url_kwarg = 'contador_id'