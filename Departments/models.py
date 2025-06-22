from django.db import models
from Faculties.models import Faculty
# Create your models here.

class Departement(models.Model):
    departement_id = models.fields.IntegerField()
    image =models.ImageField(upload_to='images/departement', null=True, blank=True)
    titre = models.fields.CharField(max_length=100)
    contenu = models.fields.CharField(max_length=1000)
    faculty = models.ForeignKey(
    Faculty,
    on_delete=models.CASCADE,
    related_name='departements',
    null=True,
    blank=True
)

    def __str__(self):
     return f'{self.titre}'