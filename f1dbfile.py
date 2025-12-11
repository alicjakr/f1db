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

def flts_table():
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

def add_new_driver():
    print("Adding new driver")
    driver_number=input("Driver's number: ")
    #add if statement to check if a driver with given number already exists
    driver_name=input("Driver's name: ")
    driver_surname=input("Driver's surname: ")
    driver_team=input("Driver's team: ")
    current_pts=input("Driver's current points: ")
    cursor.execute("INSERT INTO drivers VALUES (%s)", (driver_number, driver_name, driver_surname, driver_team, current_pts))

def add_new_race():
    print("Adding new race")
    #round number should be automatic
    rGP_name=input("Race's GP name: ")
    rGP_fullname=input("Race's GP name: ")
    rstart_date=input("Race's start date: ")
    rend_date=input("Race's end date: ")
    rdistance=float(input("Race's distance: "))
    rcircuit_length=float(input("Race's circuit: "))
    rlaps=int(input("Race's laps number: "))
    cursor.execute("INSERT INTO races VALUES (%s)", (rGP_name, rGP_fullname, rstart_date, rend_date, rdistance, rcircuit_length, rlaps))

def add_new_team():
    print("Adding new team")
    team_name=input("Team's name: ")
    team_es=input("Team's engine supplier: ")
    team_loc=input("Team's location: ")
    team_cp=int(input("Team's constructor points: "))
    team_GPpts=int(input("Team's Grand Prix points: "))
    team_GPwins=int(input("Team's GP wins: "))
    team_GPpoles=int(input("Team's GP poles: "))
    team_sprintpts=int(input("Team's sprint points: "))
    team_sprintwins=int(input("Team's sprint wins:"))
    team_sprintpoles=int(input("Team's sprint poles:"))
    cursor.execute("INSERT INTO team_specifications VALUES (%s)", (team_name, team_es, team_loc, team_cp, team_GPpts, team_GPwins, team_GPpoles, team_sprintpts, team_sprintwins, team_sprintpoles))


def add_new_flt():
    #only if new race was added
    print("Adding new fastest lap time")
    tname=input("Track's name: ")
    GPname=input("Grand Prix's name: ")
    drivers_number=input("Driver's number: ")
    drivers_name=input("Driver's name: ")
    drivers_surname=input("Driver's surname: ")
    drivers_team=input("Driver's team: ")
    drivers_lap_time=input("Driver's lap time: ")
    cursor.execute("INSERT INTO add_new_flt VALUES (%s)", (tname, GPname, drivers_number, drivers_name, drivers_surname, drivers_team, drivers_lap_time))

def add_new_rr():
    #only if new race was added
    print("Adding new race result")
    GPname=input("Grand Prix's name: ")
    racedate=input("Race's date: ")
    winners_num=int(input("Winner's number: "))
    winners_name=input("Winner's name: ")
    winners_surname=input("Winner's surname: ")
    winners_team=input("Winner's team: ")
    laps_num=int(input("Laps number: "))
    racetime=input("Race's time: ")
    cursor.execute("INSERT INTO race_results VALUES (%s)", (GPname, racedate, winners_num, winners_name, winners_surname, winners_team, laps_num, racetime))


#user interface
if __name__ == '__main__':
    print("F1 2025 database")
    print("Please choose desired option: \n 1. Drivers table \n 2. Teams table \n 3. Races table \n 4. Fastest lap time table \n 5. Race results table \n"
          " 6. Add a new driver \n 7. Add a new team \n 8. Add a new race \n 9. Add a new fastest lap time \n 10. Add a new race result \n")
    chosen_option=int(input())
    match chosen_option:
        case 1:
            drivers_table()
        case 2:
            teams_table()
        case 3:
            races_table()
        case 4:
            flts_table()
        case 5:
            rr_table()
        case 6:
            add_new_driver()
        case 7:
            add_new_team()
        case 8:
            add_new_race()
        case 9:
            add_new_flt()
        case 10:
            add_new_rr()
        case _:
            print("Please choose a valid option")

cursor.close()
conn.close()