from django.db import models

"""
Indicadores
"""
class Indicadores(models.Model):
    Nombres = models.CharField(verbose_name='Nombres',max_length=60)
    UnidadMedida =models.CharField(verbose_name='UnidadMedida',max_length=60)
    ValorReferenciaMax = models.CharField(verbose_name='ValorReferenciaMax',max_length=60)
    ValorReferenciaMin = models.CharField(verbose_name='ValorReferenciaMin',max_length=60)
    Descripcion = models.CharField(verbose_name='Descripcion',max_length=60)

    class Meta:
        verbose_name_plural = 'Indicadores'

    def __str__(self):
        return f'{self.Nombres}-{self.UnidadMedida}-{self.ValorReferenciaMax}-{self.ValorReferenciaMin}-{self.Descripcion}'

# Create your models here.
