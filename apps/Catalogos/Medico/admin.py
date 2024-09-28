from django.contrib import admin
from apps.Catalogos.Medico.models import Medico

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    search_fields = ['id,','Codigo']
    list_display = ['Codigo', 'Nombres','Apellidos','FecNacimiento','Direccion','Especialidad','Telefono']

# Register your models here.
