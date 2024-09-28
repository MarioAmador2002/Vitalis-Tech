from django.db import models

"""
Especialidad
"""
class Especialidad(models.Model):
    Nombre = models.CharField(verbose_name="Nombre", max_length=60)
    Descripcion = models.CharField(verbose_name="Descripcion",max_length=60)
    Estatus = models.CharField(verbose_name="Estatus", max_length=60)
    Fecha = models.DateField(verbose_name="Fecha")
    FechaModificacion = models.DateField(verbose_name="FechaModificacion")

    class Meta:
        verbose_name_plural = "Especialidad"

    def __str__(self):
        return f'{self.Nombre} {self.Descripcion}-{self.Estatus}-{self.Fecha}-{self.FechaModificacion}'



# Create your models here.
