from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    Precio = models.DecimalField(max_digits=10, decimal_places=2)
