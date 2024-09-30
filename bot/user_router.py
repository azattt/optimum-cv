import logging
from aiogram import Router, F, Bot
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
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
        self.limit = 3

        self.router.message.register(self.show, UserStates.search_result)
        self.router.callback_query.register(self.show, F.data.startswith(self.callback_data + ":"))

    async def show(self, message_or_callback_query: Message | CallbackQuery):
        print(1)
        if isinstance(message_or_callback_query, Message):
            message = message_or_callback_query
            page = 0
        elif isinstance(message_or_callback_query.message, Message):
            await message_or_callback_query.answer()
            if message_or_callback_query.data is None:
                raise RuntimeError("empty callback")
            message = message_or_callback_query.message
            page = int(message_or_callback_query.data.split(":")[-1])
        else:
            raise RuntimeError("message or callback_query.message is not valid")
        
        if len(self.data) - page * self.limit > 0 and page >= 0:
            inline_keyboard: list[list[InlineKeyboardButton]] = []
            for row in self.data[self.limit * page : self.limit * (page + 1)]:
                inline_keyboard.append([InlineKeyboardButton(text=row[0], callback_data=row[1])])
            
            inline_keyboard.append([InlineKeyboardButton(text="Назад", callback_data=f"{self.callback_data}:{page-1}"),
                                    InlineKeyboardButton(text="Вперед", callback_data=f"{self.callback_data}:{page+1}")])
            reply_markup = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
            if isinstance(message_or_callback_query, Message):
                await message.answer(self.title, reply_markup=reply_markup)
            else:
                await message.edit_text(self.title, reply_markup=reply_markup)

        

    def set_data(self, data: list[tuple[str, str]]):
        self.data = data


logger = logging.getLogger("user_router")
user_router = Router(name="user_router")


@user_router.message(CommandStart())
@user_router.message(UserStates.start)
async def start_message(message: Message, state: FSMContext):
    await message.answer("Введите адрес населенного пункта")
    await state.set_state(UserStates.search_input)


# @user_router.callback_query(UserStates.search_result and F.callback_data == "search_results")
search_paginator = Paginator(
    user_router, "search_results", "Результаты поиска (данные берутся с сайта pkk.rosreestr.ru): "
)

@user_router.message(UserStates.search_input)
async def search_input(
    message: Message,
    state: FSMContext,
):
    if message.text is None:
        await message.answer("Неверный адрес.")
        return
    try:
        result = await search_address(message.text)
        if result is None:
            raise RuntimeError("search_address result is None")
    except Exception:
        await message.answer("Ошибка поиска. Отчет об ошибке отправлен")
        await start_message(message, state)
        raise
    search_paginator.set_data([(row["address"], f"search_results:{i}") for i, row in enumerate(result)])
    await state.set_data({"search_input_data": {"result": result, "message_id": message.message_id}})
    await search_paginator.show(message)
