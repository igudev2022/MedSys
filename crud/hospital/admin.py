from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Pacientes, Medicos, Consulta, Telefones , Estados, Especialidades

admin.site.register(Pacientes)
admin.site.register(Medicos)
admin.site.register(Consulta)
admin.site.register(Telefones)
admin.site.register(Estados)
admin.site.register(Especialidades)



