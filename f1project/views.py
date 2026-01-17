from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.postgres.aggregates import StringAgg
from .models import *
from django.template import loader

def main_page(request):
    return render(request, 'main.html')

def display_drivers(request):
    drivers_records=Drivers.objects.select_related('team').all().order_by('-current_points')
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
    r_sprintpoles=request.POST['sprintpoles']

    team=Teams(team=r_team, engine_supplier=r_engine, location=r_location, constructor_points=r_cp, gp_points=r_gppoints, gp_wins=r_gpwins, gp_poles=r_gppoles, sprint_points=r_sprintpoints, sprint_wins=r_sprintwins, sprint_poles=r_sprintpoles)
    team.save()
    return HttpResponseRedirect(reverse('teams'))

def driversfastestlap(request):
    records=FastestLapTimes.objects.values('driver_number__number', 'driver_number__name', 'driver_number__surname', 'driver_number__team').annotate(the_count=Count("driver_number")).order_by('-the_count')
    return render(request, 'displayDriversFastestLap.html', {'records':records})

def driverwins(request):
    wins_records=RaceResults.objects.values('winner_number__number', 'winner_number__name', 'winner_number__surname', 'winner_number__team').annotate(win_count=Count("winner_number__number"), countries=StringAgg('gp_name__gp_name', delimiter=', ', distinct=True)).order_by('-win_count')
    return render(request, 'displayDriverWins.html', {'records':wins_records})