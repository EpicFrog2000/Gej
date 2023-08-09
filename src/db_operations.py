import mysql.connector
import key_words
import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="test_data_job_market"
)

def translate_and_filter(lista):
    translations = {
        "full-time": "pełny etat",
        "part time": "część etatu",
        "dodatkowa / tymczasowa": "dodatkowa / tymczasowa",
        "expert": "ekspert",
        "assistant": "asystent",
        "director": "dyrektor",
        "manager / supervisor": "kierownik / koordynator",
        "trainee": "praktykant / stażysta",
        "full office work": "praca stacjonarna",
        "hybrid work": "praca hybrydowa",
        "home office work": "praca zdalna",
        "mobile work": "praca mobilna",
        "contract of employment": "umowa o pracę",
        "B2B contract": "kontrakt B2B",
        "contract of mandate": "umowa zlecenie",
        "internship / apprenticeship contract": "umowa o staż / praktyki",
        "temporary staffing agreement": "umowa na zastępstwo",
        "contract for specific work": "umowa o dzieło",
    }
    translated_list = []
    for item in lista:
        if item in translations:
            translated_list.append(translations[item])
        elif item not in translated_list:
            translated_list.append(item)
    return translated_list

def insert_data(data_list,start_id_offer):
    connection = mydb.cursor()
    id_offer = start_id_offer 
    for data_row in data_list:
        #insert into main
        sql = "INSERT INTO data (title, company, location, salary, id, doswiadczenie) VALUES (%s,%s,%s,%s,%s,%s)"
        values = (data_row[0], data_row[1], data_row[2], data_row[4], id_offer, data_row[11])
        connection.execute(sql, values)
        mydb.commit()
        # insert management_level
        lista_management_level = data_row[3].split(",")
        for item in lista_management_level:
            matches = [key for key in key_words.key_words_management_level if key in item]
            matches = translate_and_filter(matches)
            for match in matches:
                sql = "INSERT INTO  management_level (id, management_level) VALUES (%s,%s)"
                values = (id_offer, match)
                connection.execute(sql, values)
                mydb.commit()
        # insert tryb_pracy
        lista_tryb_pracy = data_row[5].split(",")
        for item in lista_tryb_pracy:
            matches = [key for key in key_words.key_words_work_type if key in item]
            matches = translate_and_filter(matches)
            for match in matches:
                sql = "INSERT INTO work_type (id, work_type) VALUES (%s,%s)"
                values = (id_offer, match)
                connection.execute(sql, values)
                mydb.commit()
        # insert etat
        lista_etat = data_row[6].split(",")
        for item in lista_etat:
            matches = [key for key in key_words.key_words_etat if key in item]
            matches = translate_and_filter(matches)
            for match in matches:
                sql = "INSERT INTO etat (id, etat) VALUES (%s,%s)"
                values = (id_offer, match)
                connection.execute(sql, values)
                mydb.commit()
        # insert kontrakt
        lista_kontrakt = data_row[7].split(",")
        for item in lista_kontrakt:
            matches = [key for key in key_words.key_words_kontrakt if key in item]
            matches = translate_and_filter(matches)
            for match in matches:
                sql = "INSERT INTO kontrakt (id, kontrakt) VALUES (%s,%s)"
                values = (id_offer, match)
                connection.execute(sql, values)
                mydb.commit()
        # insert specjalizacje
        lista_specjalizacja = data_row[8].split(",")
        for item in lista_specjalizacja:
            sql = "INSERT INTO specjalizacje (id, specjalizacja) VALUES (%s,%s)"
            values = (id_offer, item)
            connection.execute(sql, values)
            mydb.commit()
        # insert technologie_wymagane
        for item in data_row[9]:
            sql = "INSERT INTO technologie_wymagane (id, technologia) VALUES (%s,%s)"
            values = (id_offer, item)
            connection.execute(sql, values)
            mydb.commit()
        # insert technologie_mile_widziane
        for item in data_row[10]:
            sql = "INSERT INTO technologie_mile_widziane (id, technologia) VALUES (%s,%s)"
            values = (id_offer, item)
            connection.execute(sql, values)
            mydb.commit()
        id_offer += 1
    mydb.commit()
    print("data succesfuly inserted")
    connection.close()
    return id_offer

def insert_to_historic_data():
    connection = mydb.cursor()
    todays_date = datetime.datetime.now()
    todays_date = str(todays_date.year) + "-" + str(todays_date.month)  + "-" + str(todays_date.day)

    connection.execute("SELECT COUNT(id) AS count FROM data;")
    count_of_all_offers = connection.fetchone()
    val = (count_of_all_offers[0], todays_date)
    sql = "INSERT INTO historic_count (count, date) VALUES (%s, %s)"
    connection.execute(sql, val)
    mydb.commit()
    
    connection.execute("SELECT (SUM(CASE WHEN salary > 0 THEN 1 ELSE 0 END) / COUNT(salary)) * 100 AS percentage FROM data;")
    salary_percent = connection.fetchone()
    val = (salary_percent[0], todays_date)
    sql = "INSERT INTO historic_salary (salary, date) VALUES (%s, %s)"
    connection.execute(sql, val)
    mydb.commit()

    connection.execute("SELECT etat, COUNT(id) AS count FROM etat WHERE etat IN ('pełny etat', 'część etatu', 'dodatkowa / tymczasowa') GROUP BY etat ORDER  BY count DESC;")
    etat_data = connection.fetchall()
    val = ()
    for x in etat_data:
        val += (x[1],)
    val += (todays_date, )
    sql = "INSERT INTO `historic_etat`(`pełny etat`, `część etatu`, `dodatkowa / tymczasowa`, `date`) VALUES (%s, %s, %s, %s)"
    connection.execute(sql, val)
    mydb.commit()

        
    connection.execute("SELECT kontrakt, COUNT(id) AS count FROM kontrakt WHERE kontrakt IN ('umowa o pracę', 'kontrakt B2B', 'umowa zlecenie', 'umowa o staż / praktyki', 'umowa o dzieło', 'umowa na zastępstwo') GROUP BY kontrakt ORDER  BY count DESC;")
    kontrakt_data = connection.fetchall()
    val=()
    for x in kontrakt_data:
        val += (x[1],)
    val +=(todays_date,)
    sql = "INSERT INTO `historic_kontrakt`(`umowa o pracę`, `kontrakt B2B`, `umowa zlecenie`, `umowa o staż / praktyki`, `umowa o dzieło`, `umowa na zastępstwo`, `date`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    connection.execute(sql, val)
    mydb.commit()
        
    connection.execute("SELECT management_level, COUNT(id) AS count FROM management_level WHERE management_level IN ('Mid', 'asystent', 'Junior', 'Senior', 'ekspert', 'team manager','menedżer', 'praktykant / stażysta','dyrektor') GROUP BY management_level ORDER  BY count DESC;")
    management_level_data = connection.fetchall()
    val=()
    for x in management_level_data:
        val += (x[1],)
    val +=(todays_date,)
    sql = "INSERT INTO `historic_management_level`(`Mid`, `asystent`, `Junior`, `Senior`, `ekspert`, `team manager`, `menedżer`, `praktykant / stażysta`, `dyrektor`, `date`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    connection.execute(sql, val)
    mydb.commit()
        
    connection.execute("SELECT work_type, COUNT(id) AS count FROM work_type WHERE work_type IN ('praca hybrydowa', 'praca zdalna', 'praca stacjonarna', 'praca mobilna') GROUP BY work_type ORDER  BY count DESC")
    management_level_data = connection.fetchall()
    val=()
    for x in management_level_data:
        val += (x[1],)
    val +=(todays_date,)
    sql = "INSERT INTO `historic_work_type`(`praca hybrydowa`, `praca zdalna`, `praca stacjonarna`, `praca mobilna`, `date`) VALUES (%s, %s, %s, %s, %s)"
    connection.execute(sql, val)
    mydb.commit()
        
    connection.execute("SELECT specjalizacja, COUNT(specjalizacja) AS count FROM specjalizacje WHERE specjalizacja IS NOT NULL AND specjalizacja != '' GROUP BY specjalizacja ORDER BY count DESC;")
    specjalizacja_data = connection.fetchall()
    val=()
    for x in specjalizacja_data:
        sql = "INSERT INTO `historic_specjalizacja`(`specjalizacja`, `count`, `date`) VALUES (%s, %s, %s)"
        val = (x[0],x[1],todays_date,)
        connection.execute(sql, val)
        mydb.commit()
        
    connection.execute("SELECT technologia, COUNT(technologia) AS count FROM technologie_wymagane GROUP BY technologia ORDER BY count DESC;")
    wym_tech_data = connection.fetchall()
    val=()
    for x in wym_tech_data:
        sql = "INSERT INTO `historic_technologie_wymagane`(`technologia`, `count`, `date`) VALUES (%s, %s, %s)"
        val = (x[0],x[1],todays_date,)
        connection.execute(sql, val)
        mydb.commit()
        
    connection.execute("SELECT technologia, COUNT(technologia) AS count FROM technologie_mile_widziane GROUP BY technologia ORDER BY count DESC;")
    wym_tech_data = connection.fetchall()
    val=()
    for x in wym_tech_data:
        sql = "INSERT INTO `historic_technologie_mile_widziane`(`technologia`, `count`, `date`) VALUES (%s, %s, %s)"
        val = (x[0],x[1],todays_date,)
        connection.execute(sql, val)
        mydb.commit()    
        
def clear_tables():
    connection = mydb.cursor()
    tables_to_clear = [
        "data",
        "etat",
        "kontrakt",
        "management_level",
        "specjalizacje",
        "technologie_wymagane",
        "technologie_mile_widziane",
        "work_type"]
    for table in tables_to_clear:
        sql = f"DELETE FROM {table};"
        connection.execute(sql)
    mydb.commit()
