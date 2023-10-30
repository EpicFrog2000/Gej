from bot_class_indeed import Bot
from db_operations_indeed import insert_data

#db_operations_indeed.clear_tables() DO NOT USE PLZ BROOO
def gather_data():
    bot = Bot()
    bot.get_data()
    insert_data(bot.data)
#print("DONE!")
gather_data()