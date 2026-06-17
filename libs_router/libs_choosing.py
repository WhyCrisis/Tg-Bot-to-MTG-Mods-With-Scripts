from aiogram import Router
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


from libs_router.libs_text import text_mtg_mod


router = Router()

@router.callback_query(F.data == 'arizona_mobile_mtg_libs')
async def ar_mtg_lib(callback: CallbackQuery):
    await callback.answer()
    await text_mtg_mod(callback.message)




