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
from django.contrib.auth.models import User 
from apps.user.models import ClienteProfile,ContadorProfile
# Create your views here.

############################################################
# VIEWS
class CatalogoDetailView(DetailView):
    model = CatalogoCuentas
    template_name = 'view/catalogo_detail.html'
    context_object_name = 'catalogo'
    pk_url_kwarg = 'id_catalogo'
class ActivoDetailView(DetailView):
    model = Activo
    template_name = 'view/activo_detail.html'
    context_object_name = 'activo'
    pk_url_kwarg = 'id_activo'

class PasivoDetailView(DetailView):
    model = Pasivo
    template_name = 'view/pasivo_detail.html'
    context_object_name = 'pasivo'
    pk_url_kwarg = 'id_pasivo'

#########################################################
# NEWS

def newCatalogo(request):

    if request.method=='POST':

        print(request.user)
        pasivos = request.POST.getlist('pasivos')
        activos = request.POST.getlist('activos')
        cuentas = request.POST.getlist('cuentas')
        country = request.POST['country']
        type_catalogo= request.POST['type_catalogo']
        patrimonio_neto = request.POST['patrimonio_neto']
        gastos = request.POST['gastos']
        banco = request.POST['banco']
        ingresos = request.POST['ingresos']
        saldo_intermediario = request.POST['saldo_intermediario']
        dateToday = date.today()
        name = request.POST['name']
        cliente = request.POST['cliente']

        if name is not None:
            user = User.objects.get(username=request.user)
            contador = ContadorProfile.objects.get(user_id=user.id)
            CatalogoCuentas.objects.create(
                country_id=country,
                name=name,
                date=dateToday,
                type_catalog=type_catalogo,
                banco_id=banco,
                patrimonio_neto=patrimonio_neto,
                gastos=gastos,
                ingresos=ingresos,
                saldo_intermediario=saldo_intermediario,
                cliente=cliente,
                contador=contador.contador_id,
            )
            return redirect('/user/contador/'+str(contador.contador_id))

    form = RawCatalogoForm()
    context = {
        'form': form,
    }

    return render(request, 'new/newCatalog.html',context) 

def newCountryForm(request):
    if request.method=='POST':
        name = request.POST['name']
        description = request.POST['description']

        if name is not None:
            Country.objects.create(name=name, description=description)
            return redirect('/')
    
    form = RawCountryForm()
    context = {
        'form': form,
    }
    
    return render(request, 'new/newCountry.html',context) 

def newBancoForm(request):
    if request.method=='POST':
        name = request.POST['name']
        description = request.POST['description']

        if name is not None:
            Country.objects.create(name=name, description=description)
            return redirect('/')
    
    form = RawBancoForm()
    context = {
        'form': form,
    }
    
    return render(request, 'new/newBanco.html',context) 


def newPasivoForm(request):
    if request.method=='POST':
        name_pasivo = request.POST['name']
        saldo_pasivo = request.POST['saldo']
        type_pasivo= request.POST['type']
        subtype_pasivo = request.POST['subtype']
        date_pasivo = date.today()
        
        if name_pasivo is not None:
            Pasivo.objects.create( date=date_pasivo,name_pasivo=name_pasivo, saldo=saldo_pasivo, type=type_pasivo, subtype=subtype_pasivo)
            return redirect('/')
    
    form = RawPasivoForm()
    context = {
        'form': form,
    }
    return render(request, 'new/newPasivo.html',context) 

def newActivoForm(request):
    if request.method=='POST':
        name_activo = request.POST['name']
        saldo_activo = request.POST['saldo']
        type_activo = request.POST['type']
        subtype_activo = request.POST['subtype']
        date_activo = date.today()
        
        if name_activo is not None:
            Activo.objects.create( date=date_activo,name_activo=name_activo, saldo=saldo_activo, type=type_activo, subtype=subtype_activo)
            return redirect('/')
    
    form = RawActivoForm()
    context = {
        'form': form,
    }
    return render(request, 'new/newActivo.html',context) 

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
        
        if name_account is not None:
            Cuenta.objects.create(date=date_account,name=name_account,type_account=type_account,pasivos=pasivo,activos=activo,mov_deudor=mov_deudor,mov_acreedor=mov_acreedor)
            return redirect("/")

    form = RawCuentaForm()
    context = {
        'form': form,
    }
    
    return render(request, 'new/newAccount.html',context) 

##########################################################
class GeneratePdf(View): 
    def get(self, request, *args, **kwargs):
        pdf = request.GET["pdf"]

        catalogo = CatalogoCuentas.objects.get(id_catalogo=pdf)

        context = {
            "catalogo" : catalogo
        } 

        pdf = render_to_pdf('view/catalogo_detail.html',context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Catalogo_%s.pdf" %(12341231)
            content = "inline; filename=%s" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename=%s" %(filename) 
            response['Content-Disposition'] = content
            return response
        return HttpResponse('No Found')
    