from django.contrib import admin
from apps.Catalogos.Indicadores.models import Indicadores

@admin.register(Indicadores)
class IndicadoresAdmin(admin.ModelAdmin):
    search_fields = ['id', 'Nombres']
    list_display = ['Nombres', 'UnidadMedida','ValorReferenciaMax','ValorReferenciaMin','Descripcion']
# Register your models here.
