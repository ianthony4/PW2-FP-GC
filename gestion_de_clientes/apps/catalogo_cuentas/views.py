from django.shortcuts import (render,HttpResponse,redirect,get_object_or_404)
from .forms import (RawCatalogoForm,
                    RawCuentaForm,
                    RawCountryForm,
                    RawActivoForm,
                    RawPasivoForm,
                    RawBancoForm)
from .models import (CatalogoCuentas,
                    Country,
                    Pasivo,
                    Activo,
                    Cuenta,
                    Banco)
                    
from django.views.generic import View,DetailView
from django.template.loader import get_template
from .utils import render_to_pdf #created in step 4
from datetime import date
from django.contrib.auth import authenticate, login

# Create your views here.

class CatalogoDetailView(DetailView):
    model = CatalogoCuentas
    template_name = 'catalogo_detail.html'
    context_object_name = 'catalogo'

class ActivoDetailView(DetailView):
    model = Activo
    template_name = 'activo_detail.html'
    context_object_name = 'activo'

class PasivoDetailView(DetailView):
    model = Pasivo
    template_name = 'pasivo_detail.html'
    context_object_name = 'pasivo'
    
def newCatalogo(request):

    if request.method=='POST':
        pasivo = request.POST['pasivo']
        activo = request.POST['activo']
        country = request.POST['country']
        type_catalogo= request.POST['type_catalogo']
        patrimonio_neto = request.POST['patrimonio_neto']
        gastos = request.POST['gastos']
        ingresos = request.POST['ingresos']
        saldo_intermediario = request.POST['saldo_intermediario']
        date = date.today()
        
        if country is not None:
            CatalogoCuentas.objects.create(id_catalogo=abs(int(hash(country))),)
            return redirect('/')

    form = RawCatalogoForm()
    context = {
        'form': form,
    }

    return render(request, 'createNewCatalog.html',context) 

def newCountryForm(request):
    if request.method=='POST':
        name = request.POST['name']
        description = request.POST['description']

        if name is not None:
            Country.objects.create(id_country = abs(int(hash(name))),name=name, description=description)
            return redirect('/')
    
    form = RawCountryForm()
    context = {
        'form': form,
    }
    
    return render(request, 'newCountry.html',context) 
def newBancoForm(request):
    if request.method=='POST':
        name = request.POST['name']
        description = request.POST['description']

        if name is not None:
            Country.objects.create(id_country = abs(int(hash(name))),name=name, description=description)
            return redirect('/')
    
    form = RawBancoForm()
    context = {
        'form': form,
    }
    
    return render(request, 'newBanco.html',context) 


def newPasivoForm(request):
    if request.method=='POST':
        name_pasivo = request.POST['name']
        saldo_pasivo = request.POST['saldo']
        type_pasivo= request.POST['type']
        subtype_pasivo = request.POST['subtype']
        subsubtype_pasivo = request.POST['subsubtype']
        date_pasivo = date.today()
        
        if name_pasivo is not None:
            Pasivo.objects.create(id_pasivo=abs(int(hash(name_pasivo))), date=date_pasivo,name_pasivo=name_pasivo, saldo=saldo_pasivo, type=type_pasivo, subtype=subtype_pasivo, subsubtype=subsubtype_pasivo)
            return redirect('/')
    
    form = RawPasivoForm()
    context = {
        'form': form,
    }
    return render(request, 'newPasivo.html',context) 

def newActivoForm(request):
    if request.method=='POST':
        name_activo = request.POST['name']
        saldo_activo = request.POST['saldo']
        type_activo = request.POST['type']
        subtype_activo = request.POST['subtype']
        subsubtype_activo = request.POST['subsubtype']
        date_activo = date.today()
        
        if name_activo is not None:
            Activo.objects.create(id_activo=abs(int(hash(name_activo))), date=date_activo,name_activo=name_activo, saldo=saldo_activo, type=type_activo, subtype=subtype_activo, subsubtype=subsubtype_activo)
            return redirect('/')
    
    form = RawActivoForm()
    context = {
        'form': form,
    }
    return render(request, 'newActivo.html',context) 

def newAccountForm(request):
    if request.method == 'POST':
        type_account = request.POST["type_account"]
        pasivo = request.POST["pasivo"]
        activo = request.POST["activo"]
        name_account = request.POST["name"]
        type_account = request.POST["type_account"]
        date_account = date.today()
        mov_deudor = pasivo
        mov_acreedor = activo
        id_cuenta = abs(int(hash(name_account)))
        
        if name_account is not None:
            Cuenta.objects.create(date=date_account,name=name_account,type_account=type_account,pasivos=pasivo,activos=activo,mov_deudor=mov_deudor,mov_acreedor=mov_acreedor,id_cuenta=id_cuenta)
            return redirect("/")

    form = RawCuentaForm()
    context = {
        'form': form,
    }
    
    return render(request, 'newAccount.html',context) 
class GeneratePdf(View): 
    def get(self, request, *args, **kwargs):

        template = get_template('pdf/invoice.html')

        context = {
            'invoice_id': 123, 
            'customer_name': 'Vladimir Sulla',
            'amount': 12000,
            'today': "Today",
        }
        pdf = render_to_pdf('pdf/invoice.html',context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %(12341231)
            content = "inline; filename=%s" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename=%s" %(filename) 
            response['Content-Disposition'] = content
            return response
        return HttpResponse('No Found')
    
def homeView(request):
    return render(request, 'home.html')

def loginView(request):
    if request.method == "POST":
        us = request.POST["user"]
        ps = request.POST["pass"]
        user = authenticate(request, username=us,password=ps)
        if user is not None:
            login(request, user)
            # Redireccionar a la página deseada después del inicio de sesión exitoso
            return redirect("catalogo")
        else:
            # Mostrar un mensaje de error en la plantilla (opcional)
            error_message = "Nombre de usuario o contraseña incorrectos."
            return render(request, "login.html", {'error_message': error_message})
    return render(request, 'login.html')

