from django.contrib import admin
from apps.Catalogos.DetalleExamenes.models import DetalleExamenes

@admin.register(DetalleExamenes)
class DetalleExamenesAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['TipoExamen','Estado','Costo','Observacion']

# Register your models here.
