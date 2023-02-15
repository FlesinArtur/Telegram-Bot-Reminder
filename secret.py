from os import environ

import dotenv

dotenv.load_dotenv('.env')
BOT_TOKEN = environ.get('BOT_TOKEN')
