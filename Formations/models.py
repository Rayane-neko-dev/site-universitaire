from django.db import models
from Departments.models import Departement  # import Departement model here


class Formation(models.Model):
    formation_id = models.AutoField(primary_key=True)  # Voilà le fameux ID explicite
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE, related_name='formations')
    titre = models.CharField(max_length=255)
    credits = models.PositiveIntegerField()
    duree = models.CharField(max_length=100)  # e.g., '3 ans'
    niveau_etude = models.CharField(max_length=100)  # e.g., 'BAC +3'
    langue_enseignement = models.CharField(max_length=100)
    capitalisation = models.TextField()
    progression = models.TextField()

    def __str__(self):
        return self.titre


class Speciality(models.Model):
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE, related_name='specialities')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Semester(models.Model):
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name='semesters')
    semester_number = models.PositiveIntegerField()

    def __str__(self):
        return f"Semestre {self.semester_number} - {self.speciality.name}"


class Course(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=255)
    time_volume = models.FloatField(help_text="Volume horaire (heures/crédits)")

    def __str__(self):
        return f"{self.name} ({self.time_volume}h)"
