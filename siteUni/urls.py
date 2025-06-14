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
from Agenda import views as agenda_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/', home_views.Home, name='home'),
    path('Agenda/', agenda_views.Agenda, name='agenda'),
    path('actus/', actuality_view, name='actuality'),
    path('actus/<int:actualite_id>/', actuality_detailed_view, name='actuality_detail'),
     path('Faculties/', Faculties_view, name='faculties'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)