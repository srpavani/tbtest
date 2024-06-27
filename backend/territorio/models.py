from django.db import models
from django.contrib.gis.db import models

class Territorio(models.Model):
    nome = models.CharField(max_length=255)
    coordenadas = models.PolygonField()
    
    def __str__(self):
        return self.nome

class Quadra(models.Model):
    territorio = models.ForeignKey(Territorio, on_delete=models.CASCADE, related_name='quadras')
    grupo = models.CharField(max_length=50)
    coordenadas = models.PolygonField()
    trabalhada = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.grupo} - {self.territorio.nome}'