from django.db import models

#Creating models
class Drivers(models.Model):
    number=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    team=models.CharField(max_length=100)
    current_points=models.IntegerField()
    class Meta:
        db_table="drivers"

class Teams(models.Model):
    team=models.CharField(max_length=100, primary_key=True)
    engine_supplier=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    constructor_points=models.IntegerField()
    gp_points=models.IntegerField()
    gp_wins=models.IntegerField()
    gp_poles=models.IntegerField()
    sprint_points=models.IntegerField()
    sprint_wins=models.IntegerField()
    sprint_poles=models.IntegerField()
    class Meta:
        db_table="team_specifications"

class Races(models.Model):
    round_number=models.IntegerField(primary_key=True)
    gp_name=models.CharField(max_length=100)
    gp_fullname=models.CharField(max_length=250)
    start_date=models.DateField()
    end_date=models.DateField()
    distance=models.FloatField()
    circuit_length=models.FloatField()
    laps_number=models.IntegerField()
    class Meta:
        db_table="races"

class FastestLapTimes(models.Model):
    track_name=models.CharField(max_length=100, primary_key=True)
    gp_name=models.CharField(max_length=100)
    driver_number=models.IntegerField()
    driver_name=models.CharField(max_length=100)
    driver_surname=models.CharField(max_length=100)
    team=models.CharField(max_length=100)
    lap_time=models.TimeField()
    class Meta:
        db_table="fastest_lap_times"

class RaceResults(models.Model):
    gp_name=models.CharField(max_length=100, primary_key=True)
    race_date=models.DateField()
    winner_number=models.IntegerField()
    winner_name=models.CharField(max_length=100)
    winner_surname=models.CharField(max_length=100)
    team=models.CharField(max_length=100)
    laps_number=models.IntegerField()
    race_time=models.TimeField()
    class Meta:
        db_table="race_results"