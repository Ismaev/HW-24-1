from aiogram import types, Dispatcher
from config import bot, dp




# async def echo(message: types.Message):
#     if message.text.isdigit():
#         await bot.send_message(chat_id=message.from_user.id, text=int(message.text) ** 2)
#     else:
#         await bot.send_message(chat_id=message.from_user.id, text=message.text)
#
# def register_handlers_extra(dp: Dispatcher):
#     dp.register_message_handler(echo)