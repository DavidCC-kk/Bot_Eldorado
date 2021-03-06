# settings.py
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
COMMAND = os.getenv('DISCORD_COMMAND')
CLEVERBOT_API = os.getenv('CLEVERBOT_API_KEY')
LANGUAGE_CODE = os.getenv('LANG_CODE')
LANGUAGE_NAME = os.getenv('LANG_NAME')