

from django.db import models

from clientes.models import Cliente


class Expediente(models.Model):
    expediente = models.CharField(max_length=200, blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    fecha_carga = models.DateField(auto_now=True)
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE
    )
    monto = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return str(self.pk)

# Create your models here.
