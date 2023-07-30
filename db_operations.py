import mysql.connector
import key_words

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
    return id_offer