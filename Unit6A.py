from telebot import types
from Token import bot
from Unit6B import Unit6B
import time
import gspread


class Unit6A:
    @staticmethod
    def unit6a():
        @bot.message_handler(func=lambda message: message.text == '📚 Unit 6A' or message.text == '/Unit6A')
        def website(message):
            markup = types.InlineKeyboardMarkup()
            markup.add(
                types.InlineKeyboardButton('Video',
                                           url="https://www.youtube.com/watch?v=Yz4PLILQPTc"))

            mess_1 = """
<b>Unit 6A What the waiter really thinks</b>
"""

            hm_1 = """
Knowing how to tip in restaurants can be a
nightmare, especially on holiday. A waiter tells
you what to do...

Is there anywhere where people never tip?
In Japan. You mustn't do it there. The Japanese

think that tipping someone means treating them
like a servant. The price is the price.

Where should you tip?
Everywhere else. As a waiter, I find it hard to
imagine anyone being upset with extra cash.

You should never feel embarrassed to leave a tip
on the table. In fact, in countries where you don't
have to tip, it's even more appreciated.

Do you need to tip if service is already included?
In countries like France and Australia, service is always
included in the prices. The service charge is often shared
with the kitchen staff as well - which is a good thing, helping
everyone to earn a bit more. When you have to pay a service
charge, of course, you needn't add an extra tip unless you really
want to. If you do tip, check that the money is going to the waiter
and not to the restaurant owner, and if in doubt, leave cash.

How much should you tip? When shouldn’t you tip?

The standard service charge is 12.5% of the bill in Britain, so if The only circumstances when I think you shouldn't
your bill doesn't include service, you should tip about 10% (the _tip are when the service is really really bad, for

USA and Canada are another story ~ there’s no upper limit!). example, if you ask for things that never arrive, or if
But — and this is important — if you're leaving a good tip, don’t staff are extremely unfriendly. But remember that
make a big thing about it and expect the waiter to look at you what many people think of as ‘slow service’ is often

adoringly. Do it discreetly and enjoy the feel-good factor instead. _ more the kitchen’s fault than the waiter’s.
"""

            bot.send_message(message.chat.id, mess_1, reply_markup=markup, parse_mode='html')
            time.sleep(0.5)
            bot.send_message(message.chat.id, hm_1, parse_mode='html')
            time.sleep(0.5)
            bot.send_message(message.chat.id,
                             'Next'
                             '\nPress\n/Unit6B'
                             '\n/Unit6A_Test')
            time.sleep(0.5)


@bot.message_handler(func=lambda message: message.text == '📝 Unit 6A Test' or message.text == '/Unit6A_Test')
def test(inner_message):
    score = 0
    chat_id = inner_message.chat.id
    bot.send_message(chat_id=chat_id,
                     text="1.If it _____ (rain), we will stay indoors."
                          "\n1)rains."
                          "\n2)will rain."
                          "\n3)rained.")

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
                     text="2.If I _____ (study), I will pass the exam."
                          "\n1)study"
                          "\n2)will study"
                          "\n3)studied")


def check_answer2(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "1":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer3(msg, score))
    bot.send_message(chat_id=inner_message.chat.id,
                     text="3.If she _____ (arrive) late, we will start without her."
                          "\n1)arrives"
                          "\n2)will arrive"
                          "\n3)arrived")


def check_answer3(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "1":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer4(msg, score))
    bot.send_message(chat_id=inner_message.chat.id,
                     text="4.If you _____ (call) me, I will answer."
                          "\n1)call"
                          "\n2)will call"
                          "\n3)called")


def check_answer4(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "1":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer5(msg, score))
    bot.send_message(chat_id=inner_message.chat.id,
                     text="5.If they _____ (not hurry), they will miss the train."
                          "\n1)don't hurry"
                          "\n2)won't hurry"
                          "\n3)didn't hurry")


def check_answer5(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "1":
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
    worksheet.update_cell(row_index, 15, str(score))
    user_first_name = inner_message.from_user.first_name
    user_last_name = inner_message.from_user.last_name
    if user_last_name:
        bot.send_message(chat_id=inner_message.chat.id,
                         text="Rating added for user: {} {}".format(user_first_name, user_last_name))
    else:
        bot.send_message(chat_id=inner_message.chat.id,
                         text="Rating added for user: {}".format(user_first_name, ))
    bot.send_message(inner_message.chat.id,
                     text="Next /Unit6B\nOr:/Unit6A_Test to "
                          "try again")
    if answer == '/Unit6B':
        bot.register_next_step_handler(inner_message, Unit6B)
