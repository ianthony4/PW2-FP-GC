from .models import Activo,Pasivo
from .serializers import ActivoSerializer,PasivoSerializer
from rest_framework import viewsets

class ActivoViewSet(viewsets.ModelViewSet):
    queryset = Activo.objects.all()
    serializer_class = ActivoSerializer 

class PasivoViewSet(viewsets.ModelViewSet):
    queryset = Pasivo.objects.all()
    serializer_class = PasivoSerializer 


