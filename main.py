import db_operations
import bot_class
    
bot = bot_class.Bot()
bot.get_site_ready()
bot.click_button_acc()
numer_stron_sesji = bot.get_all_sites_nums()
#print("title, company, location, management_level, salary_from, tryb_pracy, etat, kontrakt, specjalizacja, technologie_wymagane[LISTA], technologie_mile_widziane[LISTA]") #Will be more data later
while int(bot.current_site) <= int(numer_stron_sesji):
    print("\r Progres: ", bot.current_site, " / ", numer_stron_sesji)
    bot.get_data()
    formatted_list = []
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
        )
        formatted_list.append(formatted_item)
    #insert data to database
    db_operations.insert_data(formatted_list)
    bot.go_to_next_site()
#TODO:
# link with database
# split, format and "make usable" info form data like kontrakt, specjalizacja or management_level
# ^ maybe get discionary of this data to better insert into database
# finish getting  doswiadczenie and studia/wykrztalcenie?
# add mysql to docker