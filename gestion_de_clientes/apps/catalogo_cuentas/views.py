from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import RawCatalogoForm,RawCuentaForm,RawCountryForm,RawActivoForm,RawPasivoForm
from .models import CatalogoCuentas
from django.views.generic import View,DetailView
from django.template.loader import get_template
from .utils import render_to_pdf #created in step 4

# Create your views here.


def newCatalogo(request):
    form = RawCatalogoForm()
    context = {
        'form': form,
    }

    return render(request, 'createNewCatalog.html',context) 

class CatalogoDetailView(DetailView):
    model = CatalogoCuentas
    template_name = 'catalogo_detail.html'

def newCountryForm(request):
    form = RawCountryForm()
    context = {
        'form': form,
    }
    return render(request, 'newCountry.html',context) 

def saveCountry(request):
    form = request
    print(request)
    return redirect('/')

def newPasivoForm(request):
    form = RawPasivoForm()
    context = {
        'form': form,
    }
    print(form)
    return render(request, 'newPasivo.html',context) 

def newActivoForm(request):
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