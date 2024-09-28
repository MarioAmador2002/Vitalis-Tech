from django.db import models
from apps.Catalogos.Enfermedades.models import Enfermedades



'''
DetalleEnfermedades
'''
class DetalleEnfermedades(models.Model):
    Año = models.IntegerField(verbose_name='Año')
    Enfermedades = models.ForeignKey(Enfermedades, verbose_name='Consultas', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'DetalleEnfermedades'

    def __str__(self):
        return f'{self.Año}'


# Create your models here.
