from Token import Token
from telebot import types


class Help:
    @staticmethod
    def help():
        @Token.bot.message_handler(commands=['Lessons'])
        def button(message):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            Unit1A = types.KeyboardButton('📚 Unit 1A')
            Unit1B = types.KeyboardButton('📚 Unit 1B')
            Unit2A = types.KeyboardButton('📚 Unit 2A')
            Unit2B = types.KeyboardButton('📚 Unit 2B')
            Unit3A = types.KeyboardButton('📚 Unit 3A')
            Unit3B = types.KeyboardButton('📚 Unit 3B')
            Practical = types.KeyboardButton('📚 Practical English')
            Unit4A = types.KeyboardButton('📚 Unit 4A')
            Unit4B = types.KeyboardButton('📚 Unit 4B')
            Unit5A = types.KeyboardButton('📚 Unit 5A')
            Unit5B = types.KeyboardButton('📚 Unit 5B')
            Unit6A = types.KeyboardButton('📚 Unit 6A')
            Unit6B = types.KeyboardButton('📚 Unit 6B')
            Unit7A = types.KeyboardButton('📚 Unit 7A')
            Unit7B = types.KeyboardButton('📚 Unit 7B')

            markup.add(Unit1A, Unit1B, Unit2A, Unit2B, Unit3A, Unit3B, Practical, Unit4A, Unit4B, Unit5A, Unit5B,
                       Unit6A, Unit6B, Unit7A, Unit7B)
            Token.bot.send_message(message.chat.id, 'Кнопки на уроки:', reply_markup=markup)
