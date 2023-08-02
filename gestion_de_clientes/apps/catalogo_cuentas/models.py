from django.db import models
# Create your models here.
class Banco(models.Model):
    id_bank = models.CharField(blank=True, max_length=100)
    name_bank = models.CharField(blank=True, max_length=100)
    type_bank = models.CharField(blank=True, max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name_bank

class Country(models.Model):
    id_country = models.CharField(blank=True,max_length=100)
    name = models.CharField(blank=True,max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
class Cuenta(models.Model):
    type_account = models.CharField(blank=True, max_length=100)
    date = models.DateField(auto_now=True )
    activos = models.IntegerField(blank=True, )
    pasivos = models.IntegerField(blank=True, )
    id_cuenta = models.IntegerField(blank=True, )
    mov_deudor = models.IntegerField(blank=True, )
    mov_acreedor = models.IntegerField(blank=True, )
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Pasivo(models.Model):
    id_pasivo = models.IntegerField(blank=True, )
    date = models.DateField(auto_now=True)
    type = models.CharField(blank=True, max_length=100)
    subtype = models.CharField(blank=True, max_length=100)
    subsubtype = models.CharField(blank=True, max_length=100)
    name_pasivo = models.CharField(blank=True, max_length=100)
    saldo = models.DecimalField(blank=True,max_digits=20, decimal_places=2)
    
    def __str__(self):
        return self.name_pasivo
class Activo(models.Model):
    id_activo = models.IntegerField(blank=True, )
    date = models.DateField(auto_now=True )
    type = models.CharField(blank=True, max_length=100)
    subtype = models.CharField(blank=True, max_length=100)
    subsubtype = models.CharField(blank=True, max_length=100)
    name_activo = models.CharField(blank=True, max_length=100)
    saldo = models.DecimalField(blank=True,max_digits=20, decimal_places=2)

    def __str__(self):
        return self.name_activo
class CatalogoCuentas(models.Model):
    id_catalogo = models.CharField(blank=True, max_length=100)
    id_created = models.CharField(blank=True, max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    date = models.DateField( auto_now=True )
    type_catalog = models.CharField(blank=True, max_length=100)
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE )

    # clientes = models.ManyToManyField(Cliente)
    
    activos = models.ManyToManyField(Activo,blank=True, )

    pasivos = models.ManyToManyField(Pasivo,blank=True,)

    patrimonio_neto = models.DecimalField(blank=True,max_digits=20, decimal_places=2)

    gastos = models.DecimalField(blank=True,max_digits=20, decimal_places=2)
    ingresos = models.DecimalField(blank=True,max_digits=20, decimal_places=2)
    
    saldo_intermediario = models.DecimalField(blank=True,max_digits=20, decimal_places=2)

    cuentas_de_orden = models.ManyToManyField(Cuenta, blank=True )

    # contador = models.ForeingKey()
    
    def __str__(self):
        return self.id_catalogo

