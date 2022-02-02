from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db
from handlers import client, admin, other


async def on_startup(_):
    print('Бот онлайн')
    sqlite_db.sql_start()


client.register_handler_client(dp)
admin.register_handler_admin(dp)
other. register_handler_other(dp)

executor.start_polling(dp, on_startup=on_startup)
# executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
