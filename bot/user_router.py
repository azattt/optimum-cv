import logging
from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart

from states import UserStates

from rosreestr import search_address

logger = logging.getLogger("user_router")
user_router = Router()

@user_router.message(CommandStart())
@user_router.message(UserStates.start)
async def start_message(message: Message, state: FSMContext):
    await message.answer("Введите адрес населенного пункта")
    await state.set_state(UserStates.search_input)

@user_router.message(UserStates.search_input)
async def search_input(message: Message, state: FSMContext):
    if message.text is None:
        await message.answer("Неверный адрес.")
        return
    try:
        result = await search_address(message.text)
    except Exception:
        message.answer("Ошибка поиска. Отчет об ошибке отправлен")
        await state.set_state(UserStates.start)
        await user_router.propagate_event("message", message)
        raise
    if result is None:
        await message.answer("Результаты поиска (данные берутся с сайта pkk.rosreestr.ru): ", result)
