import random

from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp, ADMINS
from keyboards.client_kb import start_markup, game_button


@dp.message_handler(commands=['pin'], commands_prefix='!/')
async def pin_message(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await message.answer("Укажите что закрепить?")


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Добро пожаловать хозяин {message.from_user.first_name}",
                           reply_markup=start_markup)


@dp.message_handler(commands=['mem'])
async def mem_handler(call: types.CallbackQuery):
    photo = open("media/WhatsApp Image 2022-12-16 at 01.07.27 — копия.jpeg", "rb")
    await bot.send_photo(call.from_user.id, photo=photo)


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 1", callback_data="button_call_2")
    markup.add(button_call_1)
    question = "Игрок Реал Мадрида в данный момент"
    answers = [
        'Роналду',
        'Рамос',
        'Йович',
        'Одриозола',
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Ты точно не фанат реала",
        open_period=5,
        reply_markup=markup,
    )

async  def game_message(message: types.Message):
    if message.from_user.id in ADMINS:
        data = ['🎲', '⚽️', '🎳', '🏀', '🎯', '🎰']
        r = random.choice(data)
        await bot.send_dice(message.chat.id, emoji=r)
    else:
        await bot.send_message(message.chat.id, 'У тебя не достаточно прав!')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(mem_handler, commands=['mem'])
    dp.register_message_handler(pin_message, commands=['pin'], commands_prefix='!/')
    dp.register_message_handler(game_message, commands=['game'])
