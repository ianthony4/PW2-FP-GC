from rest_framework import serializers

from .models import Activo,Pasivo,CatalogoCuentas

############################################################################
# SERIALIZERS
############################################################################

class ActivoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activo
        fields = ['date','type','subtype','subsubtype','name_activo','saldo']

class PasivoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pasivo 
        fields = ['date','type','subtype','subsubtype','name_activo','saldo']

class CatalogoCuentasSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CatalogoCuentas
        fields = ['date','country','type_catalog','banco','activos','pasivos','patrimonio_neto','gastos','ingresos','saldo_intermediario',]