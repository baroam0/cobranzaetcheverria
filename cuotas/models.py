
from django.db import models

from expedientes.models import Expediente


class Cuota(models.Model):
    fecha = models.DateField(auto_now=True)
    expediente = models.ForeignKey(Expediente, on_delete=models.CASCADE) 
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    importe = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.fecha) + "-" + self.descripcion

# Create your models here.
