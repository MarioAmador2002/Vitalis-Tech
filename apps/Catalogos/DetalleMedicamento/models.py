from django.db import models
from apps.Catalogos.Medicamento.models import Medicamento

'''
DetalleMedicamento
'''
class DetalleMedicamento(models.Model):
    Receta = models.CharField(verbose_name="Receta", max_length=60)
    Dosis = models.CharField(verbose_name="Dosis", max_length=60)
    Frecuencia = models.CharField(verbose_name="Frecuencia", max_length=60)
    Duracion = models.CharField(verbose_name="Duracion", max_length=60)
    Indicacion = models.CharField(verbose_name="Indicacion", max_length=60)

    Medicamento = models.ForeignKey(Medicamento, verbose_name='Medicamento', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'DetalleMedicamento'

    def __str__(self):
        return f'{self.Receta}-{str(self.Dosis)}-{str(self.Frecuencia)}-{str(self.Duracion)}-{str(self.Indicacion)}'


# Create your models here.
