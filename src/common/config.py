"""Модуль содержит настройки проекта"""

import os

from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

BOT_TOKEN = os.getenv('BOT_TOKEN')
ALLOWED_UPDATES = ['message', 'edited_message', 'callback_query']
