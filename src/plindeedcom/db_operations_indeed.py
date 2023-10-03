import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="test_data_job_market"
)

def insert_data(data_list):
    todays_date = datetime.datetime.now()
    todays_date = str(todays_date.year) + "-" + str(todays_date.month)  + "-" + str(todays_date.day)

    connection = mydb.cursor()
    sql = "INSERT INTO `indeed_data_daily`(`tryb_hybrydowo`, `tryb_zdalnie`, `wynagrodzenie_1666,67`, `wynagrodzenie_5000,00`, `wynagrodzenie_6666,67`, `wynagrodzenie_10833,33`, `wynagrodzenie_20833,33`, `pelny_etat`, `stala`, `podwykonawstwo`, `staz/praktyka`, `tymczasowa`, `częsc_etatu`, `wolontariat`, `licencjat`, `magister`, `inzynier`, `srednie`, `srednie_techniczne/branzowe`, `doktor`, `zasadnicze_zawodowe/branzowe`, `podstawowe`, `english`, `polish`, `date`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (data_list[0], data_list[1], data_list[2], data_list[3], data_list[4],
              data_list[5], data_list[6], data_list[7], data_list[8], data_list[9],
              data_list[10], data_list[11], data_list[12], data_list[13], data_list[14],
              data_list[15], data_list[16], data_list[17], data_list[18], data_list[19],
              data_list[20], data_list[21], data_list[24], data_list[25], todays_date)
    connection.execute(sql, values)
    mydb.commit()
    
    for lokalizacja in data_list[22]:
        sql = "INSERT INTO `indeed_lokalizacja_daily`(`date`, `nazwa`, `ilosc`) VALUES (%s,%s,%s)"
        values = (todays_date, lokalizacja[0], lokalizacja[1])
        connection.execute(sql, values)
    mydb.commit()
    
    for firma in data_list[23]:
        sql = "INSERT INTO `indeed_firmy_daily`(`date`, `nazwa`, `ilosc`) VALUES (%s,%s,%s)"
        values = (todays_date, firma[0], firma[1])
        connection.execute(sql, values)
    mydb.commit()
    
    print("data succesfuly inserted")
    connection.close()
        
def clear_tables():
    connection = mydb.cursor()
    tables_to_clear = [
        "indeed_data_daily",
        "indeed_firmy_daily",
        "indeed_lokalizacja_daily"]
    for table in tables_to_clear:
        sql = f"DELETE FROM {table};"
        connection.execute(sql)
    mydb.commit()
