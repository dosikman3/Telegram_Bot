from telebot import types
from Token import bot
from Unit4B import Unit4B
import time
import gspread


class Unit4A:
    @staticmethod
    def unit4a():
        @bot.message_handler(
            func=lambda message: message.text == '📚 Unit 4A' or message.text == '/Unit4A')
        def website(message):
            markup = types.InlineKeyboardMarkup()
            markup.add(
                types.InlineKeyboardButton('Видео для этого раздела',
                                           url="https://www.youtube.com/watch?v=_6xlNyWPpB8"))

            mess_1 = """
<b>Unit 4A don't throw it away!</b>

"""

            mess_2 = ("\n"
                      "<b>1</b> Since its invention some 100 years ago, plastic has become an\n"
                      "integral part of our daily lives, said naturalist David Attenborough\n"
                      "\n"
                      "in the final episode of the highly praised BBC series Blue Planet II.\n"
                      "“But every year, some eight million tons of it ends up in the ocean...and\n"
                      "there it can be lethal.’ Slowly, it seems, we may at last be waking up to\n"
                      "the fact that something that makes our lives easier in the short term has\n"
                      "consequences that can last thousands of years.\n"
                      "\n"
                      "<b>2</b> One of our main convenience items is plastic water bottles. They are a\n"
                      "major contributor to waste in the UK, and we use ten million of them a\n"
                      "day. Although the bottles themselves can be recycled, the caps cannot.\n"
                      "The problem doesn’t stop with plastic bottles. According to new research,\n"
                      "almost a fifth of the waste that people put into recycling bins cannot, in\n"
                      "fact, be recycled. The reason for this is that the packaging is often made\n"
                      "up of several components, many of which are not recyclable.\n"
                      "\n"
                      "<b>3</b> People often believe that something is recyclable when it’s not. Take, for\n"
                      "example, that black plastic ready-meal tray that you normally put with your\n"
                      "bottles and newspapers, or your glittery Christmas wrapping paper — these\n"
                      "cannot be recycled, though white trays and plain wrapping paper can be.\n"
                      "Plastic pouches, such as the ones used for baby food or pasta sauce, can’t\n"
                      "be recycled, so it’s better to buy them in glass jars, which can be. Toothpaste\n"
                      "tubes also can’t be recycled, but the pump-action bottles can be.\n"
                      "\n"
                      "<b>4</b> Unclear labelling is often to blame. Recycling information on packaging\n"
                      "varies dramatically. Sainsbury's supermarket, for example, labels on its\n"
                      "own-brand packaging exactly which parts can and cannot be recycled.\n"
                      "Some manufacturers, on the other hand, include no information. Even the\n"
                      "recycling symbol itself is confusing, because people don’t know what the\n"
                      "numbers mean. A 1 or 2 means that a product can be widely recycled,\n"
                      "\n"
                      "3 indicates PVC, which is not widely recycled, 4 is polyethylene, and\n"
                      "5 is polypropylene, both of which can only be recycled in some centres.\n"
                      "6 and 7 are not widely accepted for recycling.\n"
                      "\n"
                      "<b>5</b> Last year, more than half of the plastic waste that the UK exported\n"
                      "for recycling was sent to China. China has now banned imports of\n"
                      "‘foreign garbage’, because it is receiving too much poor-quality plastic,\n"
                      "contaminated with non-recyclable items. It’s a worrying prospect. There\n"
                      "are fears that it might not be possible to find alternative destinations for\n"
                      "all our recyclable waste. As a result, plastic may end up being burnt, or\n"
                      "put in landfill, or more will end up in the sea.\n"
                      "\n"
                      "<b>6</b> Perhaps we should stop assuming that everything that looks recyclable\n"
                      "actually is. Instead, we need to start buying products that come in packaging that we are sure can be"
                      "recycled, or better still, we should try to avoid packaging altogether\n")

            time.sleep(0.5)
            bot.send_message(message.chat.id, mess_1, reply_markup=markup, parse_mode='html')
            time.sleep(0.5)

            bot.send_message(message.chat.id, mess_2, parse_mode='html')
            time.sleep(0.5)
            bot.send_message(message.chat.id,
                             '\nPress\n/Unit4B\n/Unit4A_Test')
            time.sleep(0.5)


@bot.message_handler(func=lambda message: message.text == '📝 Unit 4A Test' or message.text == '/Unit4A_Test')
def test(inner_message):
    score = 0
    chat_id = inner_message.chat.id
    bot.send_message(chat_id=chat_id,
                     text="1.I have _____ money to buy a new phone."
                          "\n1)too."
                          "\n2)enough."
                          "\n3)a little.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer1(msg, score))


def check_answer1(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "2":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer2(msg, score))
    bot.send_message(chat_id=inner_message.chat.id,
                     text="2.There are _____ people in the park."
                          "\n1)too"
                          "\n2)enough"
                          "\n3)a few")


def check_answer2(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer3(msg, score))
    bot.send_message(chat_id=inner_message.chat.id,
                     text="3.She is _____ young to watch that movie."
                          "\n1)too"
                          "\n2)enough"
                          "\n3)a little")


def check_answer3(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "1":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer4(msg, score))
    bot.send_message(chat_id=inner_message.chat.id,
                     text="4.He has _____ time to finish the project."
                          "\n1)too"
                          "\n2)enough"
                          "\n3)a few")


def check_answer4(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "2":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer5(msg, score))
    bot.send_message(chat_id=inner_message.chat.id,
                     text="5.Can you give me _____ water, please?"
                          "\n1)too"
                          "\n2)enough"
                          "\n3)a little")


def check_answer5(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.send_message(chat_id=inner_message.chat.id, text="Your score: {} из 5".format(score))
    bot.send_message(chat_id=inner_message.chat.id, text="Mark: {}".format(score))
    user_id = inner_message.from_user.id
    gc = gspread.service_account(filename='englishdatabase-388710-017506ff239d.json')
    sh = gc.open_by_key('1VvsHSJy8D2RllLKWwuhwHPI47KMzxOj622899-_NZmw')
    worksheet = sh.sheet1
    user_ids = worksheet.col_values(1)
    row_index = user_ids.index(str(user_id)) + 1
    worksheet.update_cell(row_index, 11, str(score))
    user_first_name = inner_message.from_user.first_name
    user_last_name = inner_message.from_user.last_name
    if user_last_name:
        bot.send_message(chat_id=inner_message.chat.id,
                         text="Rating added for user: {} {}".format(user_first_name, user_last_name))
    else:
        bot.send_message(chat_id=inner_message.chat.id,
                         text="Rating added for user: {}".format(user_first_name, ))
    bot.send_message(inner_message.chat.id,
                     text="Next:/Unit4B\nOr:/Unit4A_Test to "
                          "try again")
    if answer == '/Unit4B':
        bot.register_next_step_handler(inner_message, Unit4B)
