from Token import bot
from telebot import types
from Unit2A import Unit2A
import time
import gspread


class Unit1B:
    @staticmethod
    def unit1b():
        @bot.message_handler(func=lambda message: message.text == '📚 Unit 1B' or message.text == '/Unit1B')
        def website(message):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Video for this section',
                                                  url="https://www.youtube.com/watch?v=ujKNa0fsGfk&t=52s"))

            mess_1 = """
<b>Unit 1B Life in colour</b>
"""

            hm_1 = """
Since ancient times, colour has been linked to the way we

think and feel. For early humans, the red of fire signalled

danger. Later, artists used coloured glass in church windows
to represent different feelings, for example, green symbolized
hope. In modern times, the colours we use to paint the walls in our
houses can affect our mood. So which colours should we use when
we are decorating?

Red is an optimistic colour. It’s a good colour for a dining room,
because it makes people feel sociable. It stimulates conversation
and makes you feel hungry. But as it’s a strong colour, it can
sometimes be a bit too much, and even give people headaches. You
could just paint one wall red, or use it for accessories such as lamps
and curtains. However, never use red in a baby’s bedroom, as it may
stop the baby from sleeping. Pink, on the other hand, is often used
in bedrooms. It’s traditionally the colour of love — a pale shade can
be peaceful and restful, while a darker shade can suggest passion.
Some people think it’s a very ‘girlie’ colour, so adding in areas of
dark grey or black to this colour scheme can help make it more
generally attractive.

If you want a warm, comforting effect, try orange. It’s also good
for dining rooms, as it’s said that it helps you digest your food.
However, like red, it’s a strong colour and can make a room look
smaller, so only use it in a room that gets plenty of light. A colour
that’s great for smaller spaces, on the other hand, is yellow. It’s
a happy, energetic colour, and is a good colour for a kitchen, as
apparently, it discourages insects! It’s not very restful though, so
it’s best not to use it for a bedroom.

Purple is good for rooms where you work, for example, a study or
a bedroom, because it’s a very creative, stimulating colour. However,
it’s another colour that can make it difficult for people to relax after
a busy day, so if you use it in a bedroom, it’s a good idea to combine
it with a lighter shade or another colour. Blue is also suitable for a
study, because it helps you to think and concentrate, as well as being
calm and restful. It’s a popular colour for bathrooms, and bedrooms
too, where a lot of people spend ‘thinking time’. Another calming
colour is green, and it’s also good for a bedroom or living room.
Green makes people feel relaxed and less stressed, but it can make
them lazy, so if you don’t want people to go to sleep on the sofa,
choose cushions and carpets in a bright colour like red or orange.

For people who prefer neutral colours, brown can be a good
choice. Although it can be boring, it’s a safe, reliable colour ina
living room, and you can paint one wall green or blue if you want a
bit of extra mental stimulation! Other neutral colours, like white,
grey, and beige, are always in fashion. White is the most flexible.
It’s safe and clean, and you can add any other colours to make the
room look brighter. However, white isn’t great for a bedroom if you
want to relax there — a survey showed that people with a white
bedroom tended to work in bed at least three times a week. Finally,
the most dramatic, and perhaps eccentric, choice of bedroom wall
colour is black. In fact, it works in any room in moderation, for
example, one black wall.
"""

            bot.send_message(message.chat.id, mess_1, reply_markup=markup, parse_mode='html')
            time.sleep(0.5)
            bot.send_message(message.chat.id, hm_1, parse_mode='html')
            time.sleep(0.5)
            bot.send_message(message.chat.id, "Well done, let's pass the test /Unit_1B_Test or move on to the next section' \n/Unit2A")


@bot.message_handler(func=lambda message: message.text == '📝 Unit 1B Test' or message.text == '/Unit_1B_Test')
def test(inner_message):
    score = 0
    chat_id = inner_message.chat.id
    bot.send_message(chat_id=chat_id, text="1.Which color is traditionally associated with love and can be used in bedrooms to create a peaceful or passionate atmosphere?"
                                           "\n1)Red."
                                           "\n2)Orange."
                                           "\n3)Pink.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer1(msg, score))


def check_answer1(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer2(msg, score))
    bot.send_message(chat_id=inner_message.chat.id,
                     text="2.What effect does the color blue have on a room, making it suitable for bathrooms and bedrooms?"
                          "\n1)It stimulates creativity"
                          "\n2)It encourages social interaction"
                          "\n3)It helps with concentration and is calming")


def check_answer2(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer3(msg, score))
    bot.send_message(chat_id=inner_message.chat.id,
                     text="3.What color is recommended for a dining room because it stimulates conversation and "
                          "sociability but should be used in moderation to avoid overwhelming?"
                          "\n1)Yellow"
                          "\n2)Green"
                          "\n3)Red")


def check_answer3(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer4(msg, score))
    bot.send_message(chat_id=inner_message.chat.id,
                     text="4.Which neutral color is described as safe and reliable for a living room but can be combined "
                          "with other colors for mental stimulation?"
                          "\n1)Brown"
                          "\n2)White"
                          "\n3)Black")


def check_answer4(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "2":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer5(msg, score))
    bot.send_message(chat_id=inner_message.chat.id,
                     text="5.Why is white not recommended for a bedroom if you want to relax there?"
                          "\n1)It makes the room look smaller"
                          "\n2)People with white bedrooms tend to work in bed frequently"
                          "\n3)It discourages insects")


def check_answer5(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "2":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.send_message(chat_id=inner_message.chat.id, text="Your score: {} out of 5".format(score))
    user_id = inner_message.from_user.id
    gc = gspread.service_account(filename='englishdatabase-388710-017506ff239d.json')
    sh = gc.open_by_key('1VvsHSJy8D2RllLKWwuhwHPI47KMzxOj622899-_NZmw')
    worksheet = sh.sheet1
    user_ids = worksheet.col_values(1)
    row_index = user_ids.index(str(user_id)) + 1
    worksheet.update_cell(row_index, 5, str(score))
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
Next Unit:\n/Unit2A

\nOr press:/Unit_1B_Test for replay
                     """)
    if answer == '/Unit2A':
        bot.register_next_step_handler(inner_message, Unit2A)
