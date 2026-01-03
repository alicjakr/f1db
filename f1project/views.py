from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *
from django.template import loader
#class name

def main_page(request):
    return render(request, 'main.html')

def display_drivers(request):
    drivers_records=Drivers.objects.all().order_by('-current_points')
    return render(request,'displayDrivers.html',{'records':drivers_records})

def display_teams(request):
    teams_records=Teams.objects.all().order_by('-constructor_points')
    return render(request, 'displayTeams.html', {'records':teams_records})

def display_races(request):
    races_records=Races.objects.all()
    return render(request, 'displayRaces.html', {'records':races_records})

def display_fastest_lap_times(request):
    fastest_lap_times_records=FastestLapTimes.objects.select_related('driver_number', 'gp_name').all().order_by('gp_name__round_number')
    return render(request, 'displayFastestLapTimes.html', {'records':fastest_lap_times_records})

def display_race_results(request):
    race_results_records=RaceResults.objects.all()
    return render(request, 'displayRaceResults.html', {'records':race_results_records})

def add_driver(request):
    template = loader.get_template('adddriver.html')
    return HttpResponse(template.render({}, request))

def add_driver_record(request):
    r_number=request.POST['number']
    r_first = request.POST['first']
    r_last = request.POST['last']
    r_team=request.POST['team']
    r_currentpoints=request.POST['currentpoints']

    driver=Drivers(number=r_number, name=r_first, surname=r_last, team=r_team, current_points=r_currentpoints)
    driver.save()
    return HttpResponseRedirect(reverse('drivers'))

def add_team(request):
    template = loader.get_template('addteam.html')
    return HttpResponse(template.render({}, request))

def add_team_record(request):
    r_team=request.POST['team']
    r_engine = request.POST['engine']
    r_location = request.POST['location']
    r_cp=request.POST['cpoints']
    r_gppoints=request.POST['gppoints']
    r_gpwins=request.POST['gpwins']
    r_gppoles=request.POST['gppoles']
    r_sprintpoints=request.POST['sprintpoints']
    r_sprintwins=request.POST['sprintwins']
    r_sprintpoles=request.POST['sprintwins']

    team=Teams(team=r_team, engine_supplier=r_engine, location=r_location, constructor_points=r_cp, gp_points=r_gppoints, gp_wins=r_gpwins, gp_poles=r_gppoles, sprint_points=r_sprintpoints, sprint_wins=r_sprintwins, sprint_poles=r_sprintpoles)
    team.save()
    return HttpResponseRedirect(reverse('teams'))

def drivers_fastest_lap(request):
    #display: NUMBER - NAME - SURNAME - TEAM - COUNT OF FASTEST LAPS
    #use table FastestLapTimes
    fieldname="Number"
    return render(request, 'displayDriversFastestLap.html', {'records':FastestLapTimes.objects.values(fieldname).order_by(fieldname).annotate(the_count=Count(fieldname))})