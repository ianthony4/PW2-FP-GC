from django.contrib import admin
from django.urls import path
from .views import GeneratePdf
from .views import RawFormCuenta,getResponse

urlpatterns = [
    path('', RawFormCuenta, name = 'cuenta'),
    path('get/', getResponse, name = 'response'),
    path('renderpdf/',GeneratePdf.as_view(), name="pdf"),
]