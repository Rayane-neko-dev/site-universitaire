from django.db import models
from Faculties.models import Faculty
from multiselectfield import MultiSelectField

FORMATIONS_DISPO = (
    ('M', 'Master'),
    ('L', 'Licence'),
    ('LP', 'Licence Pro'),
    ('SC', 'Système classique'),
)

class Departement(models.Model):
    departement_id = models.IntegerField()
    image = models.ImageField(upload_to='images/departement', null=True, blank=True)
    titre = models.CharField(max_length=100)
    contenu = models.CharField(max_length=1000)
    faculty = models.ForeignKey(
        'Faculties.Faculty',
        on_delete=models.CASCADE,
        related_name='departements',
        null=True,
        blank=True
    )
    formation_dispo = MultiSelectField(
        choices=FORMATIONS_DISPO,
        default=[choix[0] for choix in FORMATIONS_DISPO],
        max_choices=len(FORMATIONS_DISPO),
        blank=True,
    )

    def __str__(self):
        return self.titre
