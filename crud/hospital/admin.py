from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Pacientes, Medicos, Consulta

admin.site.register(Pacientes)
admin.site.register(Medicos)
admin.site.register(Consulta)
