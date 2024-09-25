import logging
from aiogram import Router, F, Bot
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart

from states import UserStates

from rosreestr import search_address

class Paginator:
    def __init__(self, callback_data: str, title: str):
        self.callback_data = callback_data
        self.title = title
        self.data: list[list[str]] = []
        self.page = 0
        self.limit = 10
        

    async def show(self, message: Message):
        inline_keyboard: list[list[InlineKeyboardButton]] = []
        keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
        await message.answer(self.title, reply_markup=keyboard)

    def set_data(self, data: list[list[str]]):
        self.data = data

logger = logging.getLogger("user_router")
user_router = Router()

@user_router.message(CommandStart())
@user_router.message(UserStates.start)
async def start_message(message: Message, state: FSMContext):
    await message.answer("Введите адрес населенного пункта")
    await state.set_state(UserStates.search_input)

search_paginator = Paginator("search_results", "Результаты поиска (данные берутся с сайта pkk.rosreestr.ru): ")

@user_router.callback_query(UserStates.search_result and F.callback_data == sear)

@user_router.message(UserStates.search_input)
async def search_input(message: Message, state: FSMContext, ):
    if message.text is None:
        await message.answer("Неверный адрес.")
        return
    try:
        result = [i["address"] for i in await search_address(message.text)]
    except Exception:
        await message.answer("Ошибка поиска. Отчет об ошибке отправлен")
        await start_message(message, state)
        raise
    if result is None:
        await search_paginator.show(message)


