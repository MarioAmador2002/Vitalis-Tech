from django.db import models

"""
Enfermedades
"""
class Enfermedades(models.Model):
    Nombre = models.CharField(verbose_name='Nombre', max_length=80)
    Descripcion = models.CharField(verbose_name='Descripcion', max_length=80)
    Sintomas = models.CharField(verbose_name='Sintoma', max_length=80)
    Tratamientos = models.CharField(verbose_name='Tratamientos', max_length=80)

    class Meta:
        verbose_name_plural = 'Enfermedades'

    def __str__(self):
        return f'{self.Nombre} - {self.Descripcion}- {self.Sintomas} - {self.Tratamientos}'

# Create your models here.
