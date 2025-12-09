import psycopg2

conn=psycopg2.connect(database="template1",
                      host="localhost",
                      user="alicjakrupczynska",
                      password="",
                      port="5432")

cursor=conn.cursor()
cursor.execute("SELECT * FROM drivers ORDER BY currentpoints DESC")
alldrivers=cursor.fetchall()

for x in alldrivers:
    print(x)

conn.close()