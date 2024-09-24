from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart

from states import UserStates

from rosreestr import search_locality

user_router = Router()

@user_router.message(CommandStart())
async def start_message(message: Message, state: FSMContext):
    await message.answer("Введите адрес населенного пункта")
    await state.set_state(UserStates.search_input)

@user_router.message(UserStates.search_input)
async def search_input(message: Message, state: FSMContext):
    
    await message.answer("Результаты поиска")
