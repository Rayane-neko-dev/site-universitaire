
from django.contrib import admin
from .models import Formation, Speciality, Semester, Course

# Inline pour Course dans Semester
class CourseInline(admin.TabularInline):
    model = Course
    extra = 1  # Nombre de lignes supplémentaires vides dans l'admin

# Inline pour Semester dans Speciality
class SemesterInline(admin.TabularInline):
    model = Semester
    extra = 1

# Inline pour Speciality dans Formation
class SpecialityInline(admin.TabularInline):
    model = Speciality
    extra = 1


@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ('titre', 'departement', 'credits', 'duree', 'niveau_etude', 'langue_enseignement')
    search_fields = ('titre', 'departement__nom')
    inlines = [SpecialityInline]
    fieldsets = (
        ('Informations générales', {
            'fields': ('departement', 'titre', 'credits', 'duree', 'niveau_etude', 'langue_enseignement')
        }),
        ('Capitalisation et Progression', {
            'fields': ('capitalisation', 'progression')
        }),
    )


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ('name', 'formation')
    search_fields = ('name', 'formation__titre')
    inlines = [SemesterInline]


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('semester_number', 'speciality')
    search_fields = ('speciality__name',)
    inlines = [CourseInline]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'semester', 'time_volume')
    search_fields = ('name', 'semester__speciality__name')
