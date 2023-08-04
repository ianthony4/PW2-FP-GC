from .models import Cuenta,Activo,Pasivo,Country,Banco,TypeAccount,SubTypeAccount
from django import forms
from django.utils.safestring import mark_safe
from apps.user.models import ClienteProfile

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
    banco = forms.ModelChoiceField(
            queryset=Banco.objects.all(),
            required=False,
            empty_label="Selecciona banco",
        )

    activos = forms.ModelMultipleChoiceField(
            queryset=Activo.objects.all(),
            required=False,
            widget=forms.CheckboxSelectMultiple
        )

    pasivos = forms.ModelMultipleChoiceField(
            queryset=Pasivo.objects.all(),
            required=False,
            widget=forms.CheckboxSelectMultiple
        )

    patrimonio_neto =  forms.DecimalField()

    cliente = forms.ModelChoiceField(
            queryset=ClienteProfile.objects.all(),
            required=False,
    )

    gastos = forms.DecimalField()
    ingresos = forms.DecimalField()
    name = forms.CharField(max_length=100)
    saldo_intermediario = forms.DecimalField()

    cuentas_de_orden = forms.ModelMultipleChoiceField(
            queryset=Cuenta.objects.all(),
            required=False,
            widget=forms.CheckboxSelectMultiple
        )
    
class RawCuentaForm(forms.Form):
    type_account = forms.ChoiceField(
        choices = TYPE_ACCOUNT_CHOICES,
        widget= forms.RadioSelect(
            attrs= {
                    'class':'account_select',
                }
            ) 
        )
    name = forms.CharField()
    pasivo = forms.DecimalField()
    activo = forms.DecimalField()
    
class RawCountryForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    
    name.widget.attrs.update(
        {
            "name":"name_country",
        }
    )
    description.widget.attrs.update(
        {
            "name":"description_country",
        }
    )

class RawBancoForm(forms.Form):
    name_bank = forms.CharField()
    description = forms.CharField()
    type_bank = forms.CharField()
    description = forms.CharField()
    
    name_bank.widget.attrs.update(
        {
            "name":"name_country",
        }
    )
    description.widget.attrs.update(
        {
            "name":"description_country",
        }
    )
class RawActivoForm(forms.Form):
    name = forms.CharField()   
    saldo = forms.DecimalField()
    type = forms.ModelChoiceField(
            queryset=TypeAccount.objects.all(),
            required=False,
            empty_label="Selecciona tipo de cuenta",
        )
    subtype = forms.ModelChoiceField(
            queryset=SubTypeAccount.objects.all(),
            required=False,
            empty_label="Selecciona subtipo de cuenta",
        )

class RawPasivoForm(forms.Form):
    name = forms.CharField()   
    saldo = forms.DecimalField()
    type = forms.ModelChoiceField(
            queryset=TypeAccount.objects.all(),
            required=False,
            empty_label="Selecciona tipo de cuenta",
        )
    subtype = forms.ModelChoiceField(
            queryset=SubTypeAccount.objects.all(),
            required=False,
            empty_label="Selecciona subtipo de cuenta",
        )
