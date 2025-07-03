from .models import Departement
from django.shortcuts import render, get_object_or_404

# Create your views here.

def departement_view(request):
    deps=Departement.objects.all()
    return render(request, 'Departments/departements.html' ,{'deps':deps})

def departement_detailed_view(request, faculty_id, departement_id):
    deps = get_object_or_404(Departement, departement_id=departement_id, faculty__id=faculty_id)
    return render(request, 'Departments/departement_detail.html', {'deps': deps})
