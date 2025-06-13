from django.http import HttpResponse
from .models import Actuality
from django.shortcuts import render, get_object_or_404

def actuality_view(request):
    actus = Actuality.objects.all()
    return render(request, 'Actuality/actuality.html', 
    {'actus':actus} )



def actuality_detailed_view(request, actualite_id):
    actualite = get_object_or_404(Actuality, actualite_id=actualite_id)
    return render(request, 'Actuality/actu_detail.html', {'actualite': actualite})