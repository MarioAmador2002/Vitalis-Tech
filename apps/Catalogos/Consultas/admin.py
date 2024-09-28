from django.contrib import admin
from apps.Catalogos.Consultas.models import Consultas

@admin.register(Consultas)
class ConsultasAdmin(admin.ModelAdmin):
    search_fields = ['id,', 'NumCitas']
    list_display = ['NumCitas', 'Fecha','Razon','Hora','Nombre','Apellido','Estado','Costo',]

# Register your models here.
