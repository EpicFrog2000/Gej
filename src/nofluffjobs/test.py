import mysql.connector
import datetime

todays_date = datetime.datetime.now()
todays_date = str(todays_date.year) + "-" + str(todays_date.month)  + "-" + str(todays_date.day)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="nofluffjobs_db"
)
    
connection = mydb.cursor()
# doswiadczenie
connection.execute("SELECT experience_range, count_in_range FROM (SELECT CASE WHEN doswiadczenie BETWEEN 1 AND 2 THEN '1-2' WHEN doswiadczenie BETWEEN 2 AND 3 THEN '2-3' WHEN doswiadczenie BETWEEN 3 AND 5 THEN '3-5' WHEN doswiadczenie BETWEEN 5 AND 8 THEN '5-8' WHEN doswiadczenie >= 8 THEN '8+' ELSE 'brak_danych' END AS experience_range, COUNT(*) AS count_in_range FROM daily_data GROUP BY experience_range) AS subquery ORDER BY experience_range;")
count_doswiadczenie = connection.fetchall()
print(count_doswiadczenie)
for datarow in count_doswiadczenie:
    values = (datarow[0], datarow[1], todays_date)
    print(values)
    sql = "INSERT INTO historic_doswiadczenie (experience_range, count_in_range, date) VALUES (%s, %s, %s)"
    connection.execute(sql, values)
    mydb.commit()
