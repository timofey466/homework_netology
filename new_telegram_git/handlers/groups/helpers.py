from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import BotCommand

from loader import dp, bot

new_command = (
    ("work", "команда для админов для помощи")
)

comand_for = []
for cmd in comand_for:
    comand_for.append(BotCommand(command=cmd[0], description=cmd[1]))
await bot.set_my_commands(commands=comand_for)


@dp.message_handler(Command("work"))
async def work_helpers(message: types.Message):
    await message.reply("")
