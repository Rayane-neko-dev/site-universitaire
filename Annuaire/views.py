from django.http import HttpResponse
from .models import Annuaire
from django.shortcuts import render, get_object_or_404

def Annuaire_view(request):
    contacts = Annuaire.objects.all()
    return render(request, 'Annuaire/annuaire.html', 
    {'contacts':contacts} )
