from django.db import models

#Creating models

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

class Drivers(models.Model):
    number=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    team=models.ForeignKey(Teams, on_delete=models.CASCADE, to_field="team", db_column="team")
    current_points=models.IntegerField()
    class Meta:
        db_table="drivers"

class Races(models.Model):
    round_number=models.IntegerField(primary_key=True)
    gp_name=models.CharField(max_length=100, unique=True)
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
    gp_name=models.ForeignKey(Races, on_delete=models.CASCADE, to_field="gp_name", db_column="gp_name")
    driver_number=models.ForeignKey(Drivers, on_delete=models.CASCADE, to_field="number", db_column="driver_number")
    lap_time=models.TimeField()
    class Meta:
        db_table="fastest_lap_times"

class RaceResults(models.Model):
    gp_name=models.ForeignKey(Races, on_delete=models.CASCADE, to_field="gp_name", db_column="gp_name", primary_key=True)
    race_date=models.DateField()
    winner_number=models.ForeignKey(Drivers, on_delete=models.CASCADE, to_field="number", db_column="winner_number")
    laps_number=models.IntegerField()
    race_time=models.TimeField()
    class Meta:
        db_table="race_results"