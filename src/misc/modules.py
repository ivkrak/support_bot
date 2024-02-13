import os

from aiogram import Bot
from loguru import logger

logger.add(
    'logs/log.log',
    format='{time:HH:mm:ss} {level} {message}',
    level='DEBUG',
    rotation='50 MB'
)

bot = Bot(token=os.getenv('BOT_TOKEN'))
