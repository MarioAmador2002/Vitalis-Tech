from django.db import models
from apps.Catalogos.Examen.models import Examen

'''
DetalleExamenes
'''
class DetalleExamenes(models.Model):
    TipoExamen = models.CharField(verbose_name="TipoExamen",max_length=60)
    Estado =models.CharField(verbose_name="Estado",max_length=60)
    Costo = models.IntegerField(verbose_name="Costo",default=0)
    Observacion = models.CharField(verbose_name="Observacion",max_length=60)


    examen = models.ForeignKey(Examen, verbose_name='Examen', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "DetalleExamenes"

    def __str__(self):
        return f'{self.TipoExamen} {self.Estado} {self.Costo } {self.Observacion}'


# Create your models here.
