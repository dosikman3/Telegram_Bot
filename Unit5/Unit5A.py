from telebot import types
from Token import Token
from Unit5 import Unit5B
import time
import gspread


class Unit5A:
    @staticmethod
    def unit5a():
        @Token.bot.message_handler(func=lambda message: message.text == '📚 Unit 5A' or message.text == '/Unit5A')
        def website(message):
            markup = types.InlineKeyboardMarkup()
            markup.add(
                types.InlineKeyboardButton('Video',
                                           url="https://www.youtube.com/watch?v=fVALeerZpd4"))

            mess_1 = """
<b>Unit3 5A Screen time</b>
"""

            hm_1 = """
A few years ago, if you’d mentioned to a British
At or colleague that you were addicted to a

Danish drama series, people would have thought
you were a bit strange. But in the UK today, subtitled

foreign-language dramas aren’t just in fashion, they’re
completely mainstream.

It all began when the BBC bought the French crime drama Spiral,
though it was Denmark’s The Killing that was the tipping point.

‘I remember hearing people talking about it on the bus,’ admits Sue
Deeks, Head of Programming at the BBC. ‘It was clearly growing and
growing in popularity, but the extent of it took everyone by surprise.’
The killing was followed by The Bridge, in which a crime is committed
on the bridge between Denmark and Sweden, which regularly topped
a million viewers. The British were hooked.

One of the reasons for the success of foreign TV is that it is more
accessible than it used to be, thanks to catch-up and online services.
And if you haven’t watched the latest foreign series that everybody is
talking about, you can binge watch the episodes that you’ve missed,
and tweet about how much you love The Returned.

There may be something else in foreign

TV’s new popularity, too. In a world ‘When you read
in which we're frequently distracted subtitles, you

from our TV viewing by Twitter and have to be glued
WhatsApp, subtitles force us to focus. to the screen’
“When you read subtitles, you have

to be glued to the screen, says Deeks. “That concentration gives a
particular intensity to the viewing experience. You just can’t multitask
when you're watching a foreign-language drama.’

And while foreign-language dramas are often remade for the
Anglo-American market — for example, The Bridge became The

Tunnel — the originals still dominate, because they transport us to a
different culture. As Walter Iuzzolino, who has set up a new streaming 
service dedicated to foreign-language TV, says, “You develop a
love for the distant world, because while you’re watching, you're in
the country. If you see something amazing set in Argentina, then
Argentina itself, the houses, the people, what they wear, what their
voices sound like, the language, is one of the
biggest appeals. There is a huge pleasure in that. 
"""

            Token.bot.send_message(message.chat.id, mess_1, reply_markup=markup, parse_mode='html')
            time.sleep(0.5)
            Token.bot.send_message(message.chat.id, hm_1, parse_mode='html')
            time.sleep(0.5)
            Token.bot.send_message(message.chat.id,
                             'Next'
                             '\nPress\n/Unit5B'
                             '\n/Unit5A_Test')
            time.sleep(0.5)


@Token.bot.message_handler(func=lambda message: message.text == '📝 Unit3 5A Test' or message.text == '/Unit5A_Test')
def test(inner_message):
    score = 0
    chat_id = inner_message.chat.id
    Token.bot.send_message(chat_id=chat_id,
                     text="1.You _____ eat healthy food to stay fit."
                          "\n1)have to."
                          "\n2)can."
                          "\n3)might.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer1(msg, score))


def check_answer1(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "1":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer2(msg, score))
    Token.bot.send_message(chat_id=inner_message.chat.id,
                     text="2.She _____ arrive on time for the meeting."
                          "\n1)should"
                          "\n2)may"
                          "\n3)must")


def check_answer2(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer3(msg, score))
    Token.bot.send_message(chat_id=inner_message.chat.id,
                     text="3.I _____ go to the store. I need some groceries."
                          "\n1)might"
                          "\n2)should"
                          "\n3)can")


def check_answer3(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer4(msg, score))
    Token.bot.send_message(chat_id=inner_message.chat.id,
                     text="4.They _____ study for the exam. It's important."
                          "\n1)may"
                          "\n2)must"
                          "\n3)have to")


def check_answer4(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "2":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer5(msg, score))
    Token.bot.send_message(chat_id=inner_message.chat.id,
                     text="5._____ you please pass me the salt?"
                          "\n1)Can"
                          "\n2)Might"
                          "\n3)Should")


def check_answer5(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "1":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.send_message(chat_id=inner_message.chat.id, text="Result: {} из 5".format(score))
    Token.bot.send_message(chat_id=inner_message.chat.id, text="Mark: {}".format(score))
    user_id = inner_message.from_user.id
    file_name = 'JSON/englishdatabase-388710-017506ff239d.json'
    gc = gspread.service_account(file_name)
    sh = gc.open_by_key('1VvsHSJy8D2RllLKWwuhwHPI47KMzxOj622899-_NZmw')
    worksheet = sh.sheet1
    user_ids = worksheet.col_values(1)
    row_index = user_ids.index(str(user_id)) + 1
    worksheet.update_cell(row_index, 13, str(score))
    user_first_name = inner_message.from_user.first_name
    user_last_name = inner_message.from_user.last_name
    if user_last_name:
        Token.bot.send_message(chat_id=inner_message.chat.id,
                         text="Rating added for user: {} {}".format(user_first_name, user_last_name))
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id,
                         text="Rating added for user: {}".format(user_first_name, ))
    Token.bot.send_message(inner_message.chat.id,
                     text="Next /Unit5B\nOr press:/Unit5A_Test to "
                          "try again")
    if answer == '/Unit5B':
        Token.bot.register_next_step_handler(inner_message, Unit5B)
