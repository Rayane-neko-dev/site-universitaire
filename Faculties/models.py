from django.db import models

# listings/models.py

class Faculty(models.Model):
    fac_id = models.fields.IntegerField()
    image =models.ImageField(upload_to='images/fac', null=True, blank=True)
    nom = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    adresse = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
     return f'{self.nom}'