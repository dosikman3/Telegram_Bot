from telebot import types
from Token import Token
from Practical import Practical_English
import time
import gspread


class Unit3B:
    @staticmethod
    def unit3b():
        @Token.bot.message_handler(
            func=lambda message: message.text == '📚 Unit 3B' or message.text == '/Unit3B')
        def website(message):
            markup = types.InlineKeyboardMarkup()

            mess_1 = """
<b>Unit3 3B Photo albums</b>
"""

            hm_1 = """
Although it is still a good idea to keep all of your photos as digital

In the past, your grandmother probably kept her photos ina box,
or in an old album, and sadly, over time, these memories faded

or disappeared. But with today's technology, that shouldn't be a
problem. A digital photo lasts forever, right? Actually, think ag

computer files, there are plenty of things that can damage or even
destroy those high-tech memories.

1

Very few people realize this can happen, but if you store your
photos as .jpgs (the most common file format), the file will actually
deteriorate every time you copy and edit it. Experts disagree
about how much damage this can do, but the damage is real.

2 5
Your files may be safe on your hard drive, but how long until your hard Websites like Flickr and Instagram let you quickly
drive dies? The average lasts just five years. You could back up your upload photos and share them with others. But bear
photos on a CD-ROM or flash drive, but they don't last forever either 30 in mind that a photo site which is popular now could
—about 10-20 years at most, experts say. one day go out of business, taking your photos with

it. What's more, if you upload photos to these sites,

3 there is someone other than you who controls your
Let's say all goes well and your CD-ROM or flash drive full of photos _ access. While itis generally not in their interest
lasts for 20 years. By then, will there still be any CD-ROM drives in 5 to stop you accessing your files, they can and
the world that can read the disc? Will you be able to insert your flash Sometimes do. They can even cancel your account.
drive into a modern computer? Today's high-tech storage solution is So what should you do? Experts say you should
tomorrow's useless floppy disk, make lots of copies of your photos and save them

a in many different ways — on your computer, on

40 a back-up drive, online, and even as traditional

People talk about saving their photos in a magical place on the printed photos. It may be too late to save
internet, like Apple's iCloud, or Dropbox. But this just means they Grandma’s photos, but you can still save yours.

are in a company's data centre on ~ guess what? — lots of hard
drives, which could die or corrupt just as easily as your own. During
a thunderstorm, a cloud storage centre in the USA was hit, and
major sites like Netflix, Pinterest, and Instagram went offline for
almost a whole day. Thousands of files were lost.
"""
            time.sleep(0.5)
            Token.bot.send_message(message.chat.id, mess_1, reply_markup=markup, parse_mode='html')
            time.sleep(0.5)
            Token.bot.send_message(message.chat.id, hm_1, parse_mode='html')
            time.sleep(0.5)
            Token.bot.send_message(message.chat.id,
                             'Next Unit3 is a Practical '
                             '\nPress\n/Practical'
                             '\n/Unit3B_Test')
            time.sleep(0.5)


@Token.bot.message_handler(func=lambda message: message.text == '📝 Unit3 3B Test' or message.text == '/Unit3B_Test')
def test(inner_message):
    score = 0
    chat_id = inner_message.chat.id
    Token.bot.send_message(chat_id=chat_id,
                     text="1.Which type of question requires a 'yes' or 'no' answer?"
                          "\n1)Wh-questions."
                          "\n2)Choice questions."
                          "\n3)Polar questions.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer1(msg, score))


def check_answer1(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer2(msg, score))
    Token.bot.send_message(chat_id=inner_message.chat.id,
                     text="2.Choose the correct type of question for the following sentence:"
                          "\n'Where did you go on vacation?'"
                          "\n1)Wh-questions"
                          "\n2)Tag questions"
                          "\n3)Alternative questions")


def check_answer2(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "1":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer3(msg, score))
    Token.bot.send_message(chat_id=inner_message.chat.id,
                     text="3.Which type of question offers a choice between two or more options?"
                          "\n1)Wh-questions"
                          "\n2)Tag questions"
                          "\n3)Alternative questions")


def check_answer3(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer4(msg, score))
    Token.bot.send_message(chat_id=inner_message.chat.id,
                     text="4.Choose the correct type of question for the following sentence:"
                          "\n'Isn't it a beautiful day?'"
                          "\n1)Wh-questions"
                          "\n2)Tag questions"
                          "\n3)Alternative questions")


def check_answer4(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "2":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer5(msg, score))
    Token.bot.send_message(chat_id=inner_message.chat.id,
                     text="5.Which type of question requests specific information?"
                          "\n1)Wh-questions"
                          "\n2)Tag questions"
                          "\n3)Polar questions")


def check_answer5(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "1":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.send_message(chat_id=inner_message.chat.id, text="Your score: {} из 5".format(score))
    Token.bot.send_message(chat_id=inner_message.chat.id, text="Mark: {}".format(score))
    user_id = inner_message.from_user.id
    file_name = 'JSON/englishdatabase-388710-017506ff239d.json'
    gc = gspread.service_account(file_name)
    sh = gc.open_by_key('1VvsHSJy8D2RllLKWwuhwHPI47KMzxOj622899-_NZmw')
    worksheet = sh.sheet1
    user_ids = worksheet.col_values(1)
    row_index = user_ids.index(str(user_id)) + 1
    worksheet.update_cell(row_index, 9, str(score))
    user_first_name = inner_message.from_user.first_name
    user_last_name = inner_message.from_user.last_name
    if user_last_name:
        Token.bot.send_message(chat_id=inner_message.chat.id,
                         text="Rating added for user: {} {}".format(user_first_name, user_last_name))
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id,
                         text="Rating added for user: {}".format(user_first_name, ))
    Token.bot.send_message(inner_message.chat.id,
                     text="Next Unit3 /Practical\nOr"
                          "Press:/Unit3B_Test to"
                          "try again")
    if answer == '/Practical':
        Token.bot.register_next_step_handler(inner_message, Practical_English)
