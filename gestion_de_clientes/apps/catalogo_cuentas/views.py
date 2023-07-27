from django.shortcuts import render,HttpResponse
from .forms import RawCatalogoForm,RawCuentaForm
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf #created in step 4

# Create your views here.


def RawFormCuenta(request):
    form = RawCuentaForm()
    context = {
        'form': form,
    }
    return render(request, 'create.html',context) 
def getResponse(request):
    response = request.POST["type_account"]
    print(response)
    return HttpResponse("Hello Wold") 


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