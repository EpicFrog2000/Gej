import bot_class_indeed
import db_operations_indeed

#db_operations_indeed.clear_tables() DO NOT USE PLZ BROOO
bot = bot_class_indeed.Bot()
bot.get_data()
db_operations_indeed.insert_data(bot.data)
print("DONE!")
