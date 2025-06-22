# Register your models here.

from django.contrib import admin

from Departments.models import Departement

class DepartementAdmin(admin.ModelAdmin):

 list_display = ('titre','contenu','image') 

admin.site.register(Departement, DepartementAdmin)