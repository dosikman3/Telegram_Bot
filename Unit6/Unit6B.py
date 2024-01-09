from telebot import types
from Token import Token
from Unit7 import Unit7A
import time
import gspread


class Unit6B:
    @staticmethod
    def unit6b():
        @Token.bot.message_handler(func=lambda message: message.text == '📚 Unit 6B' or message.text == '/Unit6B')
        def website(message):
            markup = types.InlineKeyboardMarkup()

            mess_1 = """
<b>Unit3 6B Do it yourself </b>
"""

            hm_1 = """
Marina's extraordinary uses for things

Your house is full of everyday items that can be used for things you would
never have expected. | promise all these ideas work — I've tried them!

1 Do you have a problem with insects? Don’t like spiders in your
house? Citrus or lemon oil is a traditional repellent for insects of all kinds — and the oil is in the peel.
Take large pieces of peel and place them along window sills and cracks outside your house, to stop spiders, ants, 
and other unwelcome guests from coming in. Cats also really dislike the strong smell of lemons, so you can use lemon 
peel or lemon juice to keep them away from specific areas in your house or garden. However, despite what
you may have heard, lemon oil doesn’t have any effect on mosquitoes, sadly, so it won't protect you from their bites.

2 Even after you've washed them, plastic food containers often end up with a rather unpleasant smell from the food you 
kept in them. Newspaper can absorb all sorts of moisture and smells. Just crumple a piece of newspaper and put it inside 
your food container, then seal the container and leave it overnight.

In the morning, throw away the newspaper and enjoy your clean

container. You can also use the same method to deal with smelly
trainers. Just stuff them with newspaper overnight and they'll be
smell-free the next day.

3 Towels are always soft and lovely when they're new, but they
soon become a bit rough. You could buy fabric conditioner to
help to restore that softness, but you can also use a tennis
ball. Just put the ball in the dryer with your towels or sheets. Because
of the movement of the ball against the material, they will feel really
soft when you take them out. Make sure you use a new tennis ball,
though, or you risk ruining your lovely clean laundry.

4 Eggs are rich in proteins that are very similar to those found
in our hair, so they make a great conditioner. Try beating an egg with a bit of olive oil, and apply it to your hair. (Use
a couple of eggs if your hair is really dry.) If you want to smell less
like an omelette and more like you've just come back from the
hairdresser’s, add a couple of drops of scented oil. Leave on for about
20 minutes and then rinse with warm water. Your hair will be shiny
and extra smooth. But be careful not to use really hot water or you
might cook the eggs!
"""
            Token.bot.send_message(message.chat.id, mess_1, reply_markup=markup, parse_mode='html')
            time.sleep(0.5)
            Token.bot.send_message(message.chat.id, hm_1, parse_mode='html')
            time.sleep(0.5)
            Token.bot.send_message(message.chat.id,
                             'Next '
                             '\nPress\n/Unit7A'
                             '\n/Unit6B_Test')
            time.sleep(0.5)


@Token.bot.message_handler(func=lambda message: message.text == '📝 Unit3 6B Test' or message.text == '/Unit6B_Test')
def test(inner_message):
    score = 0
    chat_id = inner_message.chat.id
    Token.bot.send_message(chat_id=chat_id,
                     text="1.The book _____ (write) by a famous author."
                          "\n1)is written."
                          "\n2)was written."
                          "\n3)has written.")

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
                     text="2.The house _____ (build) last year."
                          "\n1)is built"
                          "\n2)was built"
                          "\n3)has built")


def check_answer2(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "2":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer3(msg, score))
    Token.bot.send_message(chat_id=inner_message.chat.id,
                     text="3.English _____ (speak) in many countries."
                          "\n1)is spoken"
                          "\n2)was spoken"
                          "\n3)has spoken")


def check_answer3(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "1":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer4(msg, score))
    Token.bot.send_message(chat_id=inner_message.chat.id,
                     text="4.The letter _____ (send) yesterday."
                          "\n1)is sent"
                          "\n2)was sent"
                          "\n3)has sent")


def check_answer4(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "2":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer5(msg, score))
    Token.bot.send_message(chat_id=inner_message.chat.id,
                     text="5.The cake _____ (bake) by my mom."
                          "\n1)is baked"
                          "\n2)was baked"
                          "\n3)has baked")


def check_answer5(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "2":
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
    worksheet.update_cell(row_index, 16, str(score))
    user_first_name = inner_message.from_user.first_name
    user_last_name = inner_message.from_user.last_name
    if user_last_name:
        Token.bot.send_message(chat_id=inner_message.chat.id,
                         text="Rating added for user: {} {}".format(user_first_name, user_last_name))
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id,
                         text="Rating added for user: {}".format(user_first_name, ))
    Token.bot.send_message(inner_message.chat.id,
                     text="Next:/Unit7A\nOr:/Unit7B_Test to "
                          "try again")
    if answer == '/Unit7A':
        Token.bot.register_next_step_handler(inner_message, Unit7A)
