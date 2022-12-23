from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp






#@dp.callback_query_handler(text="buttton_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 2", callback_data="button_call_2")
    markup.add(button_call_1)
    question = "Игрок не Реал Мадрида в данный момент"
    answers = [
        'Модрич',
        'Иско',
        'Камавинга',
        'Одриозола',
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Ты точно не фанат реала",
        open_period=5,
        reply_markup=markup,
    )


#@dp.callback_query_handler(text="buttton_call_2")
async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 3", callback_data="button_call_3")
    markup.add(button_call_1)
    question = "Тренер реал мадрида"
    answers = [
        'Анчелотти',
        'Гвардиола',
        'Зидан',
        'Моуриньо',
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Ты точно не фанат реала",
        open_period=5,
        reply_markup=markup,
    )

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="buttton_call_1")
    dp.register_callback_query_handler(quiz_3, text="buttton_call_3")