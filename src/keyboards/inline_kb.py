"""Custom inline keyboards"""

from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_callback_buttons(*, buttons: dict[str, str], sizes: tuple[int] = (2,)):
    """Build and return custom inline keyboard"""
    keyboard = InlineKeyboardBuilder()

    for text, data in buttons.items():
        keyboard.add(InlineKeyboardButton(text=text, callback_data=data))

    return keyboard.adjust(*sizes).as_markup()