import telebot
from telebot import types
token='7423073356:AAFepO2Qx2lUhk9brXXXHkuLoDSWQvfJzyM'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет')
@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Кнопка")
    markup.add(item1)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Кнопка":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Кнопка 2")
        markup.add(item1)
        bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
    elif message.text=="Кнопка 2":
        bot.send_message(message.chat.id,'Спасибо за прочтение статьи!')
bot.infinity_polling()








#import telebot

# Создаем бота с токеном
#bot = telebot.TeleBot('7423073356:AAFepO2Qx2lUhk9brXXXHkuLoDSWQvfJzyM')

# Создаем обработчик команды /start
#@bot.message_handler(commands=['start'])
#def handle_start(message):
    # создаем кнопку и клавиатуру для отправки контакта
 #   btn_phone = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
  #  btn_phone.add(telebot.types.KeyboardButton(text='Отправить свой контакт ☎️', request_contact=True))
   # # Отправляем приветственное сообщение с кнопкой
    #bot.send_message(message.chat.id, 'Привет! Отправь мне свой контакт, чтобы я записал твои данные и продал их на китайском  теневом рынке :D', reply_markup=btn_phone)

# Запускаем бота
#bot.infinity_polling()