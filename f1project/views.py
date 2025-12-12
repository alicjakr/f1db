from django.shortcuts import render
from .models import *
#class name

def main_page(request):
    return render(request, 'main.html')

def display_drivers(request):
    drivers_records=Drivers.objects.all()
    return render(request,'displayDrivers.html',{'records':drivers_records})

def display_teams(request):
    teams_records=Teams.objects.all()
    return render(request, 'displayTeams.html', {'records':teams_records})

def display_races(request):
    races_records=Races.objects.all()
    return render(request, 'displayRaces.html', {'records':races_records})

def display_fastest_lap_times(request):
    fastest_lap_times_records=FastestLapTimes.objects.all()
    return render(request, 'displayFastestLapTimes.html', {'records':fastest_lap_times_records})

def display_race_results(request):
    race_results_records=RaceResults.objects.all()
    return render(request, 'displayRaceResults.html', {'records':race_results_records})