# -----------------------------------------Import-----------------------------------------------

import telebot
import config
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import random

bot = telebot.TeleBot(config.token)


# ------------------------------------Keyboard_Buttons------------------------------------------

# def keyboard_buttons():
#     markup = ReplyKeyboardMarkup()
#     button1 = KeyboardButton("Відішли рандомне число")
#     button2 = KeyboardButton("Скільки буде 5")
#     markup.add(button1, button2)
#     return markup

# ------------------------------------Inline_Buttons--------------------------------------------

# player1 = "Seal"
# player2 = "Giorno Petruchio"

# def set_inline_buttons_stone():
#     markup = InlineKeyboardMarkup() # - бібліотека (не чіпай, жовте це бібліотека)
#     button1 = InlineKeyboardButton("Піти наліво", callback_data="У каменя вибрано наліво")
#     button2 = InlineKeyboardButton("Піти направо", callback_data="У каменя вибрано направо")
#     button3 = InlineKeyboardButton("Піти в ліс", callback_data="У каменя вибрано в ліс")
#     button4 = InlineKeyboardButton("Піти до моря", callback_data="У каменя вибрано до моря")
#     button5 = InlineKeyboardButton("Ти точьно хочешь піти в ліс", callback_data="Ти точно хочешь піти в ліс")
#     button6 = InlineKeyboardButton("Ти точьно хочешь піти до моря", callback_data="Ти точно хочешь піти до моря")
#     markup.add(button1, button2, button3, button4)
#     markup.add(button5, button6)
#     return markup

# --------------------------------------За кого грати-------------------------------------------

# def set_inline_buttons_chess():
#    markup = InlineKeyboardMarkup()
#    button1 = InlineKeyboardButton("Грати за білих", callback_data="У гравця вибір грати білими")
#    button2 = InlineKeyboardButton("Грати за чорних", callback_data="У гравця вибір грати чорними")
#    markup.add(button1, button2)
#    return markup

# ----------------------------------------Стадія гри--------------------------------------------

def set_inline_buttons_chess_platz2():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("Дебют", callback_data="У гравця вибір грати в дебюті")
    button2 = InlineKeyboardButton("Мітельшпіль", callback_data="У гравця вибір грати в мітельшпілі")
    button3 = InlineKeyboardButton("Ендшпіль", callback_data="У гравця вибір грати в Еншпілі")
    markup.add(button1, button2, button3)
    return markup


# -----------------------------------------Дебют------------------------------------------------

def set_inline_buttons_chess_platz21():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("Італійська партія", callback_data="Италійському дебюті")
    button2 = InlineKeyboardButton("Сицілійський захист", callback_data="Сицилянському дебюті")
    markup.add(button1, button2)
    return markup


# --------------------------------------Мітельшпіль---------------------------------------------

def set_inline_buttons_chess_platz22():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("Відкритий мітельшпіль", callback_data="відкритому мітельшпілі")
    button2 = InlineKeyboardButton("Закритий мітельшпіль", callback_data="закритому мітельшпілі")
    button3 = InlineKeyboardButton("Напів закритий мітельшпіль", callback_data="напів закритому мітельшпілі")
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    return markup


# --------------------------------------Ендшпіль------------------------------------------------

def set_inline_buttons_chess_platz23():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("Пішаковий ендшпіль", callback_data="Пішаковий ендшпіль")
    button2 = InlineKeyboardButton("Слоновий ендшпіль", callback_data="Слоновому ендшпіль")
    button3 = InlineKeyboardButton("Багато фігурний ендшпіль", callback_data="Багато фігурний ендшпіль")
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    return markup


# ----------------------------------------Задачі------------------------------------------------

def set_inline_buttons_chess_platz3():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("Задача №1", callback_data="Задача1")
    button2 = InlineKeyboardButton("Задача №2", callback_data="Задача2")
    button3 = InlineKeyboardButton("Задача №3", callback_data="Задача3")
    markup.add(button1, button2, button3)
    return markup


def set_inline_buttons_chess_platz31():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("Задача №1", callback_data="Задача1.2")
    button2 = InlineKeyboardButton("Задача №2", callback_data="Задача2.2")
    button3 = InlineKeyboardButton("Задача №3", callback_data="Задача3.2")
    markup.add(button1, button2, button3)
    return markup


def set_inline_buttons_chess_platz32():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("Задача №1", callback_data="Задача1.3")
    button2 = InlineKeyboardButton("Задача №2", callback_data="Задача2.3")
    button3 = InlineKeyboardButton("Задача №3", callback_data="Задача3.3")
    markup.add(button1, button2, button3)
    return markup


def set_inline_buttons_chess_platz33():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("Задача №1", callback_data="Задача1.4")
    button2 = InlineKeyboardButton("Задача №2", callback_data="Задача2.4")
    button3 = InlineKeyboardButton("Задача №3", callback_data="Задача3.4")
    markup.add(button1, button2, button3)
    return markup


def set_inline_buttons_chess_platz34():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("Задача №1", callback_data="Задача1.5")
    button2 = InlineKeyboardButton("Задача №2", callback_data="Задача2.5")
    button3 = InlineKeyboardButton("Задача №3", callback_data="Задача3.5")
    markup.add(button1, button2, button3)
    return markup


def set_inline_buttons_chess_platz35():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("Задача №1", callback_data="Задача1.6")
    button2 = InlineKeyboardButton("Задача №2", callback_data="Задача2.6")
    button3 = InlineKeyboardButton("Задача №3", callback_data="Задача3.6")
    markup.add(button1, button2, button3)
    return markup


def set_inline_buttons_chess_platz36():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("Задача №1", callback_data="Задача1.7")
    button2 = InlineKeyboardButton("Задача №2", callback_data="Задача2.7")
    button3 = InlineKeyboardButton("Задача №3", callback_data="Задача3.7")
    markup.add(button1, button2, button3)
    return markup


def set_inline_buttons_chess_platz37():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("Задача №1", callback_data="Задача1.8")
    button2 = InlineKeyboardButton("Задача №2", callback_data="Задача2.8")
    button3 = InlineKeyboardButton("Задача №3", callback_data="Задача3.8")
    markup.add(button1, button2, button3)
    return markup


# ----------------------------------------------------------------------------------------------

# def set_inline_buttons_chess_platz10():
#    markup = InlineKeyboardMarkup()
#    button1 = InlineKeyboardButton("Назад", callback_data="Назад")
#    markup.add(button1)
#    return markup

# --------------------------------------Ким грати?----------------------------------------------

# @bot.message_handler(commands=["chess"])
# def chess_arbeit_platz_zwie(message):
#     bot.send_message(message.chat.id, f"Привіт {message.from_user.last_name} {message.from_user.first_name}, за кого ви хочете вирішувати задачі?", reply_markup=set_inline_buttons_chess())

# ---------------------------------В якій епосі грати-------------------------------------------

@bot.message_handler(commands=["chess"])
def chess_arbeit_platz(message):
    bot.send_message(message.chat.id,
                     f" Привіт {message.from_user.last_name} {message.from_user.first_name}, Виберіть стадію партії:",
                     reply_markup=set_inline_buttons_chess_platz2())


# ----------------------------------------------------------------------------------------------

@bot.message_handler(commands=["chess3"])
def chess_arbeit_platz_drei(message):
    bot.send_message(message.chat.id, "Виберіть тему в задачі:", reply_markup=set_inline_buttons_chess_platz21())


# ----------------------------------------------------------------------------------------------

@bot.message_handler(commands=["chess4"])
def chess_arbeit_platz_vier(message):
    bot.send_message(message.chat.id, "Виберіть тему в задачі:", reply_markup=set_inline_buttons_chess_platz22())


# ----------------------------------------------------------------------------------------------

@bot.message_handler(commands=["chess5"])
def chess_arbeit_platz_fünf(message):
    bot.send_message(message.chat.id, "Виберіть тему в задачі:", reply_markup=set_inline_buttons_chess_platz23())


# ----------------------------------------------------------------------------------------------

@bot.message_handler(commands=["chess6"])
def chess_arbeit_platz_sechs(message):
    bot.send_message(message.chat.id, "Виберіть номер задачі:", reply_markup=set_inline_buttons_chess_platz3())


@bot.message_handler(commands=["chess7"])
def chess_arbeit_platz_sechs2(message):
    bot.send_message(message.chat.id, "Виберіть номер задачі:", reply_markup=set_inline_buttons_chess_platz31())


@bot.message_handler(commands=["chess8"])
def chess_arbeit_platz_sechs3(message):
    bot.send_message(message.chat.id, "Виберіть номер задачі:", reply_markup=set_inline_buttons_chess_platz32())


@bot.message_handler(commands=["chess9"])
def chess_arbeit_platz_sechs4(message):
    bot.send_message(message.chat.id, "Виберіть номер задачі:", reply_markup=set_inline_buttons_chess_platz33())


@bot.message_handler(commands=["chess10"])
def chess_arbeit_platz_sechs5(message):
    bot.send_message(message.chat.id, "Виберіть номер задачі:", reply_markup=set_inline_buttons_chess_platz34())


@bot.message_handler(commands=["chess11"])
def chess_arbeit_platz_sechs6(message):
    bot.send_message(message.chat.id, "Виберіть номер задачі:", reply_markup=set_inline_buttons_chess_platz35())


@bot.message_handler(commands=["chess12"])
def chess_arbeit_platz_sechs7(message):
    bot.send_message(message.chat.id, "Виберіть номер задачі:", reply_markup=set_inline_buttons_chess_platz36())


@bot.message_handler(commands=["chess13"])
def chess_arbeit_platz_sechs8(message):
    bot.send_message(message.chat.id, "Виберіть номер задачі:", reply_markup=set_inline_buttons_chess_platz37())


# ----------------------------------------------------------------------------------------------

# @bot.message_handler(commands=["chess7"])
# def chess_arbeit_platz_null(message):
#     bot.send_message(message.chat.id, "Назад", reply_markup=set_inline_buttons_chess_platz21())

# ---------------------------------------Start--------------------------------------------------

# @bot.message_handler(commands=["start"])
# def send_welcome(message):
#     bot.send_message(message.chat.id, f"Привіт, {message.from_user.last_name} {message.from_user.first_name}", reply_markup=keyboard_buttons())
#     bot.send_message(message.chat.id, f"Пішли {player1} і {player2}, і прийшли до каменя. І він пропонує:", reply_markup=set_inline_buttons_stone())

# ------------------------------------Continuation----------------------------------------------

# @bot.message_handler(commands=["continuation"])
# def continuation(message):
#     bot.send_message(message.chat.id, f"Мудрець підійшов до {player1} і {player2}, і сказав. Я не очікував що ви зможете пройти такий важкий шлях. тепер у вас є 2 виборо:", reply_markup=set_inline_buttons_stone())

# --------------------------------Keyboard_Buttons_Text-----------------------------------------

# @bot.message_handler(content_types=["text"])
# def conversation(message):
#     if message.text == "Відішли рандомне число":
#         random_num = random.randint(1,100)
#         bot.send_message(message.chat.id, random_num)
#     if message.text == "Скільки буде 5":
#       random_mem = "x'=x+vt"
#       bot.send_message(message.chat.id, random_mem)

# ---------------------------------------Кнопки-------------------------------------------------

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    #     if call.data == "У каменя вибрано наліво":
    #         bot.send_message(call.from_user.id, "Вам смерть, гра закінчена.")
    #     if call.data == "У каменя вибрано направо":
    #         bot.send_message(call.from_user.id, "Ура, ви дійшли до мудреця")
    #         bot.send_photo(call.from_user.id, "https://tureligious.com.ua/wp-content/uploads/2020/06/mydrex.jpg")
    #     if call.data == "У каменя вибрано в ліс":
    #         bot.send_message(call.from_user.id, "Ура тебе з'їли")
    #     if call.data == "У каменя вибрано до моря":
    #         bot.send_message(call.from_user.id, f"{player1} виживає а {player2} померає💀")
    #     if call.data == "Ти точно хочешь піти в ліс":
    #         bot.send_message(call.from_user.id, "Ти помер вже 2 рази. Зупинись і подумай!",reply_markup=set_inline_buttons_stone())
    #     if call.data == "Ти точно хочешь піти до моря":
    #         bot.send_message(call.from_user.id, f"{player2} померть, а {player1} пустили на чоботи.")

    # ----------------------------------------------------------------------------------------------

    # if call.data == "У гравця вибір грати білими":
    #     bot.send_message(call.from_user.id, "Виберіть стадію партії:",reply_markup=set_inline_buttons_chess_platz2())
    # if call.data == "У гравця вибір грати чорними":
    #     bot.send_message(call.from_user.id, "Виберіть стадію партії:",reply_markup=set_inline_buttons_chess_platz2())

    if call.data == "У гравця вибір грати в дебюті":
        bot.send_message(call.from_user.id, "Виберіть тему задачі:", reply_markup=set_inline_buttons_chess_platz21())
    if call.data == "У гравця вибір грати в мітельшпілі":
        bot.send_message(call.from_user.id, "Виберіть тему задачі:", reply_markup=set_inline_buttons_chess_platz22())
    if call.data == "У гравця вибір грати в Еншпілі":
        bot.send_message(call.from_user.id, "Виберіть тему задачі:", reply_markup=set_inline_buttons_chess_platz23())
    # if call.data == "Италійському дебюті":
    #     bot.send_audio(call.from_user.id, open("photo/123.jpg", "rb"))
    #     bot.send_audio(call.from_user.id, open("photo/1233.jpg", "rb"))
    if call.data == "Италійському дебюті":
        bot.send_message(call.from_user.id, "Виберіть номер задачі:", reply_markup=set_inline_buttons_chess_platz3())
        # bot.send_photo(call.from_user.id, open("photo/123.jpg", "rb"))
    if call.data == "Задача1":
        bot.send_photo(call.from_user.id, open("photo/итал.jpg", "rb"))
        # bot.send_message(call.from_user.id, "Ви хочете повернутися на один крок назад?", reply_markup=set_inline_buttons_chess_platz10())
    if call.data == "Задача2":
        bot.send_photo(call.from_user.id, open("photo/сицил.jpg", "rb"))
    if call.data == "Задача3":
        bot.send_photo(call.from_user.id, open("photo/непон.jpg", "rb"))
    if call.data == "Сицилянському дебюті":
        bot.send_message(call.from_user.id, "Виберіть номер задачі:", reply_markup=set_inline_buttons_chess_platz31())
    if call.data == "Задача1.2":
        bot.send_photo(call.from_user.id, open("photo/сицил.jpg", "rb"))
    if call.data == "Задача2.2":
        bot.send_photo(call.from_user.id, open("photo/сицил2.jpg", "rb"))
    if call.data == "Задача3.2":
        bot.send_photo(call.from_user.id, open("photo/сицил3.jpg", "rb"))
    if call.data == "відкритому мітельшпілі":
        bot.send_message(call.from_user.id, "Виберіть номер задачі:", reply_markup=set_inline_buttons_chess_platz32())
    if call.data == "Задача1.3":
        bot.send_photo(call.from_user.id, open("photo/відкритий1.jpg", "rb"))
    if call.data == "Задача2.3":
        bot.send_photo(call.from_user.id, open("photo/1234.png", "rb"))
    if call.data == "Задача3.3":
        bot.send_photo(call.from_user.id, open("photo/відкритий3.jpg", "rb"))
    if call.data == "закритому мітельшпілі":
        bot.send_message(call.from_user.id, "Виберіть номер задачі:", reply_markup=set_inline_buttons_chess_platz33())
    if call.data == "Задача1.4":
        bot.send_photo(call.from_user.id, open("photo/закритий.jpg", "rb"))
    if call.data == "Задача2.4":
        bot.send_photo(call.from_user.id, open("photo/закритий2.jpg", "rb"))
    if call.data == "Задача3.4":
        bot.send_photo(call.from_user.id, open("photo/закритий3.jpg", "rb"))
    if call.data == "напів закритому мітельшпілі":
        bot.send_message(call.from_user.id, "Виберіть номер задачі:", reply_markup=set_inline_buttons_chess_platz34())
    if call.data == "Задача1.5":
        bot.send_photo(call.from_user.id, open("photo/пів відкритий.jpg", "rb"))
    if call.data == "Задача2.5":
        bot.send_photo(call.from_user.id, open("photo/пів відкритий2.jpg", "rb"))
    if call.data == "Задача3.5":
        bot.send_photo(call.from_user.id, open("photo/пів відкритий3.jpg", "rb"))
    if call.data == "Пішаковий ендшпіль":
        bot.send_message(call.from_user.id, "Виберіть номер задачі:", reply_markup=set_inline_buttons_chess_platz35())
    if call.data == "Задача1.6":
        bot.send_photo(call.from_user.id, open("photo/пішак.jpg", "rb"))
    if call.data == "Задача2.6":
        bot.send_photo(call.from_user.id, open("photo/пішак2.jpg", "rb"))
    if call.data == "Задача3.6":
        bot.send_photo(call.from_user.id, open("photo/пішак3.jpg", "rb"))
    if call.data == "Слоновому ендшпіль":
        bot.send_message(call.from_user.id, "Виберіть номер задачі:", reply_markup=set_inline_buttons_chess_platz36())
    if call.data == "Задача1.7":
        bot.send_photo(call.from_user.id, open("photo/слон.jpg", "rb"))
    if call.data == "Задача2.7":
        bot.send_photo(call.from_user.id, open("photo/слон2.jpg", "rb"))
    if call.data == "Задача3.7":
        bot.send_photo(call.from_user.id, open("photo/слон3.jpg", "rb"))

    if call.data == "Багато фігурний ендшпіль":
        bot.send_message(call.from_user.id, "Виберіть номер задачі:", reply_markup=set_inline_buttons_chess_platz37())
    if call.data == "Задача1.8":
        bot.send_photo(call.from_user.id, open("photo/багато.jpg", "rb"))
    if call.data == "Задача2.8":
        bot.send_photo(call.from_user.id, open("photo/багато2.png", "rb"))
    if call.data == "Задача3.8":
        bot.send_photo(call.from_user.id, open("photo/багато3.jpg", "rb"))

    # ----------------------------------------------------------------------------------------------


bot.polling(none_stop=True)

# ----------------------------------------------------------------------------------------------