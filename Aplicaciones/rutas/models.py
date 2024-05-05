from django.db import models

# Create your models here.
class rutastrans(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=50)
    pasaje = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.pasaje)