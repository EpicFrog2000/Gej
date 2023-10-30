import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="indeed_db"
)

class indeed_db_interaction:
    connection = mydb.cursor()
    @staticmethod
    def last_date(connection=connection):
        sql = "SELECT MAX(date) FROM menu_data;"
        connection.execute(sql)
        result = connection.fetchone()[0]
        return result
    @staticmethod
    def count_all(connection=connection):
        sql = "SELECT ilosc FROM menu_data ORDER BY date DESC LIMIT 1;"
        connection.execute(sql)
        result = connection.fetchone()[0]
        return result

    @staticmethod
    def wynagrodzenie_data(connection=connection):
        sql = "SELECT nazwa, ilosc FROM wynagrodzenie_data WHERE date = (SELECT MAX(date) FROM wynagrodzenie_data);;"
        connection.execute(sql)
        result = connection.fetchall()
        wynagrodzenie_data = [{
            "nazwa": f"{int(row[0]) // 100}.{int(row[0]) % 100:02} pln",
            "ilosc": row[1],
        } for row in result]
        return wynagrodzenie_data
    
    @staticmethod
    def jezyk_data(connection=connection):
        sql = "SELECT english, polish FROM menu_data ORDER BY date DESC LIMIT 1;"
        connection.execute(sql)
        result = connection.fetchone()
        jezyk_data = {
            "english": result[0],
            "polish": result[1],
        }
        return jezyk_data
    
    @staticmethod
    def tryb_data(connection=connection):
        sql = "SELECT tryb_hybrydowo, tryb_zdalnie FROM menu_data ORDER BY date DESC LIMIT 1;"
        connection.execute(sql)
        result = connection.fetchone()
        tryb_data = {
            "tryb_hybrydowo": result[0],
            "tryb_zdalnie": result[1],
        }
        return tryb_data
    
    @staticmethod
    def wymiar_data(connection=connection):
        sql = "SELECT `pelny_etat`, `stala`, `podwykonawstwo`, `Staz/praktyka`, `tymczasowa`, `częsc_etatu`, `wolontariat` FROM menu_data ORDER BY date DESC LIMIT 1;"
        connection.execute(sql)
        result = connection.fetchone()
        wymiar_data = {
            "Pełny etat": result[0],
            "Stała": result[1],
            "Podwykonawstwo": result[2],
            "Staż/Praktyka": result[3],
            "Tymczasowa": result[4],
            "Część etatu": result[5],
            "Wolontariat": result[6],
        }
        return wymiar_data
    
    @staticmethod
    def wykrztalcenie_data(connection=connection):
        sql = "SELECT `licencjat`, `magister`, `inzynier`, `srednie`, `srednie_techniczne/branzowe`, `Doktor`, `zasadnicze_zawodowe/branzowe`, `podstawowe` FROM menu_data ORDER BY date DESC LIMIT 1;"
        connection.execute(sql)
        result = connection.fetchone()
        wykrztalcenie_data = {
            "Licencjat": result[0],
            "Magister": result[1],
            "Inżynier": result[2],
            "Średnie": result[3],
            "Średnie techniczne/branżowe": result[4],
            "Doktor": result[5],
            "Zasadnicze zawodowe/branżowe": result[6],
            "Podstawowe": result[7],
        }
        return wykrztalcenie_data
    
    @staticmethod
    def lokalizacja_data(connection=connection):
        sql = "SELECT nazwa, ilosc FROM lokalizacja_data WHERE nazwa IS NOT NULL AND nazwa != '' AND date = (SELECT MAX(date) FROM lokalizacja_data) GROUP BY nazwa ORDER BY COUNT(*) DESC LIMIT 20;;"
        connection.execute(sql)
        result = connection.fetchall()
        lokalizacja_data = [{
            "lokalizacja": row[0],
            "ilosc": row[1],
        } for row in result]
        return lokalizacja_data
    
    @staticmethod
    def firmy_data(connection=connection):
        sql = "SELECT nazwa, ilosc FROM firmy_data WHERE nazwa IS NOT NULL AND nazwa != '' AND date = (SELECT MAX(date) FROM firmy_data) GROUP BY nazwa ORDER BY COUNT(*) DESC LIMIT 20;"
        connection.execute(sql)
        result = connection.fetchall()
        firmy_data = [{
            "firma": row[0],
            "ilosc": row[1],
            }for row in result]
        return firmy_data
    
    #historic
    @staticmethod
    def get_historic_count_data(connection=connection):
        sql = "SELECT date, ilosc FROM menu_data ORDER BY date ASC;"
        connection.execute(sql)
        result = connection.fetchall()
        data_for_chart = [{"date": entry[0].strftime("%Y-%m-%d"), "count": entry[1]} for entry in result]
        return data_for_chart
    
    @staticmethod
    def get_historic_salary_data(connection=connection):
        sql = "SELECT nazwa, ilosc, `date` FROM wynagrodzenie_data ORDER BY date ASC;"
        connection.execute(sql)
        result = connection.fetchall()
        wynagrodzenie_data = [{
            "nazwa": f"{int(entry[0]) // 100}.{int(entry[0]) % 100:02} pln",
            "ilosc": entry[1],
            "date": entry[2].strftime("%Y-%m-%d"),
        }for entry in result]
        return wynagrodzenie_data
    
    @staticmethod
    def get_historic_jezyk_data(connection=connection):
        sql = "SELECT english, polish, date FROM menu_data ORDER BY date ASC;"
        connection.execute(sql)
        result = connection.fetchall()
        jezyk_data = [{
            "english": entry[0],
            "polish": entry[1],
            "date": entry[2].strftime("%Y-%m-%d"),
        } for entry in result]
        return jezyk_data
    
    @staticmethod
    def get_historic_tryb_data(connection=connection):
        sql = "SELECT tryb_hybrydowo, tryb_zdalnie, date FROM menu_data ORDER BY date ASC;"
        connection.execute(sql)
        result = connection.fetchall()
        tryb_data = [{
            "tryb_hybrydowo": entry[0],
            "tryb_zdalnie": entry[1],
            "date": entry[2].strftime("%Y-%m-%d"),
        }for entry in result]
        return tryb_data
    
    @staticmethod
    def get_historic_wymiar_data(connection=connection):
        sql = "SELECT `pelny_etat`, `stala`, `podwykonawstwo`, `Staz/praktyka`, `tymczasowa`, `częsc_etatu`, `wolontariat`, `date` FROM menu_data ORDER BY date ASC;"
        connection.execute(sql)
        result = connection.fetchall()
        wymiar_data = [{
            "Pełny etat": res[0],
            "Stała": res[1],
            "Podwykonawstwo": res[2],
            "Staż/Praktyka": res[3],
            "Tymczasowa": res[4],
            "Część etatu": res[5],
            "Wolontariat": res[6],
            "date": res[7].strftime("%Y-%m-%d"),
        }for res in result]
        return wymiar_data

    @staticmethod
    def get_historic_wykrztalcenie_data(connection=connection):
        sql = "SELECT `licencjat`, `magister`, `inzynier`, `srednie`, `srednie_techniczne/branzowe`, `Doktor`, `zasadnicze_zawodowe/branzowe`, `podstawowe`, `date` FROM menu_data ORDER BY date ASC;"
        connection.execute(sql)
        result = connection.fetchall()
        wykrztalcenie_data = [{
            "Licencjat": res[0],
            "Magister": res[1],
            "Inżynier": res[2],
            "Średnie": res[3],
            "Średnie techniczne/branżowe": res[4],
            "Doktor": res[5],
            "Zasadnicze zawodowe/branżowe": res[6],
            "Podstawowe": res[7],
            "date": res[8].strftime("%Y-%m-%d"),
        }for res in result]
        return wykrztalcenie_data
    
    @staticmethod
    def get_historic_firmy_data(connection=connection):
        sql = "SELECT nazwa, ilosc, date FROM firmy_data WHERE nazwa IS NOT NULL AND nazwa != '' ORDER BY date ASC;"
        connection.execute(sql)
        result = connection.fetchall()
        firmy_data = [{
            "firma": row[0],
            "ilosc": row[1],
            "date": row[2].strftime("%Y-%m-%d"),
            }for row in result]
        return firmy_data
    
    @staticmethod
    def get_historic_lokalizacja_data(connection=connection):
        sql = "SELECT nazwa, ilosc, date FROM lokalizacja_data WHERE nazwa IS NOT NULL AND nazwa != '' ORDER BY date ASC;"
        connection.execute(sql)
        result = connection.fetchall()
        lokalizacja_data = [{
            "lokalizacja": row[0],
            "ilosc": row[1],
            "date": row[2].strftime("%Y-%m-%d"),
        } for row in result]
        return lokalizacja_data