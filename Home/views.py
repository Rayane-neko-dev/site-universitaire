from django.shortcuts import render, redirect
from Actuality.models import Actuality
from Agenda.models import Evenement
from .forms import SubscriberForm

def Home(request):
    actus = Actuality.objects.all()
    events = Evenement.objects.all()
    form = SubscriberForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')  # ou affiche un message de succès si tu veux

    context = {
        'actus': actus,
        'events': events,
        'form': form,
    }
    return render(request, 'Home/home.html', context)
