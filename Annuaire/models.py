from django.db import models

# listings/models.py

class Annuaire(models.Model):
    annuaire_id = models.fields.IntegerField()
    nom = models.fields.CharField(max_length=50)
    mobile_1 =models.CharField(max_length=20, blank=True, null=True)
    mobile_2 = models.CharField(max_length=20, blank=True, null=True)
    mobile_3 = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(
        unique=True,
        max_length=254,
        verbose_name='Email address',
        help_text='Enter a valid email address.',
        blank=True
    )

    def __str__(self):
     return f'{self.nom}'