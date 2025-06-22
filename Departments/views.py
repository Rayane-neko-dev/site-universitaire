from .models import Departement
from django.shortcuts import render, get_object_or_404

# Create your views here.

def departement_view(request):
    deps=Departement.objects.all()
    return render(request, 'Departments/departements.html' ,{'deps':deps})
