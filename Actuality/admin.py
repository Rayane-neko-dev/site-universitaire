from django.contrib import admin

from Actuality.models import Actuality

class ActualityAdmin(admin.ModelAdmin):

 list_display = ('titre','date','image') 

admin.site.register(Actuality, ActualityAdmin)