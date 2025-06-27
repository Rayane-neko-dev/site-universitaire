from django.contrib import admin

from Annuaire.models import Annuaire

class AnnuaireAdmin(admin.ModelAdmin):

 list_display = ('nom','fax','mobile_1') 

admin.site.register(Annuaire, AnnuaireAdmin)