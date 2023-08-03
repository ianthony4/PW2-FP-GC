from django.contrib import admin
from .models import(Banco,
                    Cuenta,
                    TypeAccount,
                    SubTypeAccount,
                    Pasivo,
                    Activo,
                    CatalogoCuentas,
                    Country)
# Register your models here.

admin.site.register(Cuenta)
admin.site.register(CatalogoCuentas)
admin.site.register(Banco)
admin.site.register(TypeAccount)
admin.site.register(SubTypeAccount)
admin.site.register(Pasivo)
admin.site.register(Activo)
admin.site.register(Country)