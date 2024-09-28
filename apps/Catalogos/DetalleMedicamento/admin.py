from django.contrib import admin
from apps.Catalogos.DetalleMedicamento.models import DetalleMedicamento


@admin.register(DetalleMedicamento)
class DetalleMedicamentoAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['Receta', 'Dosis','Frecuencia','Duracion','Indicacion']







# Register your models here.
