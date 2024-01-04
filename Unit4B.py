from telebot import types
from Token import bot
from Unit5A import Unit5A
import time
import gspread


class Unit4B:
    @staticmethod
    def unit4b():
        @bot.message_handler(func=lambda
                message: message.text == '📚 Unit 4B' or message.text == '/Unit4B')
        def website(message):
            markup = types.InlineKeyboardMarkup()
            markup.add(
                types.InlineKeyboardButton('Video',
                                           url="https://www.youtube.com/watch?v=85YWV1TEK6I"))

            mess_1 = """
<b>Put it on your CV</b>
"""

            hm_1 = """
he best part-time job I ever had...

Dog walker, babysitter, shelf-stacker - most of us would
have one of these classic part-time jobs on our CV. But
did we really learn anything from the experience?

A Sir Ranulph Fiennes, explorer

When I was 16, I wanted to buy a canoe and needed £85. I washed
the buses at Midhurst bus station between 3.00 a.m. and 7.00 a.m.
during the week. Then I washed the dishes at the Angel Hotel from
6.00 p.m. to 10.00 p.m. I was paid £11 per week in all, and that’s
how I got the cash. It’s too long ago to know if I actually learned
anything from the experience.

B Russell Kane, comedian

I did two humiliating Saturday jobs. The first was selling vacuum
cleaners door to door. I didn’t sell a single one. The other job was
working with my granddad for a frozen-food delivery service.

I doubt that a Saturday job really teaches you anything. Where

I come from, it’s automatic - at age 11 you get a job. It wasn't,

‘Hey man, I’m really learning the value of work.’ It was, ‘If I want
money, I must work for it.’ My dad never gave me a penny of pocket
money after the age of 11.

C Tony Ross, illustrator and author 4

In the fifties, when I was a boy, I used to work at the post office

over Christmas. It was fantastic fun. I earned enough to buy an

old motor scooter. My favourite part was going in the lorry to \
collect the mailbags from the station because you didn’t Ze
have to walk the streets all day. The other good thing was | 2
doing a round with your own house in it, because then you~

could stop for a cup of tea. I learned the basics of working for

money, like arriving on time and enjoying it no matter what. It

was a good introduction because very few people work for fun.

D Clive Stafford Smith, lawyer

I worked for a sand and gravel company when I was 16. It was cold,
damp, and so boring that I cried. I've learned various important
things from that job. First, I know I’m very lucky to have a job

now that I truly love. I also learned that it’s crazy to pay bankers
millions while paying a low wage to people at gravel companies.
It’s terrible work and no one should have to do it. Anyone who says
differently should be forced to work at that gravel company for a year.

E Adele Parks, author

When I was doing my A levels, I worked in our local supermarket
for two years, stacking shelves. I was 16 then, and ina job like that,
you make the decision whether this is what you want to do for the
rest of your life. I spent a lot of time chatting to the other guys and
girls who had permanent jobs. I am good at talking and telling
stories, and I think I learned it there because one of the things
about stacking shelves or being at the checkout is that you have lots
of opportunities to talk to people. That’s what i liked best.
"""

            bot.send_message(message.chat.id, mess_1, reply_markup=markup, parse_mode='html')
            time.sleep(0.5)
            bot.send_message(message.chat.id, hm_1, parse_mode='html')
            time.sleep(0.5)
            bot.send_message(message.chat.id,
                             'Next Unit '
                             '\nPress\n/Unit5A'
                             '\n/Unit4B_Test')
            time.sleep(0.5)


@bot.message_handler(func=lambda message: message.text == '📝 Unit 4B Test' or message.text == '/Unit4B_Test')
def test(inner_message):
    score = 0
    chat_id = inner_message.chat.id
    bot.send_message(chat_id=chat_id,
                     text="1.I enjoy _____ books in my free time."
                          "\n1)read."
                          "\n2)reading."
                          "\n3)to read.")

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
                     text="2.She promised _____ me later."
                          "\n1)call"
                          "\n2)calling"
                          "\n3)to call")


def check_answer2(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer3(msg, score))
    bot.send_message(chat_id=inner_message.chat.id,
                     text="3.We need _____ the car before the trip."
                          "\n1)wash"
                          "\n2)washing"
                          "\n3)to wash")


def check_answer3(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer4(msg, score))
    bot.send_message(chat_id=inner_message.chat.id,
                     text="4.They can't afford _____ on vacation this year."
                          "\n1)go"
                          "\n2)going"
                          "\n3)to go")


def check_answer4(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
        bot.send_message(chat_id=inner_message.chat.id, text="Correct answer!")
        score += 1
    else:
        bot.send_message(chat_id=inner_message.chat.id, text="Incorrect answer.")

    bot.register_next_step_handler(inner_message, lambda msg: check_answer5(msg, score))
    bot.send_message(chat_id=inner_message.chat.id,
                     text="5.He decided _____ Spanish at the language school."
                          "\n1)learn"
                          "\n2)learning"
                          "\n3)to learn")


def check_answer5(inner_message, score):
    answer = inner_message.text.lower()
    if answer == "3":
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
    worksheet.update_cell(row_index, 12, str(score))
    user_first_name = inner_message.from_user.first_name
    user_last_name = inner_message.from_user.last_name
    if user_last_name:
        bot.send_message(chat_id=inner_message.chat.id,
                         text="Rating added for user: {} {}".format(user_first_name, user_last_name))
    else:
        bot.send_message(chat_id=inner_message.chat.id,
                         text="Rating added for user: {}".format(user_first_name, ))
    bot.send_message(inner_message.chat.id,
                     text="Next:/Unit5A\nOr:/Unit4B_Test to "
                          "try again")
    if answer == '/Unit5A':
        bot.register_next_step_handler(inner_message, Unit5A)
