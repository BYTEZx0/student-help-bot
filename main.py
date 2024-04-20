import logging
import telebot
from configuration.config import API_TOKEN
import requests

#configuring logging.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.init_logger(f"logs/botlog.log")


#intializing bot 
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hi, its me bot")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

logger.info("Bot started")
bot.infinity_polling()