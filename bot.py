import telebot
import os
import irkcovid
import irkweather

token = os.getenv("TOKEN")
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     text="Привет, это PorridgeMeisterBot!\n"
                          "Если хочешь узнать актуальную статистику по коронавирусу пиши /covid\n"
                          "А если хочешь увидеть погоду пиши /weather\n")


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, text="Помощь")


@bot.message_handler(commands=['covid'])
def covid(message):
    irkcovid.start_parse()
    covid_message = str(
        irkcovid.date_news + '\n'+"Актуальные новости по коронавирусу:" + '\n'
        + irkcovid.title_news + '\n' + irkcovid.content_news + '\n'
        + "!" + "Число заболевших в Иркутске! - " + irkcovid.irk_infected)
    bot.send_message(message.chat.id, text=covid_message)


@bot.message_handler(commands=['weather'])
def weather(message):
    irkweather.start_parse()
    weather_message = str("Актульная погода:\n"+"Температура: "+irkweather.temperature+'\n'+irkweather.wind+'\n' \
                                                                                                         ''+irkweather\
        .humidity)
    bot.send_message(message.chat.id, text=weather_message)


bot.polling(none_stop=True)
