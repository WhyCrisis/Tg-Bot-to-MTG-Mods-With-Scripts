from aiogram import Router, F
from aiogram.filters import Command, callback_data
from aiogram.types import (Message, ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardButton,
                           InlineKeyboardMarkup,
                           CallbackQuery,
                           FSInputFile, BackgroundTypeWallpaper
                           )
from aiogram.types import ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from composite.composite_keyboards import download_mtg_libs, choose_libs

router = Router()

async def text_mtg_mod(message: Message):
    text=(
        'ℹ️ <b>Загрузчик Lua скриптов для Arizona Mobile</b>\n'
        '● Клиент ARZ: actual release.web\n'
        '● MonetLoader: 3.8.0 (x32)\n'
        '<b>🛠 Встроенный функционал:</b>\n'
        '● Автоматическая установка всех библиотек\n'
        '    ❗ ️Обратите внимание:\n'
        '● MonetLoader не меняет оригинальный лаунчер.\n'
        '● Он отключает x64 и запускает игру в x32 (armeabi-v7a).\n'
        '● Lua — это дополнение, сам клиент остаётся без изменений.\n'
        '⚠️ ЛЮБЫЕ баги в игре, например Ошибка подключения (https://t.me/mtgmods/3218):\n'
            '   ● Это баги оригинального x32-клиента Arizona\n'
            '   ● Пишите в мастерскую <a href="https://vk.com/agm_workshop">поддержку</a>, что-бы они пофиксили\n'
            '   ● Обязательно укажите, что у вас armeabi-v7a (x32-версия)\n'
            '   ● Я не исправляю х32-клиент аризоны, даже не пишите мне \n\n'
        'ℹ️ Если у вас появляется ошибка "Приложение не установлено" / "Не удалось обработать пакет":\n'
            '   ● Скачайте другой лаунчер х64 (не от меня)(https://t.me/mtgmods/5354)\n'
            '   ● Файлы с установкой х64 и х32 приложены ниже \n'
    )
    await message.bot.send_photo(
        chat_id=message.chat.id,
        photo = FSInputFile('neccessaryfiles/pictures/arizona_mtg_Monetka.png'),
        caption = text,
        parse_mode='HTML',
        reply_markup = download_mtg_libs())


