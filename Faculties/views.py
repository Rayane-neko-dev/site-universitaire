from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Faculty

def Faculties_view(request):
    facs = Faculty.objects.all()
    return render(request, 'Faculties/faculties.html' ,{'facs':facs})




def faculty_detail(request, faculty_id):
    faculty = get_object_or_404(Faculty, id=faculty_id)
    departments = faculty.departements.all()
    return render(request, 'Departments/departements.html', {
        'deps': departments,
        'faculty': faculty
    })