from .models import Cuenta,Activos,Pasivos,Country
from django import forms
from django.utils.safestring import mark_safe

TYPE_CATALOG_CHOICES = (
    ('Numerico','Numerico'),
    ('Albafetico', 'Albafetico'),
    ('Alfanumerico', 'Alfanumerico'),
)

TYPE_ACCOUNT_CHOICES = {
    ('Cuenta de activo','Cuenta de activo'),
    ('Cuenta de pasivo','Cuenta de pasivo'),
    ('Cuenta de capital','Cuenta de Capital'),
    ('Cuenta de orden','Cuenta de orden'),

}

class RawCatalogoForm(forms.Form):
    type_catalogo = forms.ChoiceField(
        choices = TYPE_CATALOG_CHOICES,
        widget= forms.RadioSelect(
            attrs= {
                    'class':'catalog_select',
                }
            ) 
        )
    country = forms.ModelChoiceField(
            queryset=Country.objects.all(),
            required=False,
            empty_label="Selecciona pais",
        )

    activos = forms.ModelChoiceField(
            queryset=Activos.objects.all(),
            required=False,
            empty_label="Selecciona activos",
        )

    pasivos = forms.ModelChoiceField(
            queryset=Activos.objects.all(),
            required=False,
            empty_label="Selecciona activos",
        )

    patrimonio_neto =  forms.DecimalField()

    gastos = forms.DecimalField()
    ingresos = forms.DecimalField()

    saldo_intermediario = forms.DecimalField()
    
class RawCuentaForm(forms.Form):
    type_account = forms.ChoiceField(
        choices = TYPE_ACCOUNT_CHOICES,
        widget= forms.RadioSelect(
            attrs= {
                    'class':'account_select',
                }
            ) 
        )
    
    
