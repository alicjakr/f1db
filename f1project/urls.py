"""
URL configuration for f1project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

from f1project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drivers/', views.display_drivers, name='drivers'),
    path('teams/', views.display_teams, name='teams'),
    path('races/', views.display_races, name='races'),
    path('fastestlaptimes/', views.display_fastest_lap_times, name='fastestlaptimes'),
    path('raceresults/', views.display_race_results, name='raceresults'),
    path('adddriver/', views.add_driver, name='adddriver'),
    path('adddriver/addrecord/', views.add_driver_record, name='adddriver_record'),
    path('addteam/', views.add_team, name='addteam'),
    path('addteam/addrecord/', views.add_team_record, name='addteam_record'),
    path('', views.main_page, name='main'),
]

'''
    path('adddriver/', views.add_a_driver, name='adddriver'),
    path('addteam/', views.add_a_team, name='addteam'),'''
