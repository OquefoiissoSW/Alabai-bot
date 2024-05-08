import sqlite3
import telebot
import database
from telebot import types

API_TOKEN = '6939818087:AAE_Xii_G2uncUOQ9_DuqQsuUjFnIlTmClU'
bot = telebot.TeleBot(API_TOKEN)

conn = sqlite3.connect("Students.db", check_same_thread=False)
cursor = conn.cursor()

create_table_query = '''
    CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY,
    surname VARCHAR(255) NOT NULL,
    subject VARCHAR(255) NOT NULL,
    attendance INTEGER,
    marks INTEGER
    )
    '''

cursor.execute(create_table_query)
cursor.execute("INSERT INTO attendance (surname, subject, attendance, marks) VALUES (?, ?, ?, ?)",
               ('Литвинов', 'Математика', 60, 45))
last_subject = ''

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет, я ваш телеграм-бот!")

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton("Узнать мою успеваемость")
    markup.add(item)

    bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Узнать мою успеваемость")
def handle_key(message):
    msg = bot.send_message(message.chat.id, "Введите название дисциплины")
    bot.register_next_step_handler(msg, find_subject)

def is_exists(message):
    cursor.execute("SELECT * FROM attendance WHERE subject=?", (message.text,))
    if cursor.fetchone() is None:
        return False
    else:
        return True

def find_subject(message):
    subject = message.text.strip()
    last_subject = subject
    # Поиск студентов по дисциплине
    cursor.execute('''
            SELECT surname, attendance, marks
            FROM attendance
            WHERE subject = ?
        ''', (subject,))
    results = cursor.fetchall()

    if results:
        bot.reply_to(message, 'Введите фамилию')
        bot.register_next_step_handler(message, print_stat)

        # for result in results:
        #     surname, attendance, marks = result
        #     response = f"Студент: {surname}\nПосещаемость: {attendance}\nБаллы: {marks}\n\n"
        #     bot.reply_to(message, response)
    else:
        bot.reply_to(message, "По вашему запросу ничего не найдено.")

def print_stat(message):
    cursor.execute('''
        SELECT attendance, marks
        FROM attendance
        WHERE surname = ? AND subject = ? 
    ''', (message.text.strip(), last_subject))

    result = cursor.fetchone()

    attendance, mark = result
    response = f"Успеваемость студента {message} по дисциплине {last_subject}:\nПосещаемость = {attendance}\nБаллы = {mark}"
    bot.reply_to(message, response)

bot.polling()