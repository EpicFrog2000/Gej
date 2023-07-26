import mysql.connector

def insert_data(data_list):
    def connect():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="test_data_job_market"
        )
        return mydb

    with connect() as mydb:
        connection = mydb.cursor()
        sql = "INSERT INTO data (title, company, location, management_level, salary, tryb_pracy, etat, kontrakt, specjalizacja) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        connection.executemany(sql, data_list)
        mydb.commit()