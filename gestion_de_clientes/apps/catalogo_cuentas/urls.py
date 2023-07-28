from django.contrib import admin
from django.urls import path
from .views import GeneratePdf
from .views import newCatalogo,newCountryForm,saveCountry,newPasivoForm,newActivoForm,CatalogoDetailView

urlpatterns = [
    path('', newCatalogo, name = 'catalogo'),
    path('renderpdf/',GeneratePdf.as_view(), name="pdf"),
    path('newCountry/', newCountryForm, name = 'response'),
    path('saveCountry/', saveCountry, name = 'response'),
    path('newPasivo/',newPasivoForm , name = 'response'),
    path('newActivo/', newActivoForm, name = 'response'),

    path('<int:pk>',CatalogoDetailView.as_view())
]