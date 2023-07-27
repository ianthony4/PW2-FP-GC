from .models import Cuenta,CatalogoCuentas
from django import forms

TYPE_ACCOUNT_CHOICES = (
    ('Numerico','Numerico'),
    ('Albafetico', 'Albafetico'),
    ('Alfanumerico', 'Alfanumerico'),
)

TYPE_CATALOG_CHOICES = {
    ('Cuenta de activo','Cuenta de activo'),
    ('Cuenta de pasivo','Cuenta de pasivo'),
    ('Cuenta de capital','Cuenta de Capital'),
    ('Cuenta de orden','Cuenta de orden'),

}

class RawCuentaForm(forms.Form):
    type_account = forms.ChoiceField(
        choices = TYPE_ACCOUNT_CHOICES,
        widget= forms.RadioSelect(
            attrs= {
                    'class':'account_select',
                }
            ) 
        )

class RawCatalogoForm(forms.Form):
    type_catalogo = forms.ChoiceField(
        choices = TYPE_CATALOG_CHOICES,
        widget= forms.RadioSelect(
            attrs= {
                    'class':'catalog_select',
                }
            ) 
        )