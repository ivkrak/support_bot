import asyncio

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

from src.handlers import other, start, support
from src.misc import bot, logger


# Запуск бота
async def main():
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(
        start.router,
        support.router,
        other.router   
    )
    # await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    load_dotenv()
    logger.info('Бот запущен')
    asyncio.run(main())
