import os

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from src.keyboards import keyboards
from src.states.states import SupportState
from src.misc import bot

router = Router()

@router.message(F.text == ('❓Есть вопрос/проблема'))
async def question(message, state: FSMContext):
    await message.answer('Напишите мне вопрос или проблему', reply_markup=keyboards.go_to_menu_kb)
    await state.set_state(SupportState.question)

@router.message(SupportState.question)
async def forward_question(message, state: FSMContext):
    await message.forward(chat_id=os.getenv('SUPPORT_ID'), reply_markup=keyboards.answer_kb)