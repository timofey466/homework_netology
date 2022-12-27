import logging

from loader import dp

from aiogram import Dispatcher, types
from aiogram.types import message

from data.config import admins
from handlers.users.start import user_text


async def on_startup_notify(dp: Dispatcher):
    for admin in admins:
        try:
            await dp.bot.send_message(admin, "Бот Запущен и готов к работе")
        except Exception as err:
            logging.exception(err)



