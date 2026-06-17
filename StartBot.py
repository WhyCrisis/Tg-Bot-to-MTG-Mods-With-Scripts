#---

from os import getenv
import asyncio

#---

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

#---

#---
from composite.composite_buttons import router as start_router
from composite.composite_keyboards import router as keyboards_router
from composite.texts_composite import router as text_router
from libs_router.libs_text import router as libs_text
from libs_router.libs_choosing import router as choosing_libs



#---

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

#---

#---
#подключение новых роутеров. Заполнять снизу вверх по типу пригодности (желательно бы избегать конфликтов, но у меня кончаются мозги на этом этапе
dp = Dispatcher()
dp.include_router(text_router)
dp.include_router(keyboards_router)
dp.include_router(start_router)
dp.include_router(libs_text)
dp.include_router(choosing_libs)
#---

#---инициализация
async def main():
    bot = Bot(token=TOKEN)
    print("Запущено")
    await dp.start_polling(bot)
#---
if __name__ == '__main__':
    asyncio.run(main())


