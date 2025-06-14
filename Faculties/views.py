from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Faculty

def Faculties_view(request):
    facs = Faculty.objects.all()
    return render(request, 'Faculties/faculties.html' ,{'facs':facs})
