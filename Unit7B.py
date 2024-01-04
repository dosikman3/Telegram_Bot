from telebot import types
from Token import bot
from Finish import Finish
import time
import gspread


class Unit7B:
    @staticmethod
    def unit7b():
        @bot.message_handler(func=lambda message: message.text == '📚 Unit 7B' or message.text == '/Unit7B')
        def website(message):
            markup = types.InlineKeyboardMarkup()

            mess_1 = """
<b>Unit 7B Shall we go out or stay in</b>
"""

            hm_1 = """
A different kind of social network

It's a bright Thursday morning in Oxford and the Thirsty
Meeples café is a buzz of activity. As I, my wife, and two
sons sit at a sunny window table, the assistant, Gareth,
introduces himself and recommends some games. First,

o5 he suggests Forbidden Desert. ‘You have crash-landed in a
desert,’ explains Gareth. ‘You have to find all the pieces of a
flying ship in order to escape.’ Next, he suggests Small World,
in which wizards, giants, and humans with special powers
battle for land in a world that’s too small for them all. Last, he

io recommends Citadels, a game where you compete to become
the King's Master Builder by building a medieval city. We
choose Citadels. As we play, next to us Eveline, a 30-year-old
Dutch university teacher, is playing Ticket to Ride with her
Belgian husband, Roger - they are racing against each other to

15 build railway tracks across Europe. Two teenagers play Sushi
Gol, a card game where they have to create sushi dishes. What
has drawn all these different people here, from serious gamers
to families? Eveline thinks she has the answer. She looks
around at the other customers and at the library of games on

20 the shelves. ‘I would say it’s the original social network.’

Thirsty Meeples's name comes from the combination of
‘meeples', the pieces that board gamers play with, and wanting
a drink. It is one of a growing number of board game shops and
cafés popping up all over the UK, inspired by their growing

25 popularity in the USA.

Peter Wooding, a former punk rocker, opened
a board game shop called Orc's Nest in
Covent Garden, London, in 1987. For the first
few years, the shop hardly made any money
at all, but over 30 years later, it is thriving.

Wooding says that one of the reasons for
its success is that the games and players
are very different from 30 years ago. Today,
they are young professional couples, who
like the idea of playing a game with friends
and having a few drinks, rather than going out to the
pub. Another reason is that there are also far
more women playing games. Wooding
says the game Pandemic, where players
0 must collaborate to control global
diseases, and whose main character is a
female scientist, has had a huge influence.
‘Much wider appeal,’ says Wooding. ‘More
friendly.’ Pandemic is an example of
45 the newer, less aggressive games, with
themes like farming or landscape building. 9
One such game, Catan, in which players
have to buy and sell natural resources to
build roads and new cities, has sold more than
50 22 million copies in 30 languages.

‘The growth of the video games industry has, perhaps
surprisingly, also been one of the biggest factors in the new
popularity of board games, largely because they have made playing
games such a normal thing for adults to do. Everyone has at least

5 one game on their phone, and more people are open to the idea of
playing a game than ever before. Social media has also provided an
easy way for people to recommend new games to each other.

At Thirsty Meeples in Oxford, I talk
to owners John and Zuzi Morgan.

6 What's Zuzi’s explanation for the trend?
“There's so much technology,’ she says.
‘Everybody's busy and you want to bring
people back together in a way that's not
just staring at screens. It’s a natural thing

6s in people. We are supposed to be together and communicating

with each other in the real world.
"""

            bot.send_message(message.chat.id, mess_1, reply_markup=markup, parse_mode='html')
            time.sleep(0.5)
            bot.send_message(message.chat.id, hm_1, parse_mode='html')
            time.sleep(0.5)
            bot.send_message(message.chat.id,
                             'Well done!!!!'
                             'Our wishes: /END'
                             '\nLast Test'
                             '\n/Unit7B_Test')
            time.sleep(0.5)


@bot.message_handler(func=lambda message: message.text == '📝 Unit 7B Test' or message.text == '/Unit7B_Test')
def test(inner_message):
    score = 0
    chat_id = inner_message.chat.id
    bot.send_message(chat_id=chat_id,
                     text="1.They _____ the meeting off due to bad weather."
                          "\n1)put."
                          "\n2)take."
                          "\n3)call.")

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
                     text="2.I _____ my old clothes away and bought new ones."
                          "\n1)put"
                          "\n2)take"
                          "\n3)throw")


def check_answer2(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "1":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer3(msg, score))
    bot.send_message(chat_id=inner_message.chat.id,
                     text="3.She _____ her friend up to invite her to the party."
                          "\n1)put."
                          "\n2)take."
                          "\n3)call.")


def check_answer3(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer4(msg, score))
    bot.send_message(chat_id=inner_message.chat.id,
                     text="4.They _____ the TV on during the entire day."
                          "\n1)put"
                          "\n2)take"
                          "\n3)leave")


def check_answer4(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer5(msg, score))
    bot.send_message(chat_id=inner_message.chat.id,
                     text="5.He _____ his jacket on before going outside."
                          "\n1)put"
                          "\n2)take"
                          "\n3)wear")


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
    worksheet.update_cell(row_index, 18, str(score))
    cell_range_values = worksheet.range(row_index, 4, row_index, 18)
    cell_values = [int(cell.value) for cell in cell_range_values]
    average_value = sum(cell_values) / len(cell_values)
    average_value_1 = round(average_value, 1)
    worksheet.update_cell(row_index, 19, str(average_value_1))
    user_first_name = inner_message.from_user.first_name
    user_last_name = inner_message.from_user.last_name
    if user_last_name:
        bot.send_message(chat_id=inner_message.chat.id,
                         text="Rating added for user: {} {}".format(user_first_name, user_last_name))
    else:
        bot.send_message(chat_id=inner_message.chat.id,
                         text="Rating added for user: {}".format(user_first_name, ))
    cell_19_value = worksheet.cell(row_index, 19).value
    bot.send_message(inner_message.chat.id,
                     text=f"Congratulations on your final grade.:{cell_19_value},"
                          f"\nOur wishes: /END\nOr:/Unit7B_Test to "
                          "try again")
    if answer == '/END':
        bot.register_next_step_handler(inner_message, Finish)
