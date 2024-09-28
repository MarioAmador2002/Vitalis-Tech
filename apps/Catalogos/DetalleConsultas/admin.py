from django.contrib import admin
from apps.Catalogos.DetalleConsultas.models import DetalleConsultas

@admin.register(DetalleConsultas)
class DetalleConsultasAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['Diagnostico','Tratamiento']

# Register your models here.
