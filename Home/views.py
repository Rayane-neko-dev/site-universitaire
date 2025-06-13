from django.http import HttpResponse
from Actuality.models import Actuality
from Agenda.models import Evenement
from django.shortcuts import render, get_object_or_404

def Home(request):
    actus = Actuality.objects.all()
    events = Evenement.objects.all()
    return render(request, 'Home/home.html', {'actus': actus, 'events':events})
