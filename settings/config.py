import os
from dotenv import load_dotenv
from emoji import emojize
from urllib.parse import quote

load_dotenv()

VERSION = '0.0.1'
AUTHOR = 'Vasiliy Turtugeshev'

HOST = os.getenv('HOST')
POSTGRESQL_USER = os.getenv('POSTGRESQL_USER')
POSTGRESQL_PASSWORD = os.getenv('POSTGRESQL_PASSWORD')
DATABASE = os.getenv('DATABASE')

POSTGRES_URI = f"postgresql://{POSTGRESQL_USER}:" \
                    f"%s@{HOST}/{DATABASE}" % quote(f"{POSTGRESQL_PASSWORD}")

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = str(os.getenv('ADMIN_ID')).split(',')

KEYBOARD = {
    "FAST_FORWARD_BUTTON": emojize(':fast-forward_button:'),
    "FAST_REVERSE_BUTTON": emojize(':fast_reverse_button:'),
    'INFORMATION': emojize(':information:'),
}
