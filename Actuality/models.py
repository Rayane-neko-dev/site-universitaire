from django.db import models

# listings/models.py

class Actuality(models.Model):
    actualite_id = models.fields.IntegerField()
    image =models.ImageField(upload_to='images/actuality', null=True, blank=True)
    titre = models.fields.CharField(max_length=100)
    contenu = models.fields.CharField(max_length=1000)
    date = models.fields.DateField()

    def __str__(self):
     return f'{self.titre}'