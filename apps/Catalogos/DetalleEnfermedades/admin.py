from django.contrib import admin
from apps.Catalogos.DetalleEnfermedades.models import DetalleEnfermedades


@admin.register(DetalleEnfermedades)
class DetalleEnfermedadesAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['Año']

# Register your models here.
