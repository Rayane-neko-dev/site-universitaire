# Register your models here.

from django.contrib import admin

from JobOportunities.models import Job

class JobAdmin(admin.ModelAdmin):

 list_display = ('intitule_poste','faculte_rattachement','image') 

admin.site.register(Job, JobAdmin)