from django.db import models

"""
Consultas
"""
class Consultas(models.Model):
    NumCitas = models.CharField(verbose_name='NumCitas', max_length=50, unique=True)
    Fecha = models.DateField(verbose_name='Fecha')
    Razon = models.CharField(verbose_name='Razon', max_length=50)
    Hora = models.TimeField(verbose_name='Hora', auto_now_add=True)
    Nombre = models.CharField(verbose_name='Nombre', max_length=50)
    Apellido = models.CharField(verbose_name='Apellido', max_length=50)
    Estado = models.CharField(verbose_name='Estado', max_length=50)
    Costo = models.FloatField(verbose_name='Costo')

    class Meta:
        verbose_name_plural = 'Consultas'

    def __str__(self):
        return f'{self.NumCitas} - {self.Nombre} - {self.Apellido} - {self.Estado} - {self.Costo} - {self.Hora} - {self.Fecha} - {self.Razon}'



# Create your models here.
