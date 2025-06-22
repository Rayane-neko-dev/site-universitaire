from django.shortcuts import render
from .models import Bourse

def bourse_view(request):
    bourses = Bourse.objects.all()
    return render(request, 'Bourse/bourse.html', {'bourses': bourses})