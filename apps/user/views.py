from django.shortcuts import render
from django.views.generic import View,DetailView
from .models import ClienteProfile,ContadorProfile
from apps.catalogo_cuentas.models import CatalogoCuentas

# Create your views here.

class ClienteDetailView(DetailView):
    model = ClienteProfile
    template_name = 'cliente_perfil.html'
    context_object_name = 'cliente'
    pk_url_kwarg = 'cliente_id'

    def get_context_data(self, **kwargs):
        context = super(ClienteDetailView, self).get_context_data(**kwargs)
        cliente= ClienteProfile.objects.get(name=str(context['object']))
        catalogo = CatalogoCuentas.objects.filter(cliente=cliente.cliente_id)
        context['catalogo'] = catalogo 
        return context

class ContadorDetailView(DetailView):
    model = ContadorProfile
    template_name = 'contador_perfil.html'
    context_object_name = 'contador'
    pk_url_kwarg = 'contador_id'

    def get_context_data(self, **kwargs):
        context = super(ContadorDetailView, self).get_context_data(**kwargs)
        contador= ContadorProfile.objects.get(name=str(context['object']))
        catalogo = CatalogoCuentas.objects.filter(contador=contador.contador_id)
        context['catalogo'] = catalogo 
        return context