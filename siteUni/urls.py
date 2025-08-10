"""
URL configuration for siteUni project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Home import views as home_views
from Actuality.views import actuality_view
from Actuality.views import actuality_detailed_view
from Faculties.views import Faculties_view
from Faculties.views import faculty_detail
from Formations.views import formation_detail
from Agenda import views as agenda_views
from django.conf import settings
from django.conf.urls.static import static
from Departments.views import departement_view
from Bourse.views import bourse_view
from JobOportunities.views import job_view
from Annuaire.views import Annuaire_view
from Departments.views import departement_detailed_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/', home_views.Home, name='home'),
    path('', home_views.Home, name='home'),
    path('Agenda/', agenda_views.Agenda, name='agenda'),
    path('actus/', actuality_view, name='actuality'),
    path('actus/<int:actualite_id>/', actuality_detailed_view, name='actuality_detail'),
    path('Faculties/', Faculties_view, name='faculties'),
    path('deps/', departement_view, name='departement'),
    path('Faculties/<int:faculty_id>/', faculty_detail, name='faculty_detail'),
    path('Formation/<int:formation_id>/', formation_detail, name='formation_detail'),  
    path('bourse/', bourse_view, name='bourse'),
    path('job/', job_view, name='job'),
    path('annuaire/', Annuaire_view, name='annuaire'),
    path('Faculties/<int:faculty_id>/<int:departement_id>/', departement_detailed_view, name='departement_detailed'),
    path(
    'Faculties/<int:faculty_id>/<int:departement_id>/<int:formation_id>/',
    formation_detail,
    name='formation_detail'
)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)