from telebot import types
from Token import bot
from Unit4A import Unit4A
import time
import gspread


class Practical:
    @staticmethod
    def practical():
        @bot.message_handler(func=lambda
                message: message.text == '📚 Practical English' or message.text == '/Practical')
        def website(message):
            markup = types.InlineKeyboardMarkup()
            markup.add(
                types.InlineKeyboardButton('Video',
                                           url="https://www.youtube.com/watch?v=R3n1UDZ0jmU"))

            mess_1 = """
<b>Practical English</b>
"""

            bot.send_message(message.chat.id, mess_1, reply_markup=markup, parse_mode='html')
            time.sleep(0.5)
            bot.send_message(message.chat.id,
                             'Well done next Unit '
                             '\nPress \n/Unit4A'
                             '\n/Practical_Test')
            time.sleep(0.5)


@bot.message_handler(func=lambda
        message: message.text == '📝 Practical English Test' or message.text == '/Practical_Test')
def test(inner_message):
    score = 0
    chat_id = inner_message.chat.id
    bot.send_message(chat_id=chat_id,
                     text="1.Choose the correct comparative form of the adjective 'big':"
                          "\n1)biggier."
                          "\n2)bigger."
                          "\n3)biger.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer1(msg, score))


def check_answer1(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "2":
        bot.send_message(chat_id=inner_message.chat.id, text="Верно!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Неверно.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer2(msg, score))
    bot.send_message(chat_id=inner_message.chat.id,
                     text="2.Choose the correct superlative form of the adjective 'good':"
                          "\n1)gooder"
                          "\n2)goodest"
                          "\n3)best")


def check_answer2(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
        bot.send_message(chat_id=inner_message.chat.id, text="Верно!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Неверно.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer3(msg, score))
    bot.send_message(chat_id=inner_message.chat.id,
                     text="3.Which sentence uses the correct comparative degree?"
                          "\n1)She is the tallest girl in the class."
                          "\n2)She is taller girl in the class."
                          "\n3)She is tallest girl in the class.")


def check_answer3(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "1":
        bot.send_message(chat_id=inner_message.chat.id, text="Верно!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Неверно.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer4(msg, score))
    bot.send_message(chat_id=inner_message.chat.id,
                     text="4.Choose the correct superlative form of the adjective 'bad':"
                          "\n1)baddest"
                          "\n2)worser"
                          "\n3)worst")


def check_answer4(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
        bot.send_message(chat_id=inner_message.chat.id, text="Верно!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Неверно.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer5(msg, score))
    bot.send_message(chat_id=inner_message.chat.id,
                     text="5.Which sentence uses the correct comparative degree?"
                          "\n1)This book is interesting than the one I read before."
                          "\n2)This book is more interesting than the one I read before."
                          "\n3)This book is interestinger than the one I read before.")


def check_answer5(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "2":
        bot.send_message(chat_id=inner_message.chat.id, text="Верно!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Неверно.")

    bot.send_message(chat_id=inner_message.chat.id, text="Ваш результат теста: {} из 5".format(score))
    bot.send_message(chat_id=inner_message.chat.id, text="Ваша оценка: {}".format(score))
    user_id = inner_message.from_user.id
    gc = gspread.service_account(filename='englishdatabase-388710-017506ff239d.json')
    sh = gc.open_by_key('1VvsHSJy8D2RllLKWwuhwHPI47KMzxOj622899-_NZmw')
    worksheet = sh.sheet1
    user_ids = worksheet.col_values(1)
    row_index = user_ids.index(str(user_id)) + 1
    worksheet.update_cell(row_index, 10, str(score))
    user_first_name = inner_message.from_user.first_name
    user_last_name = inner_message.from_user.last_name
    if user_last_name:
        bot.send_message(chat_id=inner_message.chat.id,
                         text="Оценка добавлена для пользователя: {} {}".format(user_first_name,
                                                                                user_last_name))
    else:
        bot.send_message(chat_id=inner_message.chat.id,
                         text="Оценка добавлена для пользователя: {}".format(user_first_name, ))
    bot.send_message(inner_message.chat.id,
                     text="Next Unit:/Unit4A\nOr:/Practical_Test to"
                          "try again")
    if answer == '/Unit4A':
        bot.register_next_step_handler(inner_message, Unit4A)
