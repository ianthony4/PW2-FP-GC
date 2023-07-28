from django.db import models

# Create your models here.

class Caja(models.Model):
    id_caja = models.CharField(max_length=100)
    saldo = models.DecimalField(decimal_places=2)

    def __str__(self):
        return self.saldo

class Banco(models.Model):
    id_bank = models.CharField(max_length=100)
    name_bank = models.CharField(max_length=100)
    type_bank = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name_bank

class Cuenta(models.Model):
    type_account = models.CharField(max_length=100)
    activos = models.IntegerField()
    pasivos = models.IntegerField()
    id_cuenta = models.IntegerField()
    mov_deudor = models.IntegerField()
    mov_acreedor = models.IntegerField()

    def __str__(self):
        return self.id_cuenta

class Pasivos(models.Model):
    id_pasivo = models.IntegerField()
    type = models.CharField(max_length=100)
    subtype = models.CharField(max_length=100)
    subsubtype = models.CharField(max_length=100)
    name_pasivo = models.CharField(max_length=100)
    saldo = models.DecimalField(decimal_places=2)
    
    def __str__(self):
        return self.name_activo
class Activos(models.Model):
    id_pasivo = models.IntegerField()
    type = models.CharField(max_length=100)
    subtype = models.CharField(max_length=100)
    subsubtype = models.CharField(max_length=100)
    name_activo = models.CharField(max_length=100)
    saldo = models.DecimalField(decimal_places=2)

    def __str__(self):
        return self.name_activo
class CatalogoCuentas(models.Model):
    id_catalogo = models.CharField(max_length=100)
    id_created = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date = models.DateField()
    type_catalog = models.CharField(max_length=100)

    # clientes = models.ManyToManyField(Clientes)
    
    activos = models.ManyToManyField(Activos)

    pasivos = models.ManyToManyField(Pasivos)

    patrimonio_neto = models.DecimalField(decimal_places=2)

    gastos = models.DecimalField(decimal_places=2)
    ingresos = models.DecimalField(decimal_places=2)
    
    saldo_intermediario = models.DecimalField(decimal_places=2)

    cuentas_de_orden = models.ManyToManyField(Cuenta)

    # contador = models.ForeingKey()
    
    def __str__(self):
        return self.name
