
from django.db import models


class Cliente(models.Model):
    apellido = models.CharField(max_length=250, null=True, blank=True)
    nombre = models.CharField(max_length=250, null=True, blank=True)
    numerodocumento = models.IntegerField(null=True)
    telefono = models.CharField(max_length=250, null=True, blank=True)
    domicilio = models.CharField(max_length=250, null=True, blank=True)
    profesion = models.CharField(max_length=250, null=True, blank=True) 

    def __str__(self):
        return self.apellido + ', ' + self.nombre
        #return str(self.apellido)

    class Meta:
        verbose_name_plural = "Clientes"


# Create your models here.
