from django.db import models


"""
Genero
"""
class Genero(models.Model):
    Descripcion =  models.CharField(verbose_name='Descripcion',max_length=60)

    class Meta:
        verbose_name_plural = 'Genero'

    def __str__(self):
        return f'{self.Descripcion}'



# Create your models here.
