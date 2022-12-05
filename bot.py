import telebot
import json

import config

from constants import *
from telebot import types

bot = telebot.TeleBot(config.TOKEN)
with open('./users.txt') as fi:
    di = json.load(fi)


def add_keyboard_back_button(keyboard):
    back = types.InlineKeyboardButton(text='в начало', callback_data='back')
    keyboard.add(back)


@bot.message_handler(content_types=['text'])
def check(message):
    user_id = str(message.chat.id)

    if user_id not in di:
        di[user_id] = {FACULTY_KEY: 0, FORM_KEY: 0, YEAR_KEY: 0, GROUP_KEY: 0}

    if di[user_id][FACULTY_KEY]:
        if di[user_id][FORM_KEY]:
            if di[user_id][YEAR_KEY]:
                if di[user_id][GROUP_KEY]:
                    show_menu(user_id, di[user_id][GROUP_KEY])
                else:
                    save_dict()
                    choose_group_and_check_year(user_id, di[user_id][YEAR_KEY])
            else:
                save_dict()
                choose_year_and_check_form(user_id, di[user_id][FORM_KEY])
        else:
            save_dict()
            choose_form_menu(user_id, di[user_id][FACULTY_KEY])
    else:
        save_dict()
        choose_faculty_menu(user_id)


def save_dict():
    with open('./users.txt', 'w') as f:
        json.dump(di, f)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    # try:
    user_id = str(call.from_user.id)

    print()

    if call.data == 'back':
        di[user_id] = {FACULTY_KEY: 0, FORM_KEY: 0, YEAR_KEY: 0, GROUP_KEY: 0}
        save_dict()
        choose_faculty_menu(user_id)

    FACULTIES = {FACULTY_0}
    if call.data in FACULTIES:  # call.data = callback data that we sent when pressed the button
        di[str(user_id)][FACULTY_KEY] = call.data
        save_dict()
        choose_form_menu(user_id, call.data)

    FORMS = {FORM_0, FORM_1, FORM_2}
    if call.data in FORMS:
        di[str(user_id)][FORM_KEY] = call.data
        save_dict()
        choose_year_and_check_form(user_id, call.data)

    YEARS_OF_IT = {Y1_F0, Y2_F0, Y3_F0, Y1S_F0, Y2S_F0, Y3S_F0, Y4_F0,
                   Y1_F1, Y1S_F1, Y2S_F1,
                   Y1S_F2, Y3S_F2, Y4S_F2}
    if call.data in YEARS_OF_IT:
        di[str(user_id)][YEAR_KEY] = call.data
        save_dict()
        choose_group_and_check_year(user_id, call.data)

    GROUPS = {G0_Y1_F0, G1_Y1_F0,
              G0_Y2_F0, G1_Y2_F0, G2_Y2_F0, G3_Y2_F0, G4_Y2_F0,
              G0_Y3_F0, G1_Y3_F0, G2_Y3_F0,
              G0_Y1S_F0,
              G0_Y2S_F0,
              G0_Y3S_F0,
              G0_Y4_F0, G1_Y4_F0, G2_Y4_F0,

              G0_Y1_F1,
              G0_Y1S_F1,
              G0_Y2S_F1, G1_Y2S_F1,

              G0_Y1S_F2, G1_Y1S_F2,
              G0_Y3S_F2,
              G0_Y4S_F2
              }
    if call.data in GROUPS:
        di[str(user_id)][GROUP_KEY] = call.data
        save_dict()
        show_menu(user_id, call.data)

    # except Exception as e:
    #     print(repr(e))


def choose_faculty_menu(user_id):
    keyboard = types.InlineKeyboardMarkup(row_width=1)  # inline keyboard
    button = types.InlineKeyboardButton(text='IT Faculty', callback_data=FACULTY_0)
    keyboard.add(button)
    add_keyboard_back_button(keyboard)

    question = 'Whats your Faculty?'
    bot.send_message(user_id, text=question, reply_markup=keyboard)


def choose_form_menu(user_id, faculty):
    question = faculty + ' Whats your Form?'
    keyboard = types.InlineKeyboardMarkup(row_width=1)  # inline keyboard
    button_och = types.InlineKeyboardButton(text='Ochnaya', callback_data=FORM_0)
    button_och_zao = types.InlineKeyboardButton(text='Ochno-zaochaya vihodnogo dnya', callback_data=FORM_1)
    button_zao = types.InlineKeyboardButton(text='Zaochnaya vikhodnogo dnya', callback_data=FORM_2)
    keyboard.add(button_och, button_och_zao, button_zao)
    add_keyboard_back_button(keyboard)

    bot.send_message(user_id, text=question, reply_markup=keyboard)


def choose_group_and_check_year(user_id, year):
    question = year + ' Whats your group?'
    if year == Y1_F0:
        keyboard = types.InlineKeyboardMarkup(row_width=1)  # inline keyboard
        group_0 = types.InlineKeyboardButton(text=G0_Y1_F0, callback_data=G0_Y1_F0)
        group_1 = types.InlineKeyboardButton(text=G1_Y1_F0, callback_data=G1_Y1_F0)
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
        group_0 = types.InlineKeyboardButton(text=G0_Y3_F0, callback_data=G0_Y3_F0)
        group_1 = types.InlineKeyboardButton(text=G1_Y3_F0, callback_data=G1_Y3_F0)
        group_2 = types.InlineKeyboardButton(text=G2_Y3_F0, callback_data=G2_Y3_F0)
        keyboard.add(group_0, group_1, group_2)
        add_keyboard_back_button(keyboard)

        bot.send_message(user_id, text=question, reply_markup=keyboard)
    elif year == Y1S_F0:
        keyboard = types.InlineKeyboardMarkup(row_width=1)  # inline keyboard
        group_0 = types.InlineKeyboardButton(text=G0_Y1S_F0, callback_data=G0_Y1S_F0)
        keyboard.add(group_0)
        add_keyboard_back_button(keyboard)

        bot.send_message(user_id, text=question, reply_markup=keyboard)
    elif year == Y2S_F0:
        keyboard = types.InlineKeyboardMarkup(row_width=1)  # inline keyboard
        group_0 = types.InlineKeyboardButton(text=G0_Y2S_F0, callback_data=G0_Y2S_F0)
        keyboard.add(group_0)
        add_keyboard_back_button(keyboard)

        bot.send_message(user_id, text=question, reply_markup=keyboard)
    elif year == Y3S_F0:
        keyboard = types.InlineKeyboardMarkup(row_width=1)  # inline keyboard
        group_0 = types.InlineKeyboardButton(text=G0_Y3S_F0, callback_data=G0_Y3S_F0)
        keyboard.add(group_0)
        add_keyboard_back_button(keyboard)

        bot.send_message(user_id, text=question, reply_markup=keyboard)
    elif year == Y4_F0:
        keyboard = types.InlineKeyboardMarkup(row_width=1)  # inline keyboard
        group_0 = types.InlineKeyboardButton(text=G0_Y4_F0, callback_data=G0_Y4_F0)
        group_1 = types.InlineKeyboardButton(text=G1_Y4_F0, callback_data=G1_Y4_F0)
        group_2 = types.InlineKeyboardButton(text=G2_Y4_F0, callback_data=G2_Y4_F0)
        keyboard.add(group_0, group_1, group_2)
        add_keyboard_back_button(keyboard)

        bot.send_message(user_id, text=question, reply_markup=keyboard)

    elif year == Y1_F1:
        keyboard = types.InlineKeyboardMarkup(row_width=1)  # inline keyboard
        group_0 = types.InlineKeyboardButton(text=G0_Y1_F1, callback_data=G0_Y1_F1)
        keyboard.add(group_0)
        add_keyboard_back_button(keyboard)

        bot.send_message(user_id, text=question, reply_markup=keyboard)
    elif year == Y1S_F1:
        keyboard = types.InlineKeyboardMarkup(row_width=1)  # inline keyboard
        group_0 = types.InlineKeyboardButton(text=G0_Y1S_F1, callback_data=G0_Y1S_F1)
        keyboard.add(group_0)
        add_keyboard_back_button(keyboard)

        bot.send_message(user_id, text=question, reply_markup=keyboard)
    elif year == Y2S_F1:
        keyboard = types.InlineKeyboardMarkup(row_width=1)  # inline keyboard
        group_0 = types.InlineKeyboardButton(text=G0_Y2S_F1, callback_data=G0_Y2S_F1)
        group_1 = types.InlineKeyboardButton(text=G1_Y2S_F1, callback_data=G1_Y2S_F1)
        keyboard.add(group_0, group_1)
        add_keyboard_back_button(keyboard)

        bot.send_message(user_id, text=question, reply_markup=keyboard)
    elif year == Y1S_F2:
        keyboard = types.InlineKeyboardMarkup(row_width=1)  # inline keyboard
        group_0 = types.InlineKeyboardButton(text=G0_Y1S_F2, callback_data=G0_Y1S_F2)
        group_1 = types.InlineKeyboardButton(text=G1_Y2S_F1, callback_data=G1_Y2S_F1)
        keyboard.add(group_0, group_1)
        add_keyboard_back_button(keyboard)

        bot.send_message(user_id, text=question, reply_markup=keyboard)
    elif year == Y3S_F2:
        keyboard = types.InlineKeyboardMarkup(row_width=1)  # inline keyboard
        group_0 = types.InlineKeyboardButton(text=G0_Y3S_F2, callback_data=G0_Y3S_F2)
        keyboard.add(group_0)
        add_keyboard_back_button(keyboard)

        bot.send_message(user_id, text=question, reply_markup=keyboard)
    elif year == Y4S_F2:
        keyboard = types.InlineKeyboardMarkup(row_width=1)  # inline keyboard
        group_0 = types.InlineKeyboardButton(text=G0_Y4S_F2, callback_data=G0_Y4S_F2)
        keyboard.add(group_0)
        add_keyboard_back_button(keyboard)

        bot.send_message(user_id, text=question, reply_markup=keyboard)


def show_menu(user_id, group):
    keyboard = types.InlineKeyboardMarkup(row_width=3)  # inline keyboard

    schedule_today = types.InlineKeyboardButton(text='Today', callback_data='schedule today')
    schedule_tomorrow = types.InlineKeyboardButton(text='Tomorrow', callback_data='schedule tomorrow')
    schedule_week = types.InlineKeyboardButton(text='Week', callback_data='schedule week')
    keyboard.add(schedule_today, schedule_tomorrow, schedule_week)
    add_keyboard_back_button(keyboard)

    question = f'{group} Schedule'
    bot.send_message(user_id, text=question, reply_markup=keyboard)


def choose_year_and_check_form(user_id, form):
    question = form + ' Whats your year?'
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


bot.polling(none_stop=True)
