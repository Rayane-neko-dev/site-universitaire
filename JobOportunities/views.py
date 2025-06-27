from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Job

def job_view(request):
    jobs = Job.objects.all()
    return render(request, 'JobOportunities/job.html' ,{'jobs':jobs})


