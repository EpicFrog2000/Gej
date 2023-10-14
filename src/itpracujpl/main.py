

import db_operations
import bot_class_itpracujpl
import os
numer_stron_sesji = 0
id_offer = 1

# czyści dane aby przygotowac na pierwsze działanie programu
db_operations.clear_tables()
# Zrobione jest to po to aby upewnić się że mój świetny internet kiedyś w końcu załapie że próbuję używać przeglądarki i zacznie ładować elementy na stronie www
while numer_stron_sesji == 0:
    bot = bot_class_itpracujpl.Bot()
    bot.kliknij_przycisk_ciasteczka()
    numer_stron_sesji = bot.get_all_sites_nums()
    
#TODO Podziel program aby działał na większej ilości wątków w zależności od tego na jakim serwerze zostawie te skrypty
#     tzn. strony od 1-10 na jednym wątku 11-20 na drugim wątku itd.
while int(bot.obecna_strona) <= int(numer_stron_sesji):
    bot.get_data(numer_stron_sesji)
    formatted_list = []
    unique_items = set()
    for temp_list in bot.dane_oferty:
        formatted_item = (
            temp_list[0],#  title
            temp_list[1],#  company
            temp_list[2],#  location
            temp_list[3],#  management_level
            temp_list[4],#  salary
            temp_list[5],#  tryb_pracy
            temp_list[6],#  etat
            temp_list[7],#  kontrakt
            temp_list[8],#  specjalizacja
            tuple(temp_list[9]),# technologie_wymagane (converted to a tuple)
            tuple(temp_list[10]),# technologie_mile_widziane (converted to a tuple)
            temp_list[11],# doswiadczenie
        )
        if formatted_item not in unique_items:
            formatted_list.append(formatted_item)
            unique_items.add(formatted_item)
            
    # insertuje dane do bazy danych co 1 stronę żeby na wszelki wypadek końcowe zapytanie nie było za duże
    id_offer = db_operations.insert_data(formatted_list, id_offer)
    os.system('cls')
    print(f"\rProgres: {bot.obecna_strona} / {numer_stron_sesji}")
    bot.go_to_next_site()
# Magazynuje odpowiednie dane do tabelek jako historyczne dane
db_operations.insert_to_historic_data()