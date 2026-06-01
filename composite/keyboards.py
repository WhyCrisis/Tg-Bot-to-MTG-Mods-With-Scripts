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

router = Router()

def start_message_inline_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
        [InlineKeyboardButton(text='Телеграм канал Богдана', callback_data='perehod')],

        ],
    )
    return keyboard

def sub_message_inline_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Открыть канал", url="https://t.me/mtgmods")],
            [InlineKeyboardButton(text='✅Я подписался✅', callback_data='activate_bot')]

         ],
    )
    return keyboard

def main_butons():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Скачать скрипт", callback_data='scripts')],
            [InlineKeyboardButton(text='Библиотеки',callback_data ='libs')],
            [InlineKeyboardButton(text='Гайды', callback_data='Guides')],
            [InlineKeyboardButton(text='Наш чат', url='https://discord.gg/qBPEYjfNhv' )],
            [InlineKeyboardButton(text='Связаться с разработчиком', url='https://t.me/mtg_mods')]
         ],
    )
    return keyboard

