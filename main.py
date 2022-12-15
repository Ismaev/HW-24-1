from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from decouple import config
import logging

TOKEN = config('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Добро пожаловать хозяин {message.from_user.first_name}")

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

@dp.callback_query_handler(text="buttton_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 2", callback_data="button_call_1")
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



@dp.message_handler()
async def echo(message: types.Message):
    print(message)
    await bot.send_message(chat_id=message.from_user.id, text=message.text)
    await bot.send_message(chat_id=message.from_user.id, text=int(message.text) ** 2)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

