from django.db import models
from apps.Catalogos.Consultas.models import Consultas

'''
DetalleConsultas
'''
class DetalleConsultas(models.Model):
    Diagnostico = models.CharField(verbose_name='Diagnostico', max_length=50)
    Tratamiento = models.CharField(verbose_name='Tratamiento', max_length=50)

    consultas = models.ForeignKey(Consultas, verbose_name='Consultas', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'DetalleConsultas'

    def __str__(self):
        return f'{self.Diagnostico} - {self.Tratamiento}'


# Create your models here.
