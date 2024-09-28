from django.contrib import admin
from apps.Catalogos.Enfermedades.models import Enfermedades

@admin.register(Enfermedades)
class EnfermedadesAdmin(admin.ModelAdmin):
    search_fields = ['id','Nombre']
    list_display = ['Nombre','Descripcion','Sintomas','Tratamientos',]

# Register your models here.
