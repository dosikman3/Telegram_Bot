from telebot import types
from Token import bot
from Unit6A import Unit6A
import time
import gspread


class Unit5B:
    @staticmethod
    def unit5b():
        @bot.message_handler(func=lambda message: message.text == '📚 Unit 5B' or message.text == '/Unit5B')
        def website(message):
            markup = types.InlineKeyboardMarkup()
            markup.add(
                types.InlineKeyboardButton('Video',
                                           url="https://www.youtube.com/watch?v=p-bQ3pyINZg"))

            mess_1 = """
<b>Unit 5B A quit life?</b>
"""

            hm_1 = """
FROM THE CITY TO THE

AND SOMETIMES BACK AGAIN

I was just divorced, and bored with my easy, if super-busy,
London life. I wanted to live somewhere quieter, simpler, more
beautiful, so I sold my house and bought a big farmhouse

with 50 acres of land. I'll look after horses, I thought. I'll get a
dog. I'll grow all my own food. It will be idyllic and friends will
come to stay and tell me how lucky I am to live here.

BOB AYE!

My wife, Jean, and I had lived in London for years, and we both
worked right in the city centre. I was a police inspector and
Jean was a police dog handler. We enjoyed our jobs, but it was
pretty stressful, dealing with accidents, drugs, shootings, and
so on. We'd often talked about moving out of London, and we'd
had holidays in the country, so we thought we knew what living
in the country would be like. Ten years ago, we bought a house
in a village in Dorset, with a huge garden.
"""

            time.sleep(0.5)
            bot.send_message(message.chat.id, mess_1, reply_markup=markup, parse_mode='html')
            time.sleep(0.5)
            bot.send_message(message.chat.id, hm_1, parse_mode='html')
            time.sleep(0.5)

            bot.send_message(message.chat.id,
                             'Next'
                             '\nPress\n/Unit6A'
                             '\n/Unit6A_Test')
            time.sleep(0.5)


@bot.message_handler(func=lambda message: message.text == '📝 Unit 5B Test' or message.text == '/Unit5B_Test')
def test(inner_message):
    score = 0
    chat_id = inner_message.chat.id
    bot.send_message(chat_id=chat_id,
                     text="1.They will meet _____ the park."
                          "\n1)at."
                          "\n2)in."
                          "\n3)on.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer1(msg, score))


def check_answer1(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "1":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer2(msg, score))
    bot.send_message(chat_id=inner_message.chat.id,
                     text="2.The concert starts _____ 8 p.m."
                          "\n1)at"
                          "\n2)in"
                          "\n3)on")


def check_answer2(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer3(msg, score))
    bot.send_message(chat_id=inner_message.chat.id,
                     text="3.She usually goes to the gym _____ the morning."
                          "\n1)at"
                          "\n2)in"
                          "\n3)on")


def check_answer3(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "2":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer4(msg, score))
    bot.send_message(chat_id=inner_message.chat.id,
                     text="4.The party will take place _____ Saturday."
                          "\n1)at"
                          "\n2)in"
                          "\n3)on")


def check_answer4(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer5(msg, score))
    bot.send_message(chat_id=inner_message.chat.id,
                     text="5.He will be back _____ a few minutes."
                          "\n1)at"
                          "\n2)in"
                          "\n3)on")


def check_answer5(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "2":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.send_message(chat_id=inner_message.chat.id, text="Result: {} из 5".format(score))
    bot.send_message(chat_id=inner_message.chat.id, text="Mark: {}".format(score))
    user_id = inner_message.from_user.id
    gc = gspread.service_account(filename='englishdatabase-388710-017506ff239d.json')
    sh = gc.open_by_key('1VvsHSJy8D2RllLKWwuhwHPI47KMzxOj622899-_NZmw')
    worksheet = sh.sheet1
    user_ids = worksheet.col_values(1)
    row_index = user_ids.index(str(user_id)) + 1
    worksheet.update_cell(row_index, 14, str(score))
    user_first_name = inner_message.from_user.first_name
    user_last_name = inner_message.from_user.last_name
    if user_last_name:
        bot.send_message(chat_id=inner_message.chat.id,
                         text="Rating added for user: {} {}".format(user_first_name, user_last_name))
    else:
        bot.send_message(chat_id=inner_message.chat.id,
                         text="Rating added for user: {}".format(user_first_name, ))
    bot.send_message(inner_message.chat.id,
                     text="Next:/Unit6A\nOr:/Unit5B_Test to "
                          "try again")
    if answer == '/Unit6A':
        bot.register_next_step_handler(inner_message, Unit6A)
