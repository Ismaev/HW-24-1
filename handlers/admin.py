from aiogram import types, Dispatcher
import random
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp, ADMINS

async def game_dice(message: types.Message):
    a = await bot.send_dice(message.chat.id)
    b = await bot.send_dice(message.chat.id)
    if a.dice.value > b.dice.value:
        await bot.send_message(message.chat.id, "ты выиграл")
    elif a.dice.value < b.dice.value:
        await bot.send_message(message.chat.id, "ты проиграл")
    else:
        await  bot.send_message(message.chat.id, "ничья")

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(game_dice, commands=["Dice"])