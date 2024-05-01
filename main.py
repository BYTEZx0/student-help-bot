import logging
import telebot
from configuration.config import API_TOKEN
import utils.logger as logger_save
from utils.validator import reg_check, subject_code_check
from utils.views import post_usersave
from utils.courses import COURSE_DETAILS
from telebot.types import InputFile

#configuring logging.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger_save.init_logger(f"logs/botlog.log")


#intializing bot 
bot = telebot.TeleBot(API_TOKEN)


#to store user info
user_dict = {}

class User:
    def __init__(self, name):
        self.name = name
        self.reg_no = None
        self.dob = None


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    logger.info("char_id", message.chat.id)
    logger.info("user_dict", user_dict)
    if message.chat.id in user_dict:
        bot.send_message(message.chat.id, "Hi " +  user_dict[message.chat.id].name + "\nYou are already registered, Now you can get modelpapers using \n `/model <subject_code>` command")
        return
    msg = bot.reply_to(message, "Hi I am Student Help Bot\nEnter Your Name")
    bot.register_next_step_handler(msg, process_name_step)

@bot.message_handler(commands=['model'])
def model_command(message):
    args = message.text.split()
    if len(args) < 2:
        bot.reply_to(message, "Try using:\n /model <subject_code>")
        return
    subject_code = args[1].upper()
    if not subject_code_check(subject_code):
        bot.reply_to(message, "Invalid Subject Code")
        return
    else:
        if subject_code in COURSE_DETAILS.keys():
            bot.send_document(message.chat.id, InputFile("pdf/bitcoin.pdf")) # TODO add the reponse of file fetch to this function
        else:
            bot.reply_to(message, subject_code+" is not an existing Subject Code")

def process_name_step(message):
    #Add an exception such that no commands should be taken as name
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        msg = bot.reply_to(message, "Hi " + user.name + "\nEnter your University Registration Number")
        bot.register_next_step_handler(msg, process_reg_no_step)
    except Exceptions as e:
        bot.reply_to(message, "oops")

def process_reg_no_step(message):
    try:
        chat_id = message.chat.id
        reg_no = message.text
        #add condition to check reg_no
        if not reg_check(reg_no.upper()):
            msg = bot.reply_to(message, 'Enter Correct University Number')
            bot.register_next_step_handler(msg, process_reg_no_step)
            return
        user = user_dict[chat_id]
        user.reg_no = reg_no.upper()
        post_usersave(user_name=user.name, uyt_reg=user.reg_no, chat_id=chat_id) #save user details to database
        bot.send_message(chat_id, user.name + " Your University Registration Number : "+ user.reg_no)
    except Exceptions as e:
        bot.reply_to(message, "oops")


# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()


logger.info("Bot started")
bot.infinity_polling()
