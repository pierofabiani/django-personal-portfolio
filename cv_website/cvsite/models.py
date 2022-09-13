from django.db import models

# Create your models here.


class cvelement(models.Model):
    nome = models.CharField(max_length=20)
    riassunto = models.CharField(max_length=60)
    descrizione = models.CharField(max_length=500)
    start = models.CharField(max_length=10)
    end = models.CharField(max_length=10)

    def __str__(self):
        return self.nome
