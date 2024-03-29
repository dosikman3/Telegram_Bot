from Token import bot
from telebot import types


class Test:
    @staticmethod
    def test():
        @bot.message_handler(commands=['Test'])
        def button(message):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            Unit1A = types.KeyboardButton('📝 Unit 1A Quiz')
            Unit1B = types.KeyboardButton('📝 Unit 1B Quiz')
            Unit2A = types.KeyboardButton('📝 Unit 2A Quiz')
            Unit2B = types.KeyboardButton('📝 Unit 2B Quiz')
            Unit3A = types.KeyboardButton('📝 Unit 3A Quiz')
            Unit3B = types.KeyboardButton('📝 Unit 3B Quiz')
            Practical = types.KeyboardButton('📝 Practical English Quiz')
            Unit4A = types.KeyboardButton('📝 Unit 4A Quiz')
            Unit4B = types.KeyboardButton('📝 Unit4B Quiz')
            Unit5A = types.KeyboardButton('📝 Unit 5A Quiz')
            Unit5B = types.KeyboardButton('📝 Unit 5B Quiz')
            Unit6A = types.KeyboardButton('📝 Unit 6A Quiz')
            Unit6B = types.KeyboardButton('📝 Unit 6B Quiz')
            Unit7A = types.KeyboardButton('📝 Unit 7A Quiz')
            Unit7B = types.KeyboardButton('📝 Unit 7B Quiz')

            markup.add(Unit1A, Unit1B, Unit2A, Unit2B, Unit3A, Unit3B, Practical, Unit4A, Unit4B, Unit5A, Unit5B,
                       Unit6A, Unit6B, Unit7A, Unit7B)
            bot.send_message(message.chat.id, 'Кнопки на все тесты:', reply_markup=markup)
