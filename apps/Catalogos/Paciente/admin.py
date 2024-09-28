from django.contrib import admin
from apps.Catalogos.Paciente.models import Paciente

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    search_fields = ['id,','Codigo']
    list_display = ['Codigo','Nombres','Apellidos','FecNacimiento','Direccion','Telefono']
# Register your models here.
