from django.contrib import admin
from django.urls import path
from .views import GeneratePdf
from .views import (newCatalogo,
                    newCountryForm,
                    newPasivoForm,
                    newAccountForm,
                    newActivoForm,
                    newBancoForm,
                    CatalogoDetailView,
                    ActivoDetailView,
                    PasivoDetailView
                    )
from .views import newCatalogo,newCountryForm,saveCountry,newPasivoForm,newActivoForm,CatalogoDetailView, loginView, homeView

urlpatterns = [
    path('', newCatalogo, name = 'catalogo'),
    
    path('newCountry/', newCountryForm, name = 'response'),
    path('newPasivo/',newPasivoForm , name = 'response'),
    path('newActivo/', newActivoForm, name = 'response'),
    path('newAccount/', newAccountForm, name = 'response'),
    path('newBank/', newBancoForm, name = 'response'),

    path('catalogo/<int:pk>',CatalogoDetailView.as_view()),
    path('activo/<int:pk>',ActivoDetailView.as_view()),
    path('pasivo/<int:pk>',PasivoDetailView.as_view()),
    path('login/', loginView, name='login'),
    path('home/', homeView, name='home'),
    path('<int:pk>',CatalogoDetailView.as_view())
]