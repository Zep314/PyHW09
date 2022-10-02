# Контроллер программы

from mylog import add2log
import telebot

from ruGPT3requests import generate_ruGPT3
from parser import complexculator
import settings

bot = telebot.TeleBot(settings.bot_tocken)

@bot.message_handler(commands=['help'])
def send_start_message(message):
    bot.reply_to(message, 'ИИ сочинятель текстов и онлайн - калькулятор комплексных выражений\n'
                          'Напиши первые предложения для генерации текста\n'
                          'Для получения справки - /help\n'
                          'Для получения информации - /info\n\n'
                          'Генерировать текст - /gpt3 <Начальная "затравка для текста">\n'
                          'Пример:\n'
                          f'\t /gpt3 Однажды, в студеную зимнюю пору, Я из\n\n'
                          'Посчитать выражение - /calc <выражение>\n'
                          'Пример:\n'
                          f'\t - посчитать простое выражение - пишем: 2+5*7\n'
                          f'\t - посчитать выражение со скобками - пишем: 15/(7-(1+1))*3-(2+(1+1))\n'
                          f'\t - посчитать выражение в комплексных числах- пишем: (2+3i)*(4+5i)\n'
                          f'\t - посчитать навороченное выражение в комплексных числах- пишем: (2+3i)*(4+5i)-(-3-6i)+(8+2i)/4\n'
                 )

@bot.message_handler(commands=['info'])
def send_help_message(message):
    bot.reply_to(message, 'Бот для генерации текстов.\n'
                          'Используется модель ruGPT3 от Сбербанка\n'
                          'Так же умеет считать математические выражения в комплексных числах\n'
                 )

@bot.message_handler(commands=['calc'])
def calc_bot(message):
    bot.send_chat_action(message.chat.id, 'typing')
    add2log('<' + message.text)
    try:
        text = complexculator(message.text[6:])
    except:
        text = "Не могу ввчислить - ошибка в выражении"
    bot.reply_to(message, text)
    add2log('>' + text)

@bot.message_handler(commands=['gpt3'])
def gpt3_bot(message):
    bot.send_chat_action(message.chat.id, 'typing')
    add2log('<' + message.text)
    text = message.text[6:]
    text = generate_ruGPT3(text)
    add2log('>' + text)
    while len(text)>0:  # почему то send_message посылает только по 2048 символов в сообщении.
                        # поэтому посылаем несколькими кусками
        bot.send_message(message.chat.id, text[:2048])
        text = text[2048:]

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    add2log('<'+message.text)
    bot.reply_to(message, message.text)
    bot.send_message(message.chat.id,'Непонятно... Напиши /help - для помощи')
