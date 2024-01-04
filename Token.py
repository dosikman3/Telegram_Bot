import telebot
from dotenv import load_dotenv
import os

load_dotenv()


class Bot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)


bot_token = os.getenv('TOKEN')
bot = Bot(bot_token).bot
