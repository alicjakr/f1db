import psycopg2

conn=psycopg2.connect(database="template1",
                      host="localhost",
                      user="alicjakrupczynska",
                      password="",
                      port="5432")

cursor=conn.cursor()
cursor.execute(open("f1sql.sql", "r").read())
conn.commit()

cursor.execute("SELECT * FROM drivers ORDER BY drivers.current_points DESC")
print("Drivers")
rows=cursor.fetchall()
for row in rows:
    number, name, surname, team, current_points = row
    print(f"{number}, {name}, {surname}, {team}, {current_points}")

cursor.execute("SELECT * FROM team_specifications ORDER BY team_specifications.constructor_points DESC")
print("Team specifications")
rows=cursor.fetchall()
for row in rows:
    team, engine_supplier, location, constructor_points, GP_points, GP_wins, GP_poles, sprint_points, sprint_wins, sprint_poles = row
    print(f"{team}, {engine_supplier}, {location}, {constructor_points}, {GP_points}, {GP_wins}, {GP_poles}, {sprint_points}, {sprint_wins}, {sprint_poles}")

cursor.execute("SELECT * FROM races")
rows=cursor.fetchall()
print("Races")
for row in rows:
    round_number, GP_name, GP_fullname, start_date, end_date, distance, circuit_length, laps_number = row
    formatted_start_date=start_date.strftime("%Y-%m-%d")
    formatted_end_date=end_date.strftime("%Y-%m-%d")
    print(f"{round_number}, {GP_name}, {GP_fullname}, {formatted_start_date}, {formatted_end_date}, {distance}, {circuit_length}, {laps_number}")

cursor.execute("SELECT * FROM fastest_lap_times")
print("Fastest lap times")
rows=cursor.fetchall()
for row in rows:
    track_name, GP_name, driver_number, driver_name, driver_surname, team, lap_time = row
    minutes=lap_time.minute
    seconds=lap_time.second
    milliseconds=int(lap_time.microsecond / 1000)
    formatted_time=f"{minutes}:{seconds}.{milliseconds}"
    print(f"{track_name}, {GP_name}, {driver_number}, {driver_name}, {driver_surname}, {team}, {formatted_time}")

cursor.execute("SELECT * FROM race_results")
print("Race results")
rows=cursor.fetchall()
for row in rows:
    GP_name, race_date, winner_number, winner_name, winner_surname, team, laps_number, race_time = row
    formatted_date=race_date.strftime("%Y-%m-%d")
    hours=race_time.hour
    minutes=race_time.minute
    seconds=race_time.second
    milliseconds=int(race_time.microsecond / 1000)
    formatted_time=f"{hours}:{minutes}:{seconds}.{milliseconds}"
    print(f"{GP_name}, {formatted_date}, {winner_number}, {winner_name}, {winner_surname}, {team}, {laps_number}, {formatted_time}")

cursor.close()
conn.close()