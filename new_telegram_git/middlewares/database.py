from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import User


class GetDBUser(BaseMiddleware):

    async def on_Process_message(self, message: types.Message, data: dict):
        data["user"] = User(id=message.from_user.id, name=message.from_user.full_name)

    async def on_Process_callback(self, cq: types.CallbackQuery, data: dict):
        data["user"] = User(id=cq.from_user.id, name=cq.message.from_user.full_name)