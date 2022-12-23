from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)
cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton('CANCEL'))

start_button = KeyboardButton("/start")
quiz_button = KeyboardButton("/quiz")
game_button = KeyboardButton("/dice")

start_markup.add(start_button, quiz_button, game_button)