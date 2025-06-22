
from django.contrib import admin

from Bourse.models import Bourse

class BourseAdmin(admin.ModelAdmin):

 list_display = ('titre','date_limite') 

admin.site.register(Bourse, BourseAdmin)