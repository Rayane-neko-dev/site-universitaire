from django.db import models
from Faculties.models import Faculty

# Create your models here.

class Job(models.Model):
    job_id = models.fields.IntegerField()
    image =models.ImageField(upload_to='images/fac', null=True, blank=True)
    intitule_poste = models.fields.CharField(max_length=100)
    prerequis_recrutement = models.fields.CharField(max_length=1000 , null=True, blank=True)
    details = models.fields.CharField(max_length=200 , null=True, blank=True)
    faculte_rattachement = models.ForeignKey(
    Faculty,
    on_delete=models.CASCADE,
    related_name='job',
    null=True,
    blank=True
)
    def __str__(self):
     return f'{self.intitule_poste}'