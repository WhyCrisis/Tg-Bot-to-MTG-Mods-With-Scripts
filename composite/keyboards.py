from aiogram import Router, F
from aiogram.filters import Command, callback_data
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
            [InlineKeyboardButton(text='Связаться с разработчиком', url='https://t.me/mtg_mods')],
            [InlineKeyboardButton(text='Ресурсы MTG MODS', callback_data='mtg_mods_info')]
         ],
    )
    return keyboard

def choose_script():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Старые хелперы (заброшены ⚠️)', callback_data='mtg_mods_abandoned')],
            [InlineKeyboardButton(text='Текущие скрипты', callback_data='mtg_mods_actual')],
            [InlineKeyboardButton(text='Библиотеки для установки скриптов', callback_data='mtg_mods_libs')]

        ],
    )
    return keyboard

def choose_libs():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='MonetLoader (Arizona Mobile / Установка MTG Скриптов)', callback_data='arizona_mobile_mtg_libs')],
            [InlineKeyboardButton(text='MonetLoader (Arizona Mobile / Установка ЛЮБЫХ Скриптов)', callback_data='arizona_mobile_libs')],
            [InlineKeyboardButton(text='MoonLoader (ПК)', callback_data='moonloader_lib')],
            [InlineKeyboardButton(text='Родина Мобайл', callback_data='rodina_mobile_libs')]
        ],
    )
    return keyboard
