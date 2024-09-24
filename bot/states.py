from aiogram.fsm.state import StatesGroup, State

class UserStates(StatesGroup):
    start = State()
    search_input = State()
    search_result = State()
    