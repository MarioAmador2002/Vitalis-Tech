from django.db import models

"""
Medicamento
"""
class Medicamento(models.Model):
    Nombre = models.CharField(verbose_name="Nombre", max_length=50)
    Descripcion = models.CharField(verbose_name="Descripcion",max_length=50)
    NombreGenerico = models.CharField(verbose_name="NombreGenerico", max_length=50)
    Presentacion = models.CharField(verbose_name="Presentacion", max_length=50)
    Contradicciones = models.CharField(verbose_name="Contradicciones", max_length=50)
    EfectosSecundarios = models.CharField(verbose_name="EfectosSecundarios", max_length=50)

    class Meta:
        verbose_name_plural = "Medicamentos"

    def __str__(self):
        return f' {self.Nombre}-{self.Descripcion}-{self.NombreGenerico}-{self.Presentacion}-{self.Contradicciones}-{self.EfectosSecundarios}'


# Create your models here.
