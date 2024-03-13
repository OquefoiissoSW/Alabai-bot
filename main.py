import sqlite3
import telebot
from telebot import types

API_TOKEN = '6939818087:AAE_Xii_G2uncUOQ9_DuqQsuUjFnIlTmClU'
bot = telebot.TeleBot(API_TOKEN)
conn = sqlite3.connect("Students.db", check_same_thread=False)
cursor = conn.cursor()

@bot.message_handler(commands=['start'])
def handle_start(message):
    fill_table()

    bot.send_message(message.chat.id, "Привет, я ваш телеграм-бот!")

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton("Узнать мою успеваемость")
    markup.add(item)

    bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Узнать мою успеваемость")
def handle_key(message):
    msg = bot.send_message(message.chat.id, "Введите фамилию")
    bot.register_next_step_handler(msg, print_stat)

def print_stat(message):
    #bot.send_message(message.chat.id, message.text)
    cursor.execute("SELECT * FROM Students WHERE Surname=?", (message.text,))
    student_data = cursor.fetchone()

    if student_data:
        bot.send_message(message.chat.id, str(student_data[1]))
        bot.send_message(message.chat.id, str(student_data[2]))
    else:
        bot.send_message(message.chat.id, "Студент с такой фамилией не найден")
    #cursor.execute("SELECT * FROM Users WHERE Name=?", (name_to_find,))

def fill_table():
    create_table_query = """
        CREATE TABLE IF NOT EXISTS Students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        surname VARCHAR(255) NOT NULL,
        group_name VARCHAR(255) NOT NULL
        )
        """
    cursor.execute(create_table_query)
    cursor.execute("INSERT INTO Students (surname, group_name) VALUES (?, ?)", ('Литвинов', 'ИВТ-232'))
    cursor.execute("INSERT INTO Students (surname, group_name) VALUES (?, ?)", ('Пропердолина', 'ИВТ-231'))

bot.polling()