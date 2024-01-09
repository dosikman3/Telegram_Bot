from telebot import types
from Token import Token
from Unit7 import Unit7B
import time
import gspread


class Unit7A:
    @staticmethod
    def unit7a():
        @Token.bot.message_handler(
            func=lambda message: message.text == '📚 Unit 7A' or message.text == '/Unit7A')
        def website(message):
            markup = types.InlineKeyboardMarkup()
            markup.add(
                types.InlineKeyboardButton('Video',
                                           url="https://www.youtube.com/watch?v=OjhenMYRrHY"))

            mess_1 = """
<b>Unit3 7A Take your cash</b>
"""

            hm_1 = """

Here's the text with the missing words filled in:

He gives away his salary
to save the world

Working for a big financial company in London on a six-figure salary,
Wigs might expect Grayden Reece-Smith to be living a lavish lifestyle, going on expensive
holidays or driving a sports car around south London, where he lives. In fact,
the 28-year-old lives a very different existence from his colleagues. He lives on a figure that he calculated he could comfortably live on.

Over the past five years, Reece-Smith has handed over more than
£250,000 to organizations such as International Care Ministries, which helps the poor, and the Against Malaria Foundation. He is part of a growing number
of young professionals described as ‘effective altruists’. Effective altruists
typically donate regularly to a charity which they think will have a significant
impact. Some choose high-paying careers to make more money, which can then be given away.

Reece-Smith considered working in the charity sector after graduating
from university, but calculated that he could make a bigger difference by
donating a large part of his salary. He had taught at a school in ‘Tanzania, but
then realized that earning and giving would be more effective. “The cost of
my flights there could have paid the salaries of two teachers for an entire
year,” he says. Instead, he could ‘stay at home, living a nice life and still make a significant impact.

He is not frugal last year he went to Cuba on holiday, and he enjoys his life. But his
lifestyle isn’t as luxurious as some of the people he works with.
"I tend not to buy supermarket-branded food products, but I don't deprive myself. Other
people on my salary might have a bigger house. Some of my colleagues have
four-bedroom houses, but we only bought what we needed ~ a two-bedroom
flat. £42,000 is more than enough to live on and still save,’ he says.
"""

            Token.bot.send_message(message.chat.id, mess_1, reply_markup=markup, parse_mode='html')
            time.sleep(0.5)
            Token.bot.send_message(message.chat.id, hm_1, parse_mode='html')
            time.sleep(0.5)
            Token.bot.send_message(message.chat.id,
                             'Next'
                             '\nPres\n/Unit7B'
                             '\n/Unit7A_Test')
            time.sleep(0.5)


@Token.bot.message_handler(func=lambda message: message.text == '📝 Unit3 7A Test' or message.text == '/Unit7A_Test')
def test(inner_message):
    score = 0
    chat_id = inner_message.chat.id
    Token.bot.send_message(chat_id=chat_id,
                     text="1.She said, 'I am going to the store.' She said that she ____ to the store."
                          "\n1)goes."
                          "\n2)went."
                          "\n3)was going.")

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
                     text="2.He said, 'I will call you later.' He said that he _____ me later."
                          "\n1)will call"
                          "\n2)would call"
                          "\n3)called")


def check_answer2(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "2":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer3(msg, score))
    Token.bot.send_message(chat_id=inner_message.chat.id,
                     text="3.'I have finished my homework,' she said. "
                          "She said that she ____ her homework."
                          "\n1)has finished"
                          "\n2)had finished"
                          "\n3)finished")


def check_answer3(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "2":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer4(msg, score))
    Token.bot.send_message(chat_id=inner_message.chat.id,
                     text="4.They said, 'We are leaving tomorrow.' "
                          "They said that they _____ leaving the next day."
                          "\n1)are leaving"
                          "\n2)were leaving"
                          "\n3)had left")


def check_answer4(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "2":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer5(msg, score))
    Token.bot.send_message(chat_id=inner_message.chat.id,
                     text="5.'I can swim,' he said. He said that he _____ swim."
                          "\n1)can"
                          "\n2)could"
                          "\n3)may")


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
    worksheet.update_cell(row_index, 17, str(score))
    user_first_name = inner_message.from_user.first_name
    user_last_name = inner_message.from_user.last_name
    if user_last_name:
        Token.bot.send_message(chat_id=inner_message.chat.id,
                         text="Rating added for user: {} {}".format(user_first_name, user_last_name))
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id,
                         text="Rating added for user: {}".format(user_first_name, ))
    Token.bot.send_message(inner_message.chat.id,
                     text="Next:/Unit7B\nOr :/Unit7A_Test to "
                          "try again")
    if answer == '/Unit7B':
        Token.bot.register_next_step_handler(inner_message, Unit7B)
