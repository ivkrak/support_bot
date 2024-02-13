import os

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from src.keyboards import keyboards

router = Router()



@router.message()
async def other(message: Message):
    await message.answer(
        text='Я вас не понимаю, попробуйте еще раз',
        reply_markup=keyboards.menu_kb
    )
