import asyncio
import getpass
import os
import logging

from tortoise import Tortoise

from aiogram import Bot, Dispatcher

from user_router import user_router


async def main():
    logging.basicConfig()
    logging.getLogger('aiogram').setLevel(logging.DEBUG)
    # init db
    db_user = 'zemlebot'
    db_password = getpass.getpass('Postgresql password: ')
    await Tortoise.init(
        db_url=f'postgres://{db_user}:{db_password}@localhost:5432/zemlebot',
        modules={'models': ['models']},
    )
    await Tortoise.generate_schemas(safe=True)
    zemlebot_token = os.getenv('ZEMLEBOT_TOKEN')
    if zemlebot_token is None:
        raise RuntimeError('Bot token is not set')
    bot = Bot(zemlebot_token)
    dp = Dispatcher()
    dp.include_router(user_router)
    await dp.start_polling(bot)
    await Tortoise.close_connections()
    

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
