from django.contrib import admin
from apps.Catalogos.Examen.models import Examen

@admin.register(Examen)
class ExamenAdmin(admin.ModelAdmin):
    search_fields = ['id','NumExamen']
    list_display = ['NumExamen','Nombres','FecExamen','Resultado','Descripcion']
# Register your models here.
