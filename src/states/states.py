from aiogram.fsm.state import State, StatesGroup


class SupportState(StatesGroup):
    question = State()
    answer = State()
