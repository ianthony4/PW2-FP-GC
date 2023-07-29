from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import RawCatalogoForm,RawCuentaForm,RawCountryForm,RawActivoForm,RawPasivoForm
from .models import CatalogoCuentas
from django.views.generic import View,DetailView
from django.template.loader import get_template
from .utils import render_to_pdf #created in step 4
from django.contrib.auth import authenticate, login

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
    context_object_name = 'catalogo'

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