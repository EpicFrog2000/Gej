

import db_operations
import bot_class
import os
def main():
    numer_stron_sesji = 0
    id_offer = 1

    db_operations.clear_tables()

    while numer_stron_sesji == 0:
        bot = bot_class.Bot()
        bot.click_button_acc()
        numer_stron_sesji = bot.get_all_sites_nums()

    #print("title, company, location, management_level, salary_from, tryb_pracy, etat, kontrakt, specjalizacja, technologie_wymagane[LISTA], technologie_mile_widziane[LISTA], doswiadczenie") #Will be more data later
    while int(bot.current_site) <= int(numer_stron_sesji):
        bot.get_data(numer_stron_sesji)
        formatted_list = []
        unique_items = set()
        for inner_list in bot.dane_oferty:
            formatted_item = (
                inner_list[0],#title
                inner_list[1],#company
                inner_list[2],#location
                inner_list[3],#management_level
                inner_list[4],#salary
                inner_list[5],#tryb_pracy
                inner_list[6],#etat
                inner_list[7],#kontrakt
                inner_list[8],#specjalizacja
                tuple(inner_list[9]),# technologie_wymagane (converted to a tuple)
                tuple(inner_list[10]),# technologie_mile_widziane (converted to a tuple)
                inner_list[11],#doswiadczenie
            )
            if formatted_item not in unique_items:
                formatted_list.append(formatted_item)
                unique_items.add(formatted_item)
        #insert data to database
        id_offer = db_operations.insert_data(formatted_list, id_offer)
        os.system('cls')
        print(f"\rProgres: {bot.current_site} / {numer_stron_sesji}")
        bot.go_to_next_site()

    db_operations.insert_to_historic_data()
    #TODO:
    # add mysql to docker
    # visualize data
    
if __name__ == "__main__":
    main()