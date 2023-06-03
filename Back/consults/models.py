from django.db import models

class Consulta(models.Model):
    palabra_buscada = models.CharField(max_length=255, unique=True)
    cantidad_busquedas = models.IntegerField(default=1)
    primera_busqueda = models.DateTimeField(auto_now_add=True)
    ultima_busqueda = models.DateTimeField(auto_now=True)
    
