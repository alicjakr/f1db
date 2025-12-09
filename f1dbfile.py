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
    print(row)

cursor.execute("SELECT * FROM team_specifications")
print("Team specifications")
rows=cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("SELECT * FROM races")
rows=cursor.fetchall()
print("Races")
for row in rows:
    print(row)

cursor.execute("SELECT * FROM race_results")
print("Race results")
rows=cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("SELECT * FROM fastest_lap_times")
print("Fastest lap times")
rows=cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()