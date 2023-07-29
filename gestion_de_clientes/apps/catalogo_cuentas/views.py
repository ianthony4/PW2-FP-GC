from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import RawCatalogoForm,RawCuentaForm,RawCountryForm,RawActivoForm,RawPasivoForm
from .models import CatalogoCuentas,Country,Pasivos,Activos
from django.views.generic import View,DetailView
from django.template.loader import get_template
from .utils import render_to_pdf #created in step 4
from datetime import date
# Create your views here.


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

class CatalogoDetailView(DetailView):
    model = CatalogoCuentas
    template_name = 'catalogo_detail.html'
    context_object_name = 'catalogo'

class ActivoDetailView(DetailView):
    model = Activos
    template_name = 'activo_detail.html'
    context_object_name = 'activo'

class PasivoDetailView(DetailView):
    model = Pasivos
    template_name = 'pasivo_detail.html'
    context_object_name = 'pasivo'
    

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

def newPasivoForm(request):
    if request.method=='POST':
        name_pasivo = request.POST['name']
        saldo_pasivo = request.POST['saldo']
        type_pasivo= request.POST['type']
        subtype_pasivo = request.POST['subtype']
        subsubtype_pasivo = request.POST['subsubtype']
        date_pasivo = date.today()
        
        if name_pasivo is not None:
            Pasivos.objects.create(id_pasivo=abs(int(hash(name_pasivo))), date=date_pasivo,name_pasivo=name_pasivo, saldo=saldo_pasivo, type=type_pasivo, subtype=subtype_pasivo, subsubtype=subsubtype_pasivo)
            return redirect('/')
    
    form = RawPasivoForm()
    context = {
        'form': form,
    }
    print(form)
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
            Activos.objects.create(id_activo=abs(int(hash(name_activo))), date=date_activo,name_activo=name_activo, saldo=saldo_activo, type=type_activo, subtype=subtype_activo, subsubtype=subsubtype_activo)
            return redirect('/')
    
    form = RawActivoForm()
    context = {
        'form': form,
    }
    return render(request, 'newActivo.html',context) 
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