from os import getenv
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from composite.startANDmainBUTTONS import router as start_router
from composite.keyboards import router as keyboards_router
from composite.texts import router as text_router
load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()
dp.include_router(text_router)
dp.include_router(keyboards_router)
dp.include_router(start_router)


async def main():
    bot = Bot(token=TOKEN)
    print("Запущено")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


