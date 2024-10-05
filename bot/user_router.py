import logging
from typing import Any
from aiogram import Bot, Router, F
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart

from states import UserStates

from rosreestr import search_address



class Paginator:
    class OldMessageError(Exception):
        pass

    FAIL_CALLBACK_DATA = "start" 
    def __init__(self, router: Router, callback_data: str, title: str, limit: int = 5):
        self.router = router
        self.callback_data = callback_data
        self.title = title
        self.limit = limit

        # self.router.message.register(self.show, UserStates.search_input)
        self.router.callback_query.register(self.show, F.data.startswith(self.callback_data + ":"))

    async def show(self, message_or_callback_query: Message | CallbackQuery, state: FSMContext):
        state_data = (await state.get_data())
        if "Paginator" not in state_data:
            raise RuntimeError()
        if self.callback_data not in state_data["Paginator"]:
            raise RuntimeError()
 
        if isinstance(message_or_callback_query, Message):
            message = message_or_callback_query
            page = 0
        elif isinstance(message_or_callback_query.message, Message):
            await message_or_callback_query.answer()
            if message_or_callback_query.data is None:
                raise RuntimeError("empty callback")
            message = message_or_callback_query.message
            if message.message_id != state_data["Paginator"][self.callback_data]["message_id"]:
                keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Вернуться в начало", callback_data=Paginator.FAIL_CALLBACK_DATA)]])
                await message.edit_text("Сообщение устарело.", reply_markup=keyboard)
                return
            page = int(message_or_callback_query.data.split(":")[-1])
        else:
            raise RuntimeError("message or callback_query.message is not valid")
        

        
        data = state_data["Paginator"][self.callback_data]["data"]

        if len(data) - page * self.limit > 0 and page >= 0:
            inline_keyboard: list[list[InlineKeyboardButton]] = []
            for row in data[self.limit * page : self.limit * (page + 1)]:
                inline_keyboard.append([InlineKeyboardButton(text=row[0], callback_data=row[1])])
            
            inline_keyboard.append([InlineKeyboardButton(text="Назад", callback_data=f"{self.callback_data}:{page-1}"),
                                    InlineKeyboardButton(text="Вперед", callback_data=f"{self.callback_data}:{page+1}")])
            reply_markup = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
            if isinstance(message_or_callback_query, Message):
                await message.answer(self.title, reply_markup=reply_markup)
            else:
                await message.edit_text(self.title, reply_markup=reply_markup)

    async def set_data(self, state: FSMContext, current_message_id: int, data: list[tuple[str, str, Any | None]]):
        await state.update_data({"Paginator": {self.callback_data: {"data": data, "message_id": current_message_id+1}}})

    async def get_data(self, state: FSMContext, callback_message_id: int):
        data = await state.get_data()
        if "Paginator" not in data:
            raise RuntimeError()
        if self.callback_data not in data["Paginator"]:
            raise RuntimeError()
        if data["Paginator"][self.callback_data]["message_id"] != callback_message_id:
            raise Paginator.OldMessageError()
        return data["Paginator"][self.callback_data]["data"]


logger = logging.getLogger("user_router")
user_router = Router(name="user_router")


@user_router.message(CommandStart())
@user_router.message(UserStates.start)

async def start_message(message: Message, state: FSMContext):
    await message.answer("Введите адрес населенного пункта")
    await state.set_state(UserStates.search_input)

@user_router.callback_query(F.data == "start")
async def start_message_callback(callback_query: CallbackQuery, bot: Bot, state: FSMContext):
    await bot.send_message(callback_query.from_user.id, "Введите адрес населенного пункта")
    await state.set_state(UserStates.search_input)
    await callback_query.answer()

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
        result = result["candidates"]
    except Exception:
        await message.answer("Ошибка поиска. Отчет об ошибке отправлен")
        await start_message(message, state)
        raise

    
    await search_paginator.set_data(state, message.message_id, [(row["address"], f"search_results_selected:{i}", row) for i, row in enumerate(result)])
    await search_paginator.show(message, state)
    await state.set_state(UserStates.search_result)

@user_router.callback_query(UserStates.search_result and F.data.startswith("search_results_selected:"))
async def search_results_selected(callback_query: CallbackQuery, state: FSMContext):
    if not isinstance(callback_query.message, Message):
        raise RuntimeError()
    if callback_query.data is None:
        raise RuntimeError()
    row = int(callback_query.data.split(":")[1])
    if row < 0:
        raise RuntimeError()
    selected_locality = (await search_paginator.get_data(state, callback_query.message.message_id))[row]

    reply_markup = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Вернуться к поиску", callback_data="start")]])  
    print(selected_locality[2])
    await callback_query.message.answer(f"Выбран населенный пункт: \"{selected_locality[0]}\"", reply_markup=reply_markup)
    await callback_query.answer()
