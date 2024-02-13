import os

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from src.database.connection import db_conn
from src.database.repository import (
    add_support_request,
    add_user_to_block_list,
    get_info_about_ticket,
)
from src.keyboards import keyboards
from src.misc import bot, logger
from src.states.states import SupportState

router = Router()

@router.message(F.text == ('❓Есть вопрос/проблема'))
async def question(message, state: FSMContext):
    await message.answer('Напишите мне вопрос или проблему', reply_markup=keyboards.menu_kb)
    await state.set_state(SupportState.question)

@router.message(SupportState.question)
async def forward_question(message: Message, state: FSMContext):
    res = await message.send_copy(chat_id=os.getenv('SUPPORT_ID'), reply_markup=keyboards.answer_kb)
    try:
        add_support_request(
            session=db_conn.get_session(),
            message_from_user_id=message.message_id,
            message_from_support_id=res.message_id,
            user_id=message.from_user.id,
        )
    except Exception as e:
        logger.error(e)
        await message.answer('Не удалось отправить сообщение в поддержку, попробуйте позже')
        return  
    await message.answer('Сообщение отправлено в поддержку')
    await state.clear()

@router.callback_query(F.data == 'answer')
async def answer_to_message(qq: CallbackQuery, state: FSMContext):
    r = get_info_about_ticket(session=db_conn.get_session(), message_from_support_id=qq.message.message_id)

    await qq.message.answer('Напишите ответ')
    await state.update_data(user_id=r.user_id, message_to_delete=qq.message.message_id)
    await state.set_state(SupportState.answer)

@router.message(SupportState.answer)
async def forward_answer(message: Message, state: FSMContext):
    forward_to_chat_id = (await(state.get_data()))['user_id']
    await bot.send_message(chat_id=forward_to_chat_id, text='Сообщение от поддержки:')
    await message.copy_to(chat_id=forward_to_chat_id)
    await bot.delete_message(chat_id=message.chat.id, message_id=(await(state.get_data()))['message_to_delete'])
    await message.answer('Сообщение отправлено')
    await state.clear()

@router.callback_query(F.data == 'block')
async def block_user(qq: CallbackQuery):
    add_user_to_block_list(
        session=db_conn.get_session(), 
        user_id=get_info_about_ticket(
            session=db_conn.get_session(), 
            message_from_support_id=qq.message.message_id
        ).user_id
    )
    await qq.message.answer('Пользователь заблокирован')
    await qq.message.delete()