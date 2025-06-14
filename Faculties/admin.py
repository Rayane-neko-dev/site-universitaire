from django.contrib import admin

# Register your models here.

from Faculties.models import Faculty

class FacultyAdmin(admin.ModelAdmin):

 list_display = ('nom','description','image') 

admin.site.register(Faculty, FacultyAdmin)