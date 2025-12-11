import psycopg2
from tabulate import tabulate

conn=psycopg2.connect(database="template1",
                      host="localhost",
                      user="alicjakrupczynska",
                      password="",
                      port="5432")

cursor=conn.cursor()
cursor.execute(open("f1sql.sql", "r").read())
conn.commit()

def drivers_table():
    cursor.execute("SELECT * FROM drivers ORDER BY drivers.current_points DESC")
    print("Drivers")
    driver_rows=cursor.fetchall()
    print(tabulate(driver_rows, headers=["Number", "Name", "Surname", "Team", "Current points"], tablefmt="fancy_grid"))

def teams_table():
    cursor.execute("SELECT * FROM team_specifications ORDER BY team_specifications.constructor_points DESC")
    print("Team specifications")
    team_rows=cursor.fetchall()
    print(tabulate(team_rows, headers=["Team", "Engine supplier", "Location", "Constructor points", "GP points", "GP wins", "GP poles", "Sprint points", "Sprint wins", "Sprint poles"], tablefmt="fancy_grid"))

def races_table():
    cursor.execute("SELECT * FROM races")
    races_rows=cursor.fetchall()
    print("Races")
    print(tabulate(races_rows, headers=["Round number", "GP name", "GP full name", "Start date", "End date", "Distance", "Circuit length", "Laps number"], tablefmt="fancy_grid"))

def flts_table_():
    cursor.execute("SELECT * FROM fastest_lap_times")
    print("Fastest lap times")
    flt_rows=cursor.fetchall()
    frows=[]
    for row in flt_rows:
        track_name, GP_name, driver_number, driver_name, driver_surname, team, lap_time=row
        fminutes=lap_time.minute
        fseconds=lap_time.second
        fmilliseconds=lap_time.microsecond//1000
        flap_time=f"{fminutes:02d}:{fseconds:02d}.{fmilliseconds:03d}"
        frows.append([track_name, GP_name, driver_number, driver_name, driver_surname, team, flap_time])
    print(tabulate(frows, headers=["Track name", "GP name", "Driver's number", "Driver's name", "Driver's surname", "Team", "Time"], tablefmt="fancy_grid"))

def rr_table():
    cursor.execute("SELECT * FROM race_results")
    print("Race results")
    rr_rows=cursor.fetchall()
    frrows=[]
    for row in rr_rows:
        GP_name, race_date, winner_number, winner_name, winner_surname, team, laps_number, race_time = row
        formatted_date=race_date.strftime("%Y-%m-%d")
        rhours=race_time.hour
        rminutes=race_time.minute
        rseconds=race_time.second
        rmilliseconds=race_time.microsecond//1000
        frace_time=f"{rhours:02d}:{rminutes:02d}:{rseconds:02d}.{rmilliseconds:03d}"
        frrows.append([GP_name, race_date, winner_number, winner_name, winner_surname, team, laps_number, frace_time])
    print(tabulate(frrows, headers=["GP name", "Date", "Winner's number", "Winner's name", "Winner's surname", "Team", "Laps' number", "Time"], tablefmt="fancy_grid"))

cursor.close()
conn.close()