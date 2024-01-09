from telebot import types
from Token import Token
from Unit2 import Unit2B
import time
import gspread


class Unit2A:
    @staticmethod
    def unit2a():
        @Token.bot.message_handler(func=lambda
                message: message.text == '📚 Unit 2A' or message.text == '/Unit2A')
        def website(message):
            markup = types.InlineKeyboardMarkup()

            mess_1 = """
<b>Unit3 2A Get ready! Get set! Go!</b>
"""

            hm_1 = """
In the USA, children love to take part in various fun competitions. So, they organize races: sack races, three-legged 
races, races with an egg on a spoon. All these competitions are a lot of fun and the kids have a great time together.

In Kazakhstan, children also like to do interesting things in their free time. After school, the children attend clubs 
and sports clubs. There they dance, sing, play football, basketball, etc. Some guys also practice martial arts: judo, karate.
To talk about a hobby in English, use the construction like doing something.

I like swimming. - I like swimming.

The verb like in this construction is in the Present Simple Tense, which means you should not forget to 
add the ending –s if the subject is expressed or it can be replaced with a 3rd person singular pronoun. numbers (he, she, it).

Tom likes playing football. – Tom likes to play football (hobby).

Do not confuse the verb ending – ing in the construction like doing something with the verb in The Present 
Continuous Tense. The verb in this tense expresses an action that is happening now, at the moment of speech, and also 
has an auxiliary verb be (am / is / are).

Tom is playing football now. - Tom is playing football now (action at the time of speech).
"""

            Token.bot.send_message(message.chat.id, mess_1, reply_markup=markup, parse_mode='html')
            time.sleep(0.5)
            Token.bot.send_message(message.chat.id, hm_1, parse_mode='html')
            time.sleep(0.5)
            Token.bot.send_message(message.chat.id,
                                   'Well done, lets move on to the next section Unit3 2B '
                                   '\nClick me\n/Unit2B'
                                   '\nOr lets take the test)'
                                   '\n/Unit2A_Test')
            time.sleep(0.5)


@Token.bot.message_handler(func=lambda message: message.text == '📝 Unit3 2A Test' or message.text == '/Unit2A_Test')
def test(inner_message):
    score = 0
    chat_id = inner_message.chat.id
    Token.bot.send_message(chat_id=chat_id, text="1.What does Tom like to do in his free time?"
                                                 "\n1)Swimming."
                                                 "\n2)Playing football."
                                                 "\n3)Reading books.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer1(msg, score))


def check_answer1(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "2":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer2(msg, score))
    Token.bot.send_message(chat_id=inner_message.chat.id,
                           text="2.Which verb tense is used to talk about a hobby in English?"
                                "\n1)Present Continuous Tense."
                                "\n2)Past Simple Tense."
                                "\n3)Present Simple Tense.")


def check_answer2(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer3(msg, score))
    Token.bot.send_message(chat_id=inner_message.chat.id,
                           text="3.When does the Present Continuous Tense express an action?"
                                "\n1)In the past."
                                "\n2)In the future."
                                "\n3)At the moment of speech.")


def check_answer3(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer4(msg, score))
    Token.bot.send_message(chat_id=inner_message.chat.id,
                           text="4.What are some activities children in the USA enjoy in competitions?"
                                "\n1)Dancing and singing."
                                "\n2)Racing with sacks."
                                "\n3)Martial arts like judo.")


def check_answer4(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "2":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer5(msg, score))
    Token.bot.send_message(chat_id=inner_message.chat.id,
                           text="5.In the sentence 'She likes _______,' which form of the verb should be used if the subject is 'She'?"
                                "\n1)Adding -ing to the verb."
                                "\n2)Adding -ed to the verb."
                                "\n3)Adding -s to the verb.")


def check_answer5(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.send_message(chat_id=inner_message.chat.id, text="Your score: {} out of 5".format(score))
    Token.bot.send_message(chat_id=inner_message.chat.id, text="Mark: {}".format(score))
    user_id = inner_message.from_user.id
    file_name = 'JSON/englishdatabase-388710-017506ff239d.json'
    gc = gspread.service_account(file_name)
    sh = gc.open_by_key('1VvsHSJy8D2RllLKWwuhwHPI47KMzxOj622899-_NZmw')
    worksheet = sh.sheet1
    user_ids = worksheet.col_values(1)
    row_index = user_ids.index(str(user_id)) + 1
    worksheet.update_cell(row_index, 6, str(score))
    user_first_name = inner_message.from_user.first_name
    user_last_name = inner_message.from_user.last_name
    if user_last_name:
        Token.bot.send_message(chat_id=inner_message.chat.id,
                               text="Rating added for user: {} {}".format(user_first_name, user_last_name))
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id,
                               text="Rating added for user: {}".format(user_first_name, ))
    Token.bot.send_message(inner_message.chat.id,
                           text="Next Unit3:/Unit2B\nИли Press:/Unit2A_Test to try again")
    if answer == '/Unit2B':
        Token.bot.register_next_step_handler(inner_message, Unit2B)
