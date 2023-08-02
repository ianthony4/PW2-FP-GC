from rest_framework import serializers

from .models import Activo,Pasivo

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
