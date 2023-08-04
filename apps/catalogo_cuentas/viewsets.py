from .models import Activo,Pasivo,CatalogoCuentas
from .serializers import ActivoSerializer,PasivoSerializer,CatalogoCuentasSerializer
from rest_framework import viewsets

class ActivoViewSet(viewsets.ModelViewSet):
    queryset = Activo.objects.all()
    serializer_class = ActivoSerializer 

class PasivoViewSet(viewsets.ModelViewSet):
    queryset = Pasivo.objects.all()
    serializer_class = PasivoSerializer 

class CatalogoCuentasViewSet(viewsets.ModelViewSet):
    queryset = CatalogoCuentas.objects.all()
    serializer_class = CatalogoCuentasSerializer 


