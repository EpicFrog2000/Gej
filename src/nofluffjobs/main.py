import db_operations
import bot_class_nofluffjobs
import os

        
max_sites_num = 0
id_offer = 1
db_operations.clear_tables()

while(max_sites_num == 0):
    bot = bot_class_nofluffjobs.Bot()
    bot.kliknij_przycisk_ciasteczka()
    max_sites_num = bot.get_all_sites_nums()

while(int(bot.obecna_strona) <= int(max_sites_num)):
    print("Progres:", bot.obecna_strona, "/", max_sites_num)
    bot.get_linki_from_current_site()
    bot.get_data_from_offers()
    #isnert data to db
    id_offer = db_operations.insert_data(bot.dane_z_ofert_stron, id_offer)
    bot.go_next_site()
    os.system('cls' if os.name == 'nt' else 'clear')
db_operations.insert_historic_data()
print("done!")

#That is much better than first one, plz someone rewrite itpracujpl module :)