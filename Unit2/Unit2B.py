from telebot import types
from Token import Token
from Unit3 import Unit3A
import time
import gspread


class Unit2B:
    @staticmethod
    def unit2b():
        @Token.bot.message_handler(func=lambda message: message.text == '📚 Unit 2B' or message.text == '/Unit2B')
        def website(message):
            markup = types.InlineKeyboardMarkup()

            mess_1 = """
<b>Unit3 2B Go to checkout</b> 
"""

            hm_1 = """
At 6.00 p.m. on Thursday, in Waterstones in Piccadilly,
Av staff were running around with bowls of jelly

beans and bottles of raspberry lemonade. Five minutes
later, people of all ages started to come through the doors, some
dressed up as characters from the books — a small girl even
produced an owl cage! ‘I’m reading the fifth book again at the
moment’, said 28-year-old Alex. “This is the third event I’ve
been to. Last year they transformed the second floor into Diagon
Alley.’ In many of the chain’s 275 branches across the UK, similar
scenes were taking place. ‘Our first wizards have arrived for
#harrypotterbooknight’, tweeted staff at the Bradford store.

But Harry Potter night wasn’t the only cause for celebration
for staff and customers. The previous day, Waterstones

had announced that it was back in profit for the first time
since 2011, under the leadership of its very own wizard,
James Daunt. Daunt was already a successful bookseller, who
had many loyal customers. He was brought in to rescue the
Waterstones chain when it was about to close down.

When Daunt took over Waterstones, his first task was to cut
costs. Then he had to make the stores more attractive and
improve the lighting. Coffee shops were opened inside the
stores, and events were held, such as the now-famous Harry
Potter nights, or talks by authors. But the biggest change was

that Daunt gave each individual store the power to choose
what books to sell, and to choose the prices for different books.
This made a big difference. Sales went up because shops were
stocking more books that appealed to local customers.

Another of his changes was training really knowledgeable
staff. ‘If a customer can tell me what was the last really good
book they read, I know exactly what to sell them next,’ Daunt
says. Given that Waterstones stocks more than 150,000 titles,
this is not an easy thing to do — but it is something that is
helping Waterstones to differentiate itself from Amazon.

Daunt is optimistic about the future of bookshops. ‘People love
buying books,’ he said. ‘It’s a physical pleasure that customers
don’t get when they shop online. If we keep creating shops
that do that, it doesn’t matter what goes on online. High streets
and shops are part of the heart of the community. People will
always want to go to shops.’
"""

            Token.bot.send_message(message.chat.id, mess_1, reply_markup=markup, parse_mode='html')
            time.sleep(0.5)
            Token.bot.send_message(message.chat.id, hm_1, parse_mode='html')
            time.sleep(0.5)
            Token.bot.send_message(message.chat.id,
                             "Well done, let's pass the test /Unit_2B_Test or move on to the next section' \n/Unit3A")


@Token.bot.message_handler(func=lambda message: message.text == '📝 Unit3 2B' or message.text == '/Unit2B_Test')
def test(inner_message):
    score = 0
    chat_id = inner_message.chat.id
    Token.bot.send_message(chat_id=chat_id,
                     text="1.Which sentence uses the correct form of the Future Simple tense?"
                          "\n1)I will going to the party tonight.."
                          "\n2)I am going to go to the party tonight.."
                          "\n3)I going to the party tonight..")

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
                     text="2.She ___________ start a new job next month."
                          "\n1)is going to"
                          "\n2)will going to"
                          "\n3)going to be")


def check_answer2(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "1":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer3(msg, score))
    Token.bot.send_message(chat_id=inner_message.chat.id,
                     text="3.Which sentence uses the correct form of the Future Simple tense?"
                          "\n1)They going to visit their grandparents tomorrow."
                          "\n2)They are going to visit their grandparents tomorrow."
                          "\n3)They will visit their grandparents tomorrow.")


def check_answer3(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer4(msg, score))
    Token.bot.send_message(chat_id=inner_message.chat.id,
                     text="4.He ___________ travel to Europe next summer."
                          "\n1)will going to"
                          "\n2)going to be"
                          "\n3)is going to")


def check_answer4(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    Token.bot.register_next_step_handler(inner_message, lambda msg: check_answer5(msg, score))
    Token.bot.send_message(chat_id=inner_message.chat.id,
                     text="5.Which sentence uses the correct form of the Future Simple tense?"
                          "\n1)We will to have a picnic in the park."
                          "\n2)We going to have a picnic in the park."
                          "\n3)We are going to have a picnic in the park.")


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
    worksheet.update_cell(row_index, 7, str(score))
    user_first_name = inner_message.from_user.first_name
    user_last_name = inner_message.from_user.last_name
    if user_last_name:
        Token.bot.send_message(chat_id=inner_message.chat.id,
                         text="Rating added for user: {} {}".format(user_first_name, user_last_name))
    else:
        Token.bot.send_message(chat_id=inner_message.chat.id,
                         text="Rating added for user: {}".format(user_first_name, ))
    Token.bot.send_message(inner_message.chat.id,
                     text="Next Unit3:/Unit3A\nOr press:/Unit2B_Test to try again")
    if answer == '/Unit3A':
        Token.bot.register_next_step_handler(inner_message, Unit3A)
