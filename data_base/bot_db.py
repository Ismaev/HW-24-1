import sqlite3
from config import bot
import random

db = sqlite3.connect('bot.sqlite3')
cursor = db.cursor()


def sql_create():
    if db:
        print('база данных подключен')
    db.execute(
        "CREATE TABLE IF NOT EXISTS anketa"
        "(id INTEGER PRIMARY KEY, fullname TEXT,"
        "direction TEXT, age INTEGER, grup TEXT)"
    )
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO anketa VALUES "
                       "(?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()


async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM anketa ").fetchall()
    random_user = random.choice(result)
    await bot.send_message(message.from_user.id, random_user[1],
                           f"{random_user[2]}, {random_user[3]}, {random_user[4]}, ")


async def sql_command_all():
    return cursor.execute('SELECT * FROM anketa').fetchall()


async def sql_command_delete(id):
    cursor.execute("DELETE FROM anketa WHERE id = ?", (id,))
    db.commit()


async def sql_commands_get_id():
    return cursor.execute('SELECT id FROM anketa').fetchall()
