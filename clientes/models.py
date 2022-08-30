
from django.db import models


class Cliente(models.Model):
    apellido = models.CharField(max_length=250, null=True, blank=True)
    nombre = models.CharField(max_length=250, null=True, blank=True)
    numerodocumento = models.IntegerField(null=True)
    domicilio = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.apellido + ', ' + self.nombre

    class Meta:
        verbose_name_plural = "Clientes"


# Create your models here.
