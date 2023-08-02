from django.contrib import admin
from .models import Banco,Cuenta,Pasivo,Activo,CatalogoCuentas,Country
# Register your models here.

admin.site.register(Cuenta)
admin.site.register(CatalogoCuentas)
admin.site.register(Banco)
admin.site.register(Pasivo)
admin.site.register(Activo)
admin.site.register(Country)