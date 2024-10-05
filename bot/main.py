import asyncio
import getpass
import os
import logging

from tortoise import Tortoise

from aiogram import Bot, Dispatcher

from user_router import user_router
from middlewares import BanMiddleware
from tortoise_storage import TortoiseStorage

async def main():
    logging.basicConfig()
    logging.getLogger('aiogram').setLevel(logging.DEBUG)
    # init db
    db_user = 'zemlebot'
    db_password = getpass.getpass('Postgresql password: ')
    await Tortoise.init(
        db_url=f'asyncpg://{db_user}:{db_password}@localhost:5432/zemlebot',
        modules={'models': ['models']},
    )
    await Tortoise.generate_schemas(safe=True)
    zemlebot_token = os.getenv('ZEMLEBOT_TOKEN')
    if zemlebot_token is None:
        raise RuntimeError('Bot token is not set')
    bot = Bot(zemlebot_token)
    tortoise_storage = TortoiseStorage()
    dp = Dispatcher(storage=tortoise_storage)
    ban_middleware = BanMiddleware()
    dp.update.wrap_outer_middleware(ban_middleware)
    dp.include_router(user_router)
    await dp.start_polling(bot)
    await Tortoise.close_connections()
    

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
