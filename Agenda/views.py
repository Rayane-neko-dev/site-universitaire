
from django.http import HttpResponse
from .models import Evenement
from django.shortcuts import render, get_object_or_404

def Agenda(request):
    events = Evenement.objects.all()
    return render(request, 'Agenda/agenda.html', 
    {'events':events} )

