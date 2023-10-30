import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="indeed_db"
)

def insert_data(data_list):
    todays_date = datetime.datetime.now()
    todays_date = str(todays_date.year) + "-" + str(todays_date.month)  + "-" + str(todays_date.day)

    connection = mydb.cursor()
    sql = "INSERT INTO `menu_data`(`tryb_hybrydowo`, `tryb_zdalnie`, `pelny_etat`, `stala`, `podwykonawstwo`, `staz/praktyka`, `tymczasowa`, `częsc_etatu`, `wolontariat`, `licencjat`, `magister`, `inzynier`, `srednie`, `srednie_techniczne/branzowe`, `doktor`, `zasadnicze_zawodowe/branzowe`, `podstawowe`, `english`, `polish`, `date`, `ilosc`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (data_list[0], data_list[1], data_list[3], data_list[4],
              data_list[5], data_list[6], data_list[7], data_list[8], data_list[9],
              data_list[10], data_list[11], data_list[12], data_list[13], data_list[14],
              data_list[15], data_list[16], data_list[17], data_list[20], data_list[21], todays_date, data_list[22])
    connection.execute(sql, values)
    mydb.commit()
    
    for lokalizacja in data_list[18]:
        sql = "INSERT INTO `lokalizacja_data`(`date`, `nazwa`, `ilosc`) VALUES (%s,%s,%s)"
        values = (todays_date, lokalizacja[0], lokalizacja[1])
        connection.execute(sql, values)
    mydb.commit()
    
    for firma in data_list[19]:
        sql = "INSERT INTO `firmy_data`(`date`, `nazwa`, `ilosc`) VALUES (%s,%s,%s)"
        values = (todays_date, firma[0], firma[1])
        connection.execute(sql, values)
    mydb.commit()
    
    for wynagrodzenie in data_list[2]:
        sql = "INSERT INTO `wynagrodzenie_data`(`date`, `nazwa`, `ilosc`) VALUES (%s,%s,%s)"
        values = (todays_date, wynagrodzenie[0], wynagrodzenie[1])
        connection.execute(sql, values)
    mydb.commit()

    #print("data succesfuly inserted")
    connection.close()
        
def clear_tables():
    connection = mydb.cursor()
    tables_to_clear = [
        "menu_data",
        "firmy_data",
        "lokalizacja_data"]
    for table in tables_to_clear:
        sql = f"DELETE FROM {table};"
        connection.execute(sql)
    mydb.commit()
