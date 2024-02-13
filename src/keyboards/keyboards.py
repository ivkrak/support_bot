from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)

menu_kb = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text='❓Есть вопрос/проблема')],
        [KeyboardButton(text='🎁 Забрать подарок')],
    ]
)

go_to_menu_kb = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text='⏪ Назад')]
    ]
)

answer_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Ответить', callback_data='answer')],
        [InlineKeyboardButton(text='Заблокировать пользователя', callback_data='block')],
    ]
)