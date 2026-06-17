from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import (Message,ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardButton,
                           InlineKeyboardMarkup,
                           CallbackQuery,
                           FSInputFile
                           )
from aiogram.types import ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from composite.composite_keyboards import choose_script, choose_libs

router = Router()

@router.callback_query(F.data == 'scripts')
async def scripts_menu_da(callback: CallbackQuery):
    await callback.answer()
    await scripts_menu(callback.message)


@router.callback_query(F.data == 'mtg_mods_libs')
async def libs_scripts(callback: CallbackQuery):
    await callback.answer()
    await libs_menu_choose(callback.message)

async def scripts_menu(message: Message):
    await message.answer(
        text=(
        "<b>📂 Меню скриптов</b>\n\n"
        "Выберите интересующий вас раздел из списка ниже:\n\n"
        "⚠️ <b>Важно:</b> скрипты требуют наличия установленных библиотек <code>Moonloader</code> или <code>Monetloader</code>.\n\n"
        "📖 <b>Гайды:</b> Если не знаете, как устанавливать — откройте раздел «Библиотеки», там есть подробная инструкция.\n\n"
        "💡 <b>Совет:</b> изучайте функционал скриптов поэтапно в карточках товаров.\n\n"
        "🛠 <b>Поддержка:</b> по всем вопросам обновления и помощи пишите "
        "<a href='https://t.me/mtg_mods'>Разработчику</a>."
        ),
        parse_mode ='HTML',
        reply_markup = choose_script())


async def libs_menu_choose(message: Message):
    await message.answer(
        text=(
        '<b>Выбор нужной библиотеки под вашe устройство:</b>\n\n'
        '⚠️ <b>Важно:</b> выбирайте библиотеку для вашего устройства внимательно и устанавливайте ее строго по гайду!\n\n'
        ),
        parse_mode ='HTML',
        reply_markup = choose_libs())