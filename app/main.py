import telebot;
from text import price_list, barbers, free_time
from telebot import types
bot =  telebot.TeleBot('7292320375:AAH3488C1HEFoCQMv64N0ozidOJxcqEqTNs')

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Добро пожаловать в наш барбершоп! Как я могу вам помочь?")



@bot.message_handler(commands=['price'])
def handle_price(message):
    text= "Прайс-лист на различные виды стрижек:\n"
    for item in price_list:
        text += f"{item['service']}: {item['price']} рублей\n"
    bot.reply_to(message, text)


@bot.message_handler(commands=['barbers'])
def handle_price(message):
    text = "Наши барбера:\n"
    for item in barbers:
        text += f"{item['name']}. {item['experience']}. Специализация: {item['specialization']}\n"
    bot.reply_to(message, text)



@bot.message_handler(commands=["freetime"])
def send_time(message):
    if free_time:
        text = "Свободные окошки:\n"
        for time in free_time:
            text += f"- {time}\n"
    bot.reply_to(message, text)

bot.polling(none_stop=True)