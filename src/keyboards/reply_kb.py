"""Custom reply keyboards"""

from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_keyboard(*buttons: str, placeholder: str=None, sizes: tuple[int]=(2,)):
    """Build and return custom reply keyboard"""
    keyboard = ReplyKeyboardBuilder()

    for index, text in enumerate(buttons, start=0):
        keyboard.add(KeyboardButton(text=text))

    return keyboard.adjust(*sizes).as_markup(
        resize_keyboard=True, input_field_placeholder=placeholder)