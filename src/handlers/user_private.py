"""Module contains event handler functions"""

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.utils.formatting import as_list, Bold

from src.keyboards.inline_kb import get_callback_buttons
from src.keyboards.reply_kb import get_keyboard

user_private_router = Router()


@user_private_router.message(CommandStart())
async def cmd_start(message: Message):
    welcome_text = as_list(
        'Привет 👋 я бот-помощник.',
        'Моя задача - помочь тебе в изучении английского языка.',
        'Если ты готов, то можем приступить прямо сейчас.',
    )

    await message.answer(
        welcome_text.as_html(),
        reply_markup=get_callback_buttons(
            buttons={'Поехали': 'go'},
            sizes=(1,)
        )
    )


@user_private_router.callback_query(F.data == 'go')
async def callback_run(callback: CallbackQuery):
    await callback.answer('Отлично!', show_alert=False)
    instructions_text = as_list(
        'обучение будет происходить в игровой форме.',
        'Правила очень простые - я задаю слово на русском языке,',
        'ты выбираешь один из четырёх вариантов на английском.',
        'Если не знаешь какой из вариантов выбрать, то жми кнопку',
        '"Дальше". Кстати, ты можешь использовать тренажёр как',
        'конструктор и добавить любое слово или удалить уже ранее',
        'добавленное слово. Для этого воспользуйся кнопками:',
        Bold('добавить слово ➕'),
        Bold('удалить слово 🔙')
    )
    await callback.message.answer(
        instructions_text.as_html(),
        reply_markup=get_callback_buttons(
            buttons={'Начать обучение': 'begin'}
        )
    )


@user_private_router.callback_query(F.data == 'begin')
async def callback_run(callback: CallbackQuery):
    await callback.answer('Обучение началось твоё..', show_alert=False)
    await callback.message.answer(
        'Отлично!',
        reply_markup=get_keyboard(
            'Dream',
            'We',
            'it',
            'She',
            'Дальше',
            'Добавить слово',
            'Удалить слово',
            placeholder='Выберите команду',
            sizes=(2, 2, 2, 1)
        )
    )