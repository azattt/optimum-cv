import logging
from aiogram import Router, F, Bot
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart

from states import UserStates

from rosreestr import search_address

class Paginator:
    def __init__(self, router: Router, callback_data: str, title: str):
        self.router = router
        self.callback_data = callback_data
        self.title = title
        self.data: list[tuple[str, str]] = []
        self.page = 0
        self.limit = 10

        self.router.message.register(self.show, UserStates.search_input)
        
        

    async def show(self, message: Message):
        inline_keyboard: list[list[InlineKeyboardButton]] = []
        for row in self.data[self.limit * self.page: self.limit * (self.page+1)]:
            inline_keyboard.append([InlineKeyboardButton(text=row[0], callback_data=row[1])])

        reply_markup = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
        await message.answer(self.title, reply_markup=reply_markup)
    
    # async def

    def set_data(self, data: list[tuple[str, str]]):
        self.data = data
    
    async def __call__(self, message: Message):
        await self.show(message)
    

logger = logging.getLogger("user_router")
user_router = Router()

@user_router.message(CommandStart())
@user_router.message(UserStates.start)
async def start_message(message: Message, state: FSMContext):
    await message.answer("Введите адрес населенного пункта")
    await state.set_state(UserStates.search_input)


# @user_router.callback_query(UserStates.search_result and F.callback_data == "search_results")
search_paginator = Paginator(user_router, "search_results", "Результаты поиска (данные берутся с сайта pkk.rosreestr.ru): ")
user_router.callback_query.register(search_paginator.show, UserStates.search_result and F.callback_data == search_paginator.callback_data)

@user_router.message(UserStates.search_input)
async def search_input(message: Message, state: FSMContext, ):
    if message.text is None:
        await message.answer("Неверный адрес.")
        return
    try:
        result = await search_address(message.text)
    except Exception:
        await message.answer("Ошибка поиска. Отчет об ошибке отправлен")
        await start_message(message, state)
        raise
    if result is None:
        search_paginator.set_data(result)
        await search_paginator.show(message)


