from telebot import types
from Token import bot
from Unit3B import Unit3B
import time
import gspread


class Unit3A:
    @staticmethod
    def unit3a():
        @bot.message_handler(func=lambda
                message: message.text == '📚 Unit 3A' or message.text == '/Unit3A')
        def website(message):
            markup = types.InlineKeyboardMarkup()
            markup.add(
                types.InlineKeyboardButton('Video for this section',
                                           url="https://www.youtube.com/watch?v=lxRwEPvL-mQ"))

            mess_1 = """
<b>Unit 3A Grow up!</b>
"""

            hm_1 = """
So you think you're a grown-up?
Think again.

Are you 29 or alder?
Then you're officially an adult Well done. In a
research study, 29 was the
age at which most people thought they finally felt like
a proper grown-up. But you're a legal adult when
you're 18, so that's about 11
years to live through what psychologists call emerging adulthood, that's the
stage when you don't yet
have children, don't live in your own house, and don't earn enough money tbe
financially independent.
Some people sa that buying
your first house or having your first child represent real adulthood
as these mean you are responsible person. A few years ago,
a bank a survey to find out the top tings that proved you were
grown-up. Number one was having a mortgage and number two
was no longer relying on your parents for money. Other things
Included having a pension plan, doing a weekly food shop, and
getting married. A less obvious sign was owning a vacuum cleaner!
"""

            bot.send_message(message.chat.id, mess_1, reply_markup=markup, parse_mode='html')
            time.sleep(0.5)
            bot.send_message(message.chat.id, hm_1, parse_mode='html')
            time.sleep(0.5)
            bot.send_message(message.chat.id,
                             "Well done, let's move on to the next section Unit 3B"
                             '\nPress\n/Unit3B'
                             '\nOr Test'
                             '\n/Unit3A_Test')
            time.sleep(0.5)


@bot.message_handler(func=lambda message: message.text == '📝 Unit 3A Test' or message.text == '/Unit3A_Test')
def test(inner_message):
    score = 0
    chat_id = inner_message.chat.id
    bot.send_message(chat_id=chat_id,
                     text="1.Choose the correct word order for forming a question:\n'You like pizza.'"
                          "\n1)Do you like pizza?."
                          "\n2)Like you pizza?."
                          "\n3)You like pizza?.")

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
                     text="2.Choose the correct word order for forming a question:"
                          "\n'She is going to the store.'"
                          "\n1)Going she to the store?"
                          "\n2)Is she going to the store?"
                          "\n3)She is going to the store?")


def check_answer2(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "1":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer3(msg, score))
    bot.send_message(chat_id=inner_message.chat.id,
                     text="3.Choose the correct word order for forming a question:"
                          "\n'They have visited Paris before.'"
                          "\n1)Have they visited Paris before?"
                          "\n2)They have visited Paris before?"
                          "\n3)Visited they have Paris before?")


def check_answer3(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "2":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer4(msg, score))
    bot.send_message(chat_id=inner_message.chat.id,
                     text="4.Choose the correct word order for forming a question:"
                          "\n'He will be at the party.'"
                          "\n1)Will be he at the party?"
                          "\n2)He will be at the party?"
                          "\n3)Be he will at the party?")


def check_answer4(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "1":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer5(msg, score))
    bot.send_message(chat_id=inner_message.chat.id,
                     text="5.Choose the correct word order for forming a question:"
                          "\n'We can go to the beach.'"
                          "\n1)Can we go to the beach?"
                          "\n2)We can go to the beach?"
                          "\n3)Go we can to the beach?")


def check_answer5(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "1":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.send_message(chat_id=inner_message.chat.id, text="Your score: {} out of 5".format(score))
    bot.send_message(chat_id=inner_message.chat.id, text="Mark: {}".format(score))
    user_id = inner_message.from_user.id
    gc = gspread.service_account(filename='englishdatabase-388710-017506ff239d.json')
    sh = gc.open_by_key('1VvsHSJy8D2RllLKWwuhwHPI47KMzxOj622899-_NZmw')
    worksheet = sh.sheet1
    user_ids = worksheet.col_values(1)
    row_index = user_ids.index(str(user_id)) + 1
    worksheet.update_cell(row_index, 8, str(score))
    user_first_name = inner_message.from_user.first_name
    user_last_name = inner_message.from_user.last_name
    if user_last_name:
        bot.send_message(chat_id=inner_message.chat.id,
                         text="Rating added for user: {} {}".format(user_first_name, user_last_name))
    else:
        bot.send_message(chat_id=inner_message.chat.id,
                         text="Rating added for user: {}".format(user_first_name, ))
    bot.send_message(inner_message.chat.id,
                     text="Next Unit:/Unit3B\nOr Press:/Unit3A_Test to try again")
    if answer == '/Unit3B':
        bot.register_next_step_handler(inner_message, Unit3B)
