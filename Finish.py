from Token import bot


class Finish:
    @staticmethod
    def finish():
        @bot.message_handler(commands=['END'])
        def finishing(message):

            if message.from_user.first_name and message.from_user.last_name:
                mess = f'Congratulation, <b>{message.from_user.first_name} {message.from_user.last_name}!</b>&#127468;&#127463;\n'
            else:
                mess = f'Congratulation, <b>{message.from_user.first_name}!</b>&#127468;&#127463;\n'
            mess_1 = """
Your commitment to learning and development deserves sincere praise. you have done
incredible work, mastering new knowledge and skills that will accompany you throughout your life.
Your persistence and dedication to learning the language was impressive. You showed real
enthusiasm and have proven that with constant diligence and perseverance, any goal can be achieved. Now,
when you have completed this course, a world of possibilities opens up for you. Keep practicing and
improve your skills in everyday life. Use English for travel,
communicating with new people, reading books and watching films. Don't be afraid to make mistakes
after all, they are an integral part of the learning process. We wish you great success in the future
using English! Let your language skills open up new horizons and help you achieve
your goals and enriches your life. Remember that learning is a continuous process and we hope
that you will continue to develop and improve. Thank you for choosing our course and entrusting us with yours
education. We wish you many new opportunities, inspiration and joy from using the English language
"""

            bot.send_message(message.chat.id, mess, parse_mode='html')
            bot.send_message(message.chat.id, mess_1)
