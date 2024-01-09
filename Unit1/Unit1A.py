import time
import gspread
from telebot import types
from Unit1 import Unit1B
from Token import Token


class Unit1A:
    @staticmethod
    def unit1A():
        @Token.bot.message_handler(func=lambda message: message.text == '📚 Unit 1A' or message.text == '/Unit1A')
        def messages(message):
            markup = types.InlineKeyboardMarkup()
            txt_file_text = ''
            file_name = open('Text/Unit1A.txt', 'r', encoding='utf-8')
            for content in file_name:
                txt_file_text += content
            Token.bot.send_message(message.chat.id, txt_file_text, reply_markup=markup, parse_mode='html')
            time.sleep(0.5)
            file_name.close()


@Token.bot.message_handler(func=lambda message: message.text == '📝 Unit3 1A Quiz' or message.text == '/Unit1A_Quiz')
def test(inner_message):
    score = 0
    chat_id = inner_message.chat.id
    Token.bot.send_message(chat_id=chat_id, text="""
<b>1A MIDDLE NAMES QUIZ</b>


1. Christopher <b>A</b>______ Kutcher
\n1)Ashton\n2)Aslan\n3)Michael""", parse_mode='html')
    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer1(msg, score))


def check_answer1(inner_message, score):
    chat_id = inner_message.chat.id
    if inner_message.content_type == 'text':
        answer = inner_message.text.lower()
        if answer in ["1", "2", "3"]:
            if answer == "1":
                Token.bot.send_message(chat_id=chat_id, text="Correct answer!")
                score += 10

                Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer2(msg, score))
                Token.bot.send_message(chat_id=chat_id, text="""
                2. Laura Jeanne <b>R</b>______ Witherspoon?
                \n1)Ruth\n2)Rene\n3)Reese""", parse_mode='html')
            else:
                Token.bot.send_message(chat_id=chat_id, text="Incorrect answer. Try again.")

                Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer1(msg, score))
        else:
            Token.bot.send_message(chat_id=chat_id, text="Incorrect answer. Enter 1, 2 or 3.")
            Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer1(msg, score))
    else:
        Token.bot.send_message(chat_id=chat_id, text="Invalid message type. Enter a text response.")
        Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer1(msg, score))


def check_answer2(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 10
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer3(msg, score))
    Token.bot.send_message(chat_id=inner_message.chat.id, text="""
3. William <b>B</b>_______ Pitt
\n1)Bobby\n2)Brad\n3) Ben""", parse_mode='html')


def check_answer3(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "2":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 10
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer4(msg, score))
    Token.bot.send_message(chat_id=inner_message.chat.id, text="""
4. David <b>J</b>______ Law
\n1)Jude\n2)Jauden\n3)Jerome""", parse_mode='html')


def check_answer4(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "1":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 10
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer5(msg, score))
    Token.bot.send_message(chat_id=inner_message.chat.id, text="""
5. Hannah <b>D</b>______ Fanning
\n1)Dio\n2)Daisy\n3)Dakota""", parse_mode='html')


def check_answer5(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 10
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer6(msg, score))
    Token.bot.send_message(chat_id=inner_message.chat.id, text="""
6. Walter <b>B</b>______ Willis
\n1)Brad\n2)Bane\n3)Bruce""", parse_mode='html')


def check_answer6(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 10
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer7(msg, score))
    Token.bot.send_message(chat_id=inner_message.chat.id, text="""
7. Thomas <b>S</b>______ Connery
\n1)Sean\n2)Seok\n3)Straizo""", parse_mode='html')


def check_answer7(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "1":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 10
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer8(msg, score))
    Token.bot.send_message(chat_id=inner_message.chat.id, text="""
8. Robyn <b>R</b>______ Fenty
\n1)Ruby\n2)Rihanna\n3)Rizotto""", parse_mode='html')


def check_answer8(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "2":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 10
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer9(msg, score))
    Token.bot.send_message(chat_id=inner_message.chat.id, text="""
9. James <b>H</b>______ Laurie
\n1)Harry\n2)Hol Horse\n3)Hugh Calum""", parse_mode='html')


def check_answer9(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 10
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer10(msg, score))
    Token.bot.send_message(chat_id=inner_message.chat.id, text="""
10. Henry <b>W</b>______ Beatty
\n1)Warden\n2)Warren\n3)William""", parse_mode='html')


def check_answer10(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "2":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 10
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.send_message(chat_id=inner_message.chat.id, text="Your score: {} out of 100".format(score))
    user_id = inner_message.from_user.id
    file_name = 'JSON/englishdatabase-388710-017506ff239d.json'
    gc = gspread.service_account(file_name)
    sh = gc.open_by_key('1VvsHSJy8D2RllLKWwuhwHPI47KMzxOj622899-_NZmw')
    worksheet = sh.sheet1
    user_ids = worksheet.col_values(1)
    row_index = user_ids.index(str(user_id)) + 1
    worksheet.update_cell(row_index, 4, str(score))
    user_first_name = inner_message.from_user.first_name
    user_last_name = inner_message.from_user.last_name

    if user_last_name:
        Token.bot.send_message(chat_id=inner_message.chat.id,
                         text="Rating added for user: {} {}".format(user_first_name, user_last_name))
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id,
                         text="The rating has been added to the user database: {}".format(user_first_name))
    Token.bot.send_message(inner_message.chat.id,
                     text="""
Now let's move on to the next Unit3 by clicking on the button /Unit1B. 

Or to retake the test, click:/Unit1A_Quiz
""")
    if answer == '/Unit1B.':
        Token.bot.register_next_step_handler(inner_message, Unit1B)
