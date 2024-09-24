import asyncio
import os
import logging

from aiogram import Bot, Dispatcher

from user_router import user_router

async def main():
    logging.basicConfig()
    logging.getLogger("aiogram").setLevel(logging.DEBUG)
    zemlebot_token = os.getenv("ZEMLEBOT_TOKEN")
    if zemlebot_token is None:
        raise RuntimeError("Bot token is not set")
    bot = Bot(zemlebot_token)
    dp = Dispatcher()
    dp.include_router(user_router)
    await dp.start_polling(bot)

asyncio.run(main())