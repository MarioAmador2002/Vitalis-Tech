from django.db import models
"""
Examen
"""
class Examen(models.Model):
    NumExamen = models.IntegerField(verbose_name='NumExamen')
    Nombres = models.CharField(verbose_name='Nombres',max_length=60)
    FecExamen = models.DateField(verbose_name='FecExamen')
    Resultado = models.CharField(verbose_name='Resultado',max_length=60)
    Descripcion = models.CharField(verbose_name='Descripcion',max_length=60)

    class Meta:
        verbose_name_plural = 'Examens'

    def __str__(self):
        return f'{self.NumExamen}-{self.Nombres}-{self.FecExamen}-{self.Resultado}-{self.Descripcion}'


# Create your models here.
