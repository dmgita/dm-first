import telebot

bot = telebot.TeleBot ( "5343720689:AAGj_7YiqKb5wpmiFEPap9pzAJeSCUVaa-o" )

bot.send_message('250690401', 'У меня есть всё что нужно')

# # Handle '/start' and '/help'
# @bot.message_handler(commands=['help', 'start'])
# def send_welcome(message):
#     bot.reply_to(message, """\
# Привет, это Радио Барсик
# \
# """)
# 
# 
# # Handle all other messages with content_type 'text' (content_types defaults to ['text'])
# 
# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
# #     bot.reply_to(message, message.text)
# #     print(message.id)
#     bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
#     print (message.chat.id)
# 
# 
# bot.infinity_polling()

