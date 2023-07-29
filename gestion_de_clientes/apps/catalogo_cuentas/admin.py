from django.contrib import admin
from .models import Banco,Cuenta,Pasivos,Activos,CatalogoCuentas,Country
# Register your models here.

admin.site.register(Cuenta)
admin.site.register(CatalogoCuentas)
admin.site.register(Banco)
admin.site.register(Pasivos)
admin.site.register(Activos)
admin.site.register(Country)