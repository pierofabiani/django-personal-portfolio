from django.db import models

# Create your models here.


class cvelement(models.Model):
    nome = models.CharField(max_length=20)
    descrizione = models.CharField(max_length=60)
    riassunto = models.CharField(max_length=500)
    start = models.DateField()
    end = models.DateField()
