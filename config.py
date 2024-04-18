import os
from dotenv import load_dotenv

#load enironment variables from .env file
load_dotenv()

API_TOKEN = os.getenv("TOKEN")