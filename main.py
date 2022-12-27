import asyncio

from aiogram.utils import executor
import logging
from handlers import client, callback, extra, admin, fsm_mentor, notification
from config import dp
from data_base.bot_db import sql_create

fsm_mentor.register_handlers_fsm(dp)
admin.register_handlers_admin(dp)
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
notification.register_handlers_notification(dp)
# extra.register_handlers_extra(dp)

async def on_startup(_):
    asyncio.create_task(notification.scheduler())
    sql_create()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

