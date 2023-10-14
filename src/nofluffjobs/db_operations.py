import mysql.connector
import datetime

todays_date = datetime.datetime.now()
todays_date = str(todays_date.year) + "-" + str(todays_date.month)  + "-" + str(todays_date.day)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="nofluffjobs_db"
)

def insert_data(data_list,start_id_offer):
    connection = mydb.cursor()
    id_offer = start_id_offer
    for data_row in data_list:
        # insert into main table
        sql = "INSERT INTO daily_data (id, company, category, seniority, salary, doswiadczenie, date) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        values = (id_offer, data_row[0], data_row[1], data_row[2], data_row[5], data_row[7], todays_date)
        connection.execute(sql, values)
        mydb.commit()
        # insert to lokacje
        sql = "INSERT INTO daily_lokacje (id, lokacja) VALUES (%s,%s)"
        for lokacja in data_row[6]:
            values = (id_offer, lokacja)
            connection.execute(sql, values)
            mydb.commit()
        # insert to wymagania must
        sql = "INSERT INTO daily_wymagania_must (id, wymaganie) VALUES (%s,%s)"
        for wymaganie in data_row[3]:
            values = (id_offer, wymaganie)
            connection.execute(sql, values)
            mydb.commit()
        # insert to wymagania nice
        sql = "INSERT INTO daily_wymagania_nice (id, wymaganie) VALUES (%s,%s)"
        for wymaganie in data_row[4]:
            values = (id_offer, wymaganie)
            connection.execute(sql, values)
            mydb.commit()  
        id_offer+=1        
    return id_offer

def insert_historic_data():
    connection = mydb.cursor()

    #offers_count
    connection.execute("INSERT INTO historic_count (count, date) SELECT COUNT(id) AS count, '"+str(todays_date)+"' AS date FROM daily_data;")
    mydb.commit()

    #category
    connection.execute("INSERT INTO historic_kategoria (kategoria, count, date) SELECT category, COUNT(*) AS category_count, '"+str(todays_date)+"' AS date FROM `daily_data` GROUP BY category ORDER BY category_count DESC LIMIT 20;")
    mydb.commit()
    
    #lokacje
    connection.execute("INSERT INTO historic_lokacja (lokacja, count, date) SELECT lokacja, COUNT(*) AS location_count, '"+str(todays_date)+"' AS date FROM `daily_lokacje` GROUP BY lokacja ORDER BY location_count DESC LIMIT 20;")
    mydb.commit()
    
    #wymagania_must
    connection.execute("INSERT INTO historic_wymagania_must (wymaganie, count, date) SELECT wymaganie, COUNT(*) AS wymaganie_count, '"+str(todays_date)+"' AS date FROM `daily_wymagania_must` GROUP BY wymaganie ORDER BY wymaganie_count DESC LIMIT 20;")
    mydb.commit()
    
    #wymagania_nice
    connection.execute("INSERT INTO historic_wymagania_nice (wymaganie, count, date) SELECT wymaganie, COUNT(*) AS wymaganie_count, '"+str(todays_date)+"' AS date FROM `daily_wymagania_nice` GROUP BY wymaganie ORDER BY wymaganie_count DESC LIMIT 20;")
    mydb.commit()
    
    # doswiadczenie
    connection.execute("SELECT experience_range, count_in_range FROM (SELECT CASE WHEN doswiadczenie BETWEEN 1 AND 2 THEN '1-2' WHEN doswiadczenie BETWEEN 2 AND 3 THEN '2-3' WHEN doswiadczenie BETWEEN 3 AND 5 THEN '3-5' WHEN doswiadczenie BETWEEN 5 AND 8 THEN '5-8' WHEN doswiadczenie >= 8 THEN '8+' ELSE 'brak_danych' END AS experience_range, COUNT(*) AS count_in_range FROM daily_data GROUP BY experience_range) AS subquery ORDER BY experience_range;")
    count_doswiadczenie = connection.fetchall()
    for datarow in count_doswiadczenie:
        values = (datarow[0], datarow[1], todays_date)
        sql = "INSERT INTO historic_doswiadczenie (experience_range, count_in_range, date) VALUES (%s, %s, %s)"
        connection.execute(sql, values)
        mydb.commit()

    # salary
    connection.execute("SELECT salary_range, count_in_range FROM (SELECT CASE WHEN salary BETWEEN 1 AND 4000 THEN '1-4000' WHEN salary BETWEEN 4000 AND 6000 THEN '4000-6000' WHEN salary BETWEEN 6000 AND 10000 THEN '6000-10000' WHEN salary BETWEEN 10000 AND 15000 THEN '10000-15000' WHEN salary BETWEEN 15000 AND 20000 THEN '15000-20000' WHEN salary >= 20000 THEN '20000+' ELSE 'Unknown' END AS salary_range, COUNT(*) AS count_in_range FROM daily_data GROUP BY salary_range) AS subquery ORDER BY salary_range;")
    count_salary = connection.fetchall()
    for datarow in count_salary:
        values = (datarow[0], datarow[1], todays_date)
        sql = "INSERT INTO historic_salary (salary_range, count_in_range, date) VALUES (%s, %s, %s)"
        connection.execute(sql, values)
        mydb.commit()

    #seniority
    connection.execute("SELECT seniority, COUNT(*) AS seniority_count FROM daily_data GROUP BY seniority;")
    seniority_querry = connection.fetchone()
    for data in seniority_querry:
        values = (data[0], data[1], todays_date)
        sql = "INSERT INTO historic_seniority (seniority, count, date) VALUES (%s,%s,%s)"
        connection.execute(sql, values)
        mydb.commit()
    
        
def clear_tables():
    connection = mydb.cursor()
    tables_to_clear = [
        "daily_data",
        "daily_lokacje",
        "daily_wymagania_must",
        "daily_wymagania_nice"]
    for table in tables_to_clear:
        sql = f"DELETE FROM {table};"
        connection.execute(sql)
    mydb.commit()