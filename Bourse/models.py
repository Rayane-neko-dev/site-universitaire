from django.db import models

# Create your models here.
from django.db import models

# listings/models.py

class Bourse(models.Model):
    bourse_id = models.fields.IntegerField()
    image =models.ImageField(upload_to='images/bourse', null=True, blank=True)
    titre = models.fields.CharField(max_length=100)
    uploaded_file = models.FileField(upload_to='uploads/')
    date_limite = models.fields.DateField()

    def __str__(self):
     return f'{self.titre}'