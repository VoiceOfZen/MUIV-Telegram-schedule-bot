import telebot
import datetime
import json
import config
from constants import *
from telebot import types

bot = telebot.TeleBot(config.TOKEN)
with open('./users.txt') as fi:
    di = json.load(fi)


@bot.message_handler(content_types=['text'])
def check(message):
    user_id = str(message.chat.id)
    print(date_from_message(message.date))

    if user_id not in di:
        di[user_id] = {FACULTY_KEY: 0, FORM_KEY: 0, YEAR_KEY: 0, GROUP_KEY: 0}

    if not di[user_id][FACULTY_KEY]:
        choose_faculty_menu(user_id)
    elif not di[user_id][FORM_KEY]:
        choose_form_menu(user_id, di[user_id][FACULTY_KEY])
    elif not di[user_id][YEAR_KEY]:
        choose_year_and_check_form(user_id, di[user_id][FORM_KEY])
    elif not di[user_id][GROUP_KEY]:
        choose_group_and_check_year(user_id, di[user_id][YEAR_KEY])
    else:
        show_menu(user_id, di[user_id][GROUP_KEY])
    save_dict()


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    user_id = str(call.from_user.id)
    data = call.data

    if data == 'back':
        di[user_id] = {FACULTY_KEY: 0, FORM_KEY: 0, YEAR_KEY: 0, GROUP_KEY: 0}
        choose_faculty_menu(user_id)

    elif data == 'schedule today':
        bot.send_message(user_id, text="TODAY")
    elif data == 'schedule tomorrow':
        bot.send_message(user_id, text="TOMORROW")
    elif data == 'schedule week':
        bot.send_message(user_id, text="WEEK")

    elif data in FACULTIES:
        di[user_id][FACULTY_KEY] = data
        choose_form_menu(user_id, data)
    elif data in FORMS:
        di[user_id][FORM_KEY] = data
        choose_year_and_check_form(user_id, data)
    elif data in YEARS_OF_IT:
        di[user_id][YEAR_KEY] = data
        choose_group_and_check_year(user_id, data)
    elif data in GROUPS:
        di[user_id][GROUP_KEY] = data
        show_menu(user_id, data)

    save_dict()



def date_from_message(timestamp):
    utc_offset = 3  # UTC+3
    date = datetime.datetime.utcfromtimestamp(timestamp) + datetime.timedelta(hours=utc_offset)
    day_of_week = date.strftime("%A")

    output = f"Today is {date.date()} \nTime {date.time()} UTC{utc_offset:+03d}, \nDay of the week {day_of_week}\n"

    # Get tomorrow's date
    tomorrow = date + datetime.timedelta(days=1)
    output += f"Tomorrow is {tomorrow.date()}\n"

    # Get all seven days of the current week
    week_start = date - datetime.timedelta(days=date.weekday())
    for i in range(7):
        current_day = week_start + datetime.timedelta(days=i)
        output += f"{current_day.strftime('%A')}: {current_day.date()}\n"

    return output


def choose_faculty_menu(user_id):
    keyboard = types.InlineKeyboardMarkup(row_width=1)  # inline keyboard
    button = types.InlineKeyboardButton(text='Факультет ит', callback_data=FACULTY_0)
    keyboard.add(button)

    question = 'на каком ты факультете?'
    bot.send_message(user_id, text=question, reply_markup=keyboard)


def choose_form_menu(user_id, faculty):
    question = faculty + ' Какая у тебя форма обучения?'
    keyboard = types.InlineKeyboardMarkup(row_width=1)  # inline keyboard
    button_och = types.InlineKeyboardButton(text='очная', callback_data=FORM_0)
    button_och_zao = types.InlineKeyboardButton(text='очно-заочная выходного дня', callback_data=FORM_1)
    button_zao = types.InlineKeyboardButton(text='заочная выходного дня', callback_data=FORM_2)
    keyboard.add(button_och, button_och_zao, button_zao)
    add_keyboard_back_button(keyboard)

    bot.send_message(user_id, text=question, reply_markup=keyboard)


def choose_year_and_check_form(user_id, form):
    question = form + ' на каком ты году обучения?'
    if form == FORM_0:
        keyboard = types.InlineKeyboardMarkup(row_width=3)  # inline keyboard

        year_1 = types.InlineKeyboardButton(text='1', callback_data=Y1_F0)
        year_2 = types.InlineKeyboardButton(text='2', callback_data=Y2_F0)
        year_3 = types.InlineKeyboardButton(text='3', callback_data=Y3_F0)
        keyboard.add(year_1, year_2, year_3)

        year_1_spo = types.InlineKeyboardButton(text='1spo', callback_data=Y1S_F0)
        year_2_spo = types.InlineKeyboardButton(text='2spo', callback_data=Y2S_F0)
        year_3_spo = types.InlineKeyboardButton(text='3spo', callback_data=Y3S_F0)
        keyboard.add(year_1_spo, year_2_spo, year_3_spo)

        year_4 = types.InlineKeyboardButton(text='4', callback_data=Y4_F0)
        keyboard.add(year_4)
        add_keyboard_back_button(keyboard)

        bot.send_message(user_id, text=question, reply_markup=keyboard)
    elif form == FORM_1:
        keyboard = types.InlineKeyboardMarkup(row_width=3)  # inline keyboard

        year_1 = types.InlineKeyboardButton(text='1', callback_data=Y1_F1)
        year_1_spo = types.InlineKeyboardButton(text='1spo', callback_data=Y1S_F1)
        year_2_spo = types.InlineKeyboardButton(text='2spo', callback_data=Y2S_F1)
        keyboard.add(year_1, year_1_spo, year_2_spo)
        add_keyboard_back_button(keyboard)

        bot.send_message(user_id, text=question, reply_markup=keyboard)
    elif form == FORM_2:
        keyboard = types.InlineKeyboardMarkup(row_width=3)  # inline keyboard

        year_1_spo = types.InlineKeyboardButton(text='1spo', callback_data=Y1S_F2)
        year_3_spo = types.InlineKeyboardButton(text='3spo', callback_data=Y3S_F2)
        year_4_spo = types.InlineKeyboardButton(text='4spo', callback_data=Y4S_F2)
        keyboard.add(year_1_spo, year_3_spo, year_4_spo)
        add_keyboard_back_button(keyboard)

        bot.send_message(user_id, text=question, reply_markup=keyboard)


def choose_group_and_check_year(user_id, year):
    question = year + ' В какой ты группе?'
    if year == Y1_F0:
        keyboard = types.InlineKeyboardMarkup(row_width=1)  # inline keyboard
        group_0 = types.InlineKeyboardButton(text='ИД 30.1/Б-22', callback_data=G0_Y1_F0)
        group_1 = types.InlineKeyboardButton(text='ИД 23.1/Б-22', callback_data=G1_Y1_F0)
        keyboard.add(group_0, group_1)
        add_keyboard_back_button(keyboard)

        bot.send_message(user_id, text=question, reply_markup=keyboard)
    elif year == Y2_F0:
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        group_0 = types.InlineKeyboardButton(text='о. ИД 23.1/Б-21', callback_data=G0_Y2_F0)
        group_1 = types.InlineKeyboardButton(text='о. ИД 23.2/Б-21', callback_data=G1_Y2_F0)
        group_2 = types.InlineKeyboardButton(text='о. ИД 23.3/Б-21', callback_data=G2_Y2_F0)
        group_3 = types.InlineKeyboardButton(text='о. ИД 23.4/Б-21', callback_data=G3_Y2_F0)
        group_4 = types.InlineKeyboardButton(text=G4_Y2_F0, callback_data=G4_Y2_F0)
        keyboard.add(group_0, group_1, group_2, group_3, group_4)
        add_keyboard_back_button(keyboard)

        bot.send_message(user_id, text=question, reply_markup=keyboard)
    elif year == Y3_F0:
        keyboard = types.InlineKeyboardMarkup(row_width=1)  # inline keyboard
        group_0 = types.InlineKeyboardButton(text='ИД 23.1/Б1-20', callback_data=G0_Y3_F0)
        group_1 = types.InlineKeyboardButton(text='ИД 23.1/Б2-20', callback_data=G1_Y3_F0)
        group_2 = types.InlineKeyboardButton(text='ИД 23.2/Б2-20', callback_data=G2_Y3_F0)
        keyboard.add(group_0, group_1, group_2)
        add_keyboard_back_button(keyboard)

        bot.send_message(user_id, text=question, reply_markup=keyboard)
    elif year == Y1S_F0:
        keyboard = types.InlineKeyboardMarkup(row_width=1)  # inline keyboard
        group_0 = types.InlineKeyboardButton(text='ИДс 23.1/Б-22', callback_data=G0_Y1S_F0)
        keyboard.add(group_0)
        add_keyboard_back_button(keyboard)

        bot.send_message(user_id, text=question, reply_markup=keyboard)
    elif year == Y2S_F0:
        keyboard = types.InlineKeyboardMarkup(row_width=1)  # inline keyboard
        group_0 = types.InlineKeyboardButton(text='о.ИДс 23.1/Б3-21', callback_data=G0_Y2S_F0)
        keyboard.add(group_0)
        add_keyboard_back_button(keyboard)

        bot.send_message(user_id, text=question, reply_markup=keyboard)
    elif year == Y3S_F0:
        keyboard = types.InlineKeyboardMarkup(row_width=1)  # inline keyboard
        group_0 = types.InlineKeyboardButton(text='ИДс 23.1/Б1-20', callback_data=G0_Y3S_F0)
        keyboard.add(group_0)
        add_keyboard_back_button(keyboard)

        bot.send_message(user_id, text=question, reply_markup=keyboard)
    elif year == Y4_F0:
        keyboard = types.InlineKeyboardMarkup(row_width=1)  # inline keyboard
        group_0 = types.InlineKeyboardButton(text='ИД 23.1/Б1-19', callback_data=G0_Y4_F0)
        group_1 = types.InlineKeyboardButton(text='ИД 23.2/Б1-19', callback_data=G1_Y4_F0)
        group_2 = types.InlineKeyboardButton(text='ИД 23.1/Б2-19', callback_data=G2_Y4_F0)
        keyboard.add(group_0, group_1, group_2)
        add_keyboard_back_button(keyboard)

        bot.send_message(user_id, text=question, reply_markup=keyboard)

    elif year == Y1_F1:
        keyboard = types.InlineKeyboardMarkup(row_width=1)  # inline keyboard
        group_0 = types.InlineKeyboardButton(text='ИВС 30.1/Б-22', callback_data=G0_Y1_F1)
        keyboard.add(group_0)
        add_keyboard_back_button(keyboard)

        bot.send_message(user_id, text=question, reply_markup=keyboard)
    elif year == Y1S_F1:
        keyboard = types.InlineKeyboardMarkup(row_width=1)  # inline keyboard
        group_0 = types.InlineKeyboardButton(text='ИВСс 30.1/Б-22', callback_data=G0_Y1S_F1)
        keyboard.add(group_0)
        add_keyboard_back_button(keyboard)

        bot.send_message(user_id, text=question, reply_markup=keyboard)
    elif year == Y2S_F1:
        keyboard = types.InlineKeyboardMarkup(row_width=1)  # inline keyboard
        group_0 = types.InlineKeyboardButton(text='ИВСс 23.1/Б-21', callback_data=G0_Y2S_F1)
        group_1 = types.InlineKeyboardButton(text='ИВСс 30.1/Б-21', callback_data=G1_Y2S_F1)
        keyboard.add(group_0, group_1)
        add_keyboard_back_button(keyboard)

        bot.send_message(user_id, text=question, reply_markup=keyboard)
    elif year == Y1S_F2:
        keyboard = types.InlineKeyboardMarkup(row_width=1)  # inline keyboard
        group_0 = types.InlineKeyboardButton(text='ИСс 23.1/Б-22', callback_data=G0_Y1S_F2)
        group_1 = types.InlineKeyboardButton(text='ИСс 23.2/Б-22', callback_data=G1_Y2S_F1)
        keyboard.add(group_0, group_1)
        add_keyboard_back_button(keyboard)

        bot.send_message(user_id, text=question, reply_markup=keyboard)
    elif year == Y3S_F2:
        keyboard = types.InlineKeyboardMarkup(row_width=1)  # inline keyboard
        group_0 = types.InlineKeyboardButton(text='ИСс 23.1/Б1-20', callback_data=G0_Y3S_F2)
        keyboard.add(group_0)
        add_keyboard_back_button(keyboard)

        bot.send_message(user_id, text=question, reply_markup=keyboard)
    elif year == Y4S_F2:
        keyboard = types.InlineKeyboardMarkup(row_width=1)  # inline keyboard
        group_0 = types.InlineKeyboardButton(text='ИСс 23.1/Б1-19', callback_data=G0_Y4S_F2)
        keyboard.add(group_0)
        add_keyboard_back_button(keyboard)

        bot.send_message(user_id, text=question, reply_markup=keyboard)


def show_menu(user_id, group):
    keyboard = types.InlineKeyboardMarkup(row_width=3)  # inline keyboard

    schedule_today = types.InlineKeyboardButton(text='сегодня', callback_data='schedule today')
    schedule_tomorrow = types.InlineKeyboardButton(text='завтра', callback_data='schedule tomorrow')
    schedule_week = types.InlineKeyboardButton(text='неделя', callback_data='schedule week')
    keyboard.add(schedule_today, schedule_tomorrow, schedule_week)
    add_keyboard_back_button(keyboard)

    question = f'расписание группы {group}'
    bot.send_message(user_id, text=question, reply_markup=keyboard)


def add_keyboard_back_button(keyboard):
    back = types.InlineKeyboardButton(text='в начало', callback_data='back')
    keyboard.add(back)


def save_dict():
    with open('./users.txt', 'w') as f:
        json.dump(di, f)


bot.polling(none_stop=True)
