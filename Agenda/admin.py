from django.contrib import admin

from Agenda.models import Evenement

class AgendaAdmin(admin.ModelAdmin):

 list_display = ('titre','date','image') 

admin.site.register(Evenement, AgendaAdmin)