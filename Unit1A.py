from telebot import types

from Unit1B import Unit1B
from Token import bot
import time
import gspread


class Unit1A:
    @staticmethod
    def unit1A():
        @bot.message_handler(func=lambda message: message.text == '📚 Unit 1A' or message.text == '/Unit1A')
        def website(message):
            markup = types.InlineKeyboardMarkup()
            mess_1 = """
<b>Unit 1A Why did they call you that</b>
            
<b>VOCABULARY</b> names

Read about the people and match photos A-H to the texts. Compare with a partner and together, work out the meaning of
the <b>bold</b> words and phrases
"""
            mess_2 = """
<b>Tell a partner about someone you know who...</b>

• has a nickname.                  
• is called something for short.
• is named after a place           
• has a very old-fashioned name
• is named after a famous          
• has changed his / her name
  person.
"""
            mess_3 = """
<b>PRONUNCIATION</b>
vowel sounds
Look at the first names in the chart.
Listen and write on your notebook the name which doesn't
have the sound in the picture.
"""
            mess_4 = """
<b>READING</b>
<b>a</b> With a partner, guess which countries or regions these name are from. Do you think they are first names or surnames?

<b>Yeon Seok</b>
<b>Rakhmaninov</b>
<b>Lopez Ramirez</b>
<b>Aarushi</b>
<b>Li</b>
<b>Abdul Ahad</b>
<b>Jones</b>

<b>b</b> Read the article and check your answers to <b>a</b>. Are the first names from the list male or female?

<b>c</b> Read the article again. In which country or countries...?

1 does the surname come before the first name
2 do people have no surname
3 do people have more than one surname
4 do people have a middle name connected to their father's name
5 do some people stop using the surname they were born with
6 are people given names depending on when they were born

<b>d</b> What is the naming custom in your country? Has it changed over the years? Do you think it ought to change?
"""

            mess_5 = """
<b>GRAMMAR</b> pronouns
<b>a</b> Talk to a partner. What are the two most popular brand names in your country for phones, sportswear, and cars?
Do you know what country the brands are from, or what the names mean?

<b>b</b> Read about how the Kindle got its name. Do you think it's a good name? Why(not)?
<b>c</b> Read the text again. With a partner, say what the <b>highlighted</b> pronouns refer to.            
"""

            hm = """
Great, I hope you read everything and completed the assignments, we can move on to the next unit /Unit2B
Or we’ll take a short Quiz on the topic to get grades
/Unit1A_Quiz

Remember to enter only numbers, otherwise the answer will be considered incorrect!
"""
            bot.send_message(message.chat.id, mess_1, reply_markup=markup, parse_mode='html')
            # with open('C:/Users/Dastan Yeluybay/PycharmProjects/Telegram_Bot/image/Unit1A/Unit1A_img1.PNG', 'rb') as img:
            #     bot.send_photo(message.chat.id, img)
            # time.sleep(0.5)
            bot.send_message(message.chat.id, mess_2, parse_mode='html')
            time.sleep(0.5)
            bot.send_message(message.chat.id, mess_3, parse_mode='html')
            # with open('C:/Users/Dastan Yeluybay/PycharmProjects/Telegram_Bot/image/Unit1A/Unit1A_img2.PNG', 'rb') as img:
            #     bot.send_photo(message.chat.id, img)
            # time.sleep(0.5)
            bot.send_message(message.chat.id, mess_4, parse_mode='html')
            # with open('C:/Users/Dastan Yeluybay/PycharmProjects/Telegram_Bot/image/Unit1A/Unit1A_img3.PNG', 'rb') as img:
            #     bot.send_photo(message.chat.id, img)
            # time.sleep(0.5)
            bot.send_message(message.chat.id, mess_5, parse_mode='html')
            # with open('C:/Users/Dastan Yeluybay/PycharmProjects/Telegram_Bot/image/Unit1A/Unit1A_img4.PNG',
            #           'rb') as img:
            #     bot.send_photo(message.chat.id, img)
            time.sleep(0.5)
            bot.send_message(message.chat.id, hm, parse_mode='html')
            time.sleep(0.5)


@bot.message_handler(func=lambda message: message.text == '📝 Unit 1A Quiz' or message.text == '/Unit1A_Quiz')
def test(inner_message):
    score = 0
    chat_id = inner_message.chat.id
    bot.send_message(chat_id=chat_id, text="""
<b>1A MIDDLE NAMES QUIZ</b>


1. Christopher <b>A</b>______ Kutcher
\n1)Ashton\n2)Aslan\n3)Michael""", parse_mode='html')
    # with open('C:/Users/Dastan Yeluybay/PycharmProjects/Telegram_Bot/image/Unit1A/Unit1A_Quiz/Name_1.1.jpeg',
    #           'rb') as img:
    #     bot.send_photo(chat_id, img)
    bot.register_next_step_handler(inner_message, lambda msg: check_answer1(msg, score))


def check_answer1(inner_message, score):
    chat_id = inner_message.chat.id
    if inner_message.content_type == 'text':
        answer = inner_message.text.lower()
        if answer in ["1", "2", "3"]:
            if answer == "1":
                bot.send_message(chat_id=chat_id, text="Correct answer!")
                score += 10

                bot.register_next_step_handler(inner_message, lambda msg: check_answer2(msg, score))
                bot.send_message(chat_id=chat_id, text="""
                2. Laura Jeanne <b>R</b>______ Witherspoon?
                \n1)Ruth\n2)Rene\n3)Reese""", parse_mode='html')
                # with open(
                #         'C:/Users/Dastan Yeluybay/PycharmProjects/Telegram_Bot/image/Unit1A/Unit1A_Quiz/Name_1.2.jpg',
                #         'rb') as img:
                #     bot.send_photo(chat_id, img)
            else:
                bot.send_message(chat_id=chat_id, text="Incorrect answer. Try again.")

                bot.register_next_step_handler(inner_message, lambda msg: check_answer1(msg, score))
        else:
            bot.send_message(chat_id=chat_id, text="Incorrect answer. Enter 1, 2 or 3.")
            bot.register_next_step_handler(inner_message, lambda msg: check_answer1(msg, score))
    else:
        bot.send_message(chat_id=chat_id, text="Invalid message type. Enter a text response.")
        bot.register_next_step_handler(inner_message, lambda msg: check_answer1(msg, score))


def check_answer2(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 10
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer3(msg, score))
    bot.send_message(chat_id=inner_message.chat.id, text="""
3. William <b>B</b>_______ Pitt
\n1)Bobby\n2)Brad\n3) Ben""", parse_mode='html')
    # with open(
    #         'C:/Users/Dastan Yeluybay/PycharmProjects/Telegram_Bot/image/Unit1A/Unit1A_Quiz/Name_1.3.jpg',
    #         'rb') as img:
    #     bot.send_photo(chat_id, img)


def check_answer3(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "2":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 10
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer4(msg, score))
    bot.send_message(chat_id=inner_message.chat.id, text="""
4. David <b>J</b>______ Law
\n1)Jude\n2)Jauden\n3)Jerome""", parse_mode='html')
    # with open(
    #         'C:/Users/Dastan Yeluybay/PycharmProjects/Telegram_Bot/image/Unit1A/Unit1A_Quiz/Name_1.4.jpg',
    #         'rb') as img:
    #     bot.send_photo(chat_id, img)


def check_answer4(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "1":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 10
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer5(msg, score))
    bot.send_message(chat_id=inner_message.chat.id, text="""
5. Hannah <b>D</b>______ Fanning
\n1)Dio\n2)Daisy\n3)Dakota""", parse_mode='html')
    # with open(
    #         'C:/Users/Dastan Yeluybay/PycharmProjects/Telegram_Bot/image/Unit1A/Unit1A_Quiz/Name_1.5.jpg',
    #         'rb') as img:
    #     bot.send_photo(chat_id, img)


def check_answer5(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 10
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer6(msg, score))
    bot.send_message(chat_id=inner_message.chat.id, text="""
6. Walter <b>B</b>______ Willis
\n1)Brad\n2)Bane\n3)Bruce""", parse_mode='html')
    # with open(
    #         'C:/Users/Dastan Yeluybay/PycharmProjects/Telegram_Bot/image/Unit1A/Unit1A_Quiz/Name_1.6.jpg',
    #         'rb') as img:
    #     bot.send_photo(chat_id, img)


def check_answer6(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 10
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer7(msg, score))
    bot.send_message(chat_id=inner_message.chat.id, text="""
7. Thomas <b>S</b>______ Connery
\n1)Sean\n2)Seok\n3)Straizo""", parse_mode='html')
    # with open(
    #         'C:/Users/Dastan Yeluybay/PycharmProjects/Telegram_Bot/image/Unit1A/Unit1A_Quiz/Name_1.7.jpg',
    #         'rb') as img:
    #     bot.send_photo(chat_id, img)


def check_answer7(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "1":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 10
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer8(msg, score))
    bot.send_message(chat_id=inner_message.chat.id, text="""
8. Robyn <b>R</b>______ Fenty
\n1)Ruby\n2)Rihanna\n3)Rizotto""", parse_mode='html')
    # with open(
    #         'C:/Users/Dastan Yeluybay/PycharmProjects/Telegram_Bot/image/Unit1A/Unit1A_Quiz/Name_1.8.png',
    #         'rb') as img:
    #     bot.send_photo(chat_id, img)


def check_answer8(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "2":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 10
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer9(msg, score))
    bot.send_message(chat_id=inner_message.chat.id, text="""
9. James <b>H</b>______ Laurie
\n1)Harry\n2)Hol Horse\n3)Hugh Calum""", parse_mode='html')
    # with open(
    #         'C:/Users/Dastan Yeluybay/PycharmProjects/Telegram_Bot/image/Unit1A/Unit1A_Quiz/Name_1.9.png',
    #         'rb') as img:
    #     bot.send_photo(chat_id, img)


def check_answer9(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 10
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer10(msg, score))
    bot.send_message(chat_id=inner_message.chat.id, text="""
10. Henry <b>W</b>______ Beatty
\n1)Warden\n2)Warren\n3)William""", parse_mode='html')
    # with open(
    #         'C:/Users/Dastan Yeluybay/PycharmProjects/Telegram_Bot/image/Unit1A/Unit1A_Quiz/Name_1.10.jpg',
    #         'rb') as img:
    #     bot.send_photo(chat_id, img)


def check_answer10(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "2":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 10
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.send_message(chat_id=inner_message.chat.id, text="Your score: {} out of 100".format(score))
    user_id = inner_message.from_user.id
    gc = gspread.service_account(filename='englishdatabase-388710-017506ff239d.json')
    sh = gc.open_by_key('1VvsHSJy8D2RllLKWwuhwHPI47KMzxOj622899-_NZmw')
    worksheet = sh.sheet1
    user_ids = worksheet.col_values(1)
    row_index = user_ids.index(str(user_id)) + 1
    worksheet.update_cell(row_index, 4, str(score))
    user_first_name = inner_message.from_user.first_name
    user_last_name = inner_message.from_user.last_name

    if user_last_name:
        bot.send_message(chat_id=inner_message.chat.id,
                         text="Rating added for user: {} {}".format(user_first_name, user_last_name))
    else:
        bot.send_message(chat_id=inner_message.chat.id,
                         text="The rating has been added to the user database: {}".format(user_first_name))
    bot.send_message(inner_message.chat.id,
                     text="""
Now let's move on to the next Unit by clicking on the button /Unit1B. 

Or to retake the test, click:/Unit1A_Quiz
""")
    if answer == '/Unit1B.':
        bot.register_next_step_handler(inner_message, Unit1B)
