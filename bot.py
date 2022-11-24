import telebot
import config
import random
import json

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


# alert
#     # # remove inline buttons
#     # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Whats your group ?",
#     # reply_markup=None)

#     # show alert
#     bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
#         text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")

# user_key_id = 'ssss'
# chosen_year = '2'
# chosen_group = 'group23_4'





@bot.message_handler(content_types=['text'])
def all_years(message):
    # 0. get user key id
    user_key_id = str(message.chat.id)

    # 1. load entire file
    with open('C:/Users/fairv/Documents/bot/mybot/users.txt') as fi:
        di = json.load(fi)

    for key, value in di.items():
        # 2a. check if user exists in base
        if key == user_key_id:
        # then load menu

            print("show menu")
        
        # 2b. if no user then make one 
        else:
            # year -> group -> rembers you if u werent rembered AND
                
            # reg = append dict
            print("Register")
            # reg menu

            # choose year 
            # choose group
            di[user_key_id] = []
            di[user_key_id].append({
            'year': chosen_year,
            'group': chosen_group
            })

            # send to file
            with open('C:/Users/fairv/Documents/bot/mybot/users.txt', 'w') as f:
                json.dump(di, f)


        # after any choices shows you menu 
                # choose another group
                # Schedule for today
                # tomorrow
                # week

    





@bot.callback_query_handler(func=lambda call: True)
def your_group(call, message=None):
    # try:
        if call.message:
            question = 'Whats your group ?'

            if call.data == "menu": #call.data это callback_data, которую мы указали при объявлении кнопки
                keyboard = types.InlineKeyboardMarkup(row_width=3) # inline keyboard

                year_1 = types.InlineKeyboardButton(text='1', callback_data='year1')
                year_2 = types.InlineKeyboardButton(text='2', callback_data='year2')
                year_3 = types.InlineKeyboardButton(text='3', callback_data='year3')
                keyboard.add(year_1, year_2, year_3)

                year_1_spo = types.InlineKeyboardButton(text='1spo', callback_data='year1spo')
                year_2_spo = types.InlineKeyboardButton(text='2spo', callback_data='year2spo')
                year_3_spo = types.InlineKeyboardButton(text='3spo', callback_data='year3spo')
                keyboard.add(year_1_spo, year_2_spo, year_3_spo)

                year_4 = types.InlineKeyboardButton(text='4', callback_data='year4')
                keyboard.add(year_4)

                question = 'Whats your year ?'
                bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

            elif call.data == "year1": 
                chosen_year = 'year1'
                # groups here
            elif call.data == "year2":
                chosen_year = 'year2'
                keyboard = types.InlineKeyboardMarkup(row_width=1)
                group_23_1 = types.InlineKeyboardButton(text='о. ИД 23.1/Б-21', callback_data='group23_1')
                group_23_2 = types.InlineKeyboardButton(text='о. ИД 23.2/Б-21', callback_data='group23_2')
                group_23_3 = types.InlineKeyboardButton(text='о. ИД 23.3/Б-21', callback_data='group23_3')
                group_23_4 = types.InlineKeyboardButton(text='о. ИД 23.4/Б-21', callback_data='group23_4')
                keyboard.add(group_23_1, group_23_2, group_23_3, group_23_4)
                bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
            elif call.data == "year3":
                chosen_year = 'year3'
                bot.send_message(call.message.chat.id, 'Your year is 3 ?')
            elif call.data == "year4":
                chosen_year = 'year4'
                bot.send_message(call.message.chat.id, 'Your year is 4 ?')

            elif call.data == "year1spo":
                chosen_year = 'year1spo'
                bot.send_message(call.message.chat.id, 'Your year is 1spo ?')
            elif call.data == "year2spo":
                chosen_year = 'year2spo'
                bot.send_message(call.message.chat.id, 'Your year is 2spo ?')
            elif call.data == "year3spo":
                chosen_year = 'year3spo'
                bot.send_message(call.message.chat.id, 'Your year is 3spo ?')
        



            elif call.data == "group23_1": 
                chosen_group = 'group23_1'
                bot.send_message(call.message.chat.id, 'You have been saved as member of 23_1')
            elif call.data == "group23_2":
                chosen_group = 'group23_2'
                bot.send_message(call.message.chat.id, 'You have been saved as member of 23_2')
            elif call.data == "group23_3":
                chosen_group = 'group23_3'
                bot.send_message(call.message.chat.id, 'You have been saved as member of 23_3')
            elif call.data == "group23_4":
                
                chosen_group = 'group23_4'
                bot.send_message(call.message.chat.id, 'You have been saved as member of 23_4')
                # save user choice 


                # load user choice
                # menu
                
                keyboard = types.InlineKeyboardMarkup(row_width=3) # inline keyboard
   
                schedule_today = types.InlineKeyboardButton(text='Today', callback_data='scheduletoday')
                schedule_tomorrow = types.InlineKeyboardButton(text='Tomorrow', callback_data='scheduletomorrow')
                schedule_week = types.InlineKeyboardButton(text='Week', callback_data='scheduleweek')

                switch_group = types.InlineKeyboardButton(text='choose another group', callback_data='switchgroup')

                keyboard.add(schedule_today, schedule_tomorrow, schedule_week, switch_group)

                question = '23.4 Schedule'
                bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
                
            elif call.data == "scheduletoday":
                bot.send_message(call.message.chat.id, 'Schedule for today:')
            elif call.data == "scheduletomorrow": 
                bot.send_message(call.message.chat.id, 'Schedule for tomorrow:')
            elif call.data == "scheduleweek":
                bot.send_message(call.message.chat.id, 'Schedule for week:')
            elif call.data == "switchgroup":
                # load last entered year

                bot.send_message(call.message.chat.id, 'Choose your group')

 
    # except Exception as e:
    #     print(repr(e))

bot.polling(none_stop=True)
