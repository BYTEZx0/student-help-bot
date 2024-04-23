import telebot
import logging
import time
from configuration.config import API_TOKEN
import utils.logger as logger_save

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger_save.init_logger(f"logs/botlog.log")

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "I'm here to help Akshay Kumar")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

def stop_bot():
    logger.info("Stopping the bot...")
    bot.stop_polling()
    time.sleep(5)  # Ensure some time for all threads to close
    logger.info("Bot stopped successfully.")

if __name__ == "__main__":
    try:
        logger.info("Bot started")
        bot.infinity_polling()
    except KeyboardInterrupt:
        stop_bot()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        stop_bot()
