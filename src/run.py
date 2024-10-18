"""Run application"""

import asyncio
import sys
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from src.common.config import BOT_TOKEN, ALLOWED_UPDATES
from src.handlers.user_private import user_private_router
from src.data.engine import session_factory, drop_tables, create_tables
from src.middlewares.db_connect import DataBaseSession


logger = logging.getLogger(__name__)

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
dp.include_router(user_private_router)


async def on_startup(bot):
    recreate = True

    # if recreate:
    #     await drop_tables()

    await create_tables()


async def on_shutdown(bot):
    pass


async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    dp.update.middleware(DataBaseSession(session_pool=session_factory))
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info('Bot stopped')
