from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('tabpacient',views.tabpacient,name="tabpacient"),
    path('cad/',views.cad,name='cad'),
    path('salvar',views.salvar,name='salvar'),
    path('atu/<int:id>',views.atu,name='atu'),
    path('update',views.update,name='update'),
    path('informacoes/<int:id>',views.informacoes,name='informacoes'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('tabmed',views.tabmed,name='tabmed'),
    path('cadmed/',views.cadmed,name="cadmed"),
    path('salvarmed',views.salvarmed,name='salvarmed'),
    path('informacoesmed/<int:id>',views.informacoesmed,name='informacoesmed'),
    path('deletemed/<int:id>',views.deletemed,name='deletemed'),
    path('agendar/', views.agendar, name='agendar'),   
]