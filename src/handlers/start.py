from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from src.keyboards import keyboards

router = Router()


# @router.message(Command(commands=['⏪ Назад', 'start']))
@router.message(Command('start'))
@router.message(F.text == '⏪ Назад')
async def start(message: Message):
    await message.answer(
        text='Здравствуйте! Спасибо, что обратились в службу поддержки ИМЯ_ОРГАНИЗАЦИИ',
        reply_markup=keyboards.menu_kb
    )



