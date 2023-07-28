from django.contrib import admin
from django.urls import path
from .views import GeneratePdf
from .views import newCatalogo,getResponse

urlpatterns = [
    path('', newCatalogo, name = 'catalogo'),
    path('get/', getResponse, name = 'response'),
    path('renderpdf/',GeneratePdf.as_view(), name="pdf"),
]