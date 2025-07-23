
from django.shortcuts import render, get_object_or_404
from .models import Formation

def formation_detail(request, formation_id):
    formation = get_object_or_404(Formation, formation_id=formation_id)
    specialities = formation.specialities.all()
    return render(request, 'Formation/formation_detail.html', {
        'formation': formation,
        'specialities': specialities,
    })