#---
from composite.texts_main import *
from composite.keyboards import *
#---

router = Router()

@router.message(Command('start'))
async def start(message: Message):
    photo = FSInputFile('neccessaryfiles/pictures/startpic.png')
    text = (
        'Данный бот создан для удобного скачивания скриптов и библиотек автора <b>MTG MODS</b>!\n'
        'Скрипты полностью защищены и портируются полностью с гитхаба разработчика и с его ГитХаба\n\n\n'
        'Данный бот был разработан @bartelliada с использованием данных взятых с канала <a href="https://t.me/mtgmods">Богдана</a>\n'
        'Для активации нажмите кнопку ниже и следуйте инструкциям!'
    )
    await message.answer_photo(photo = photo, caption= text,parse_mode='HTML', reply_markup = start_message_inline_keyboard())


@router.callback_query(F.data == 'perehod')
async def perehod_callback(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        text='Вы переходите на ТГ-Канал MTG MODS!\n Бот станет доступным после подписки! \nНажмите на кнопку ниже для подписки а затем подтвердить:',
        reply_markup=sub_message_inline_keyboard())


async def main_menu(message: Message):
    photo = FSInputFile('neccessaryfiles/pictures/mainmenu.png')
    text = (
        '🤖 Главное меню MTG MODS\n'
        'Здесь собраны самые актуальные скрипты для автоматизации а также необходимые модификации.\n'
        'Навигация по боту: \n\n'
        '🔸 Скачать скрипты — готовые конфигурации и автоматизация.\n\n'
        '🔸 Библиотеки — всё что нужно для работы софтов. \n\n'
        '🔸 Гайды — подробные инструкции по установке и настройке. \n\n'
        '🔸 Наш чат — Чат с другими пользователями\n\n'
        '🔸 Связаться с разработчиком\n\n'
        '👇 Выберите интересующий раздел:'
    )
    await message.bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=text,
        reply_markup=main_butons())

@router.callback_query(F.data == 'activate_bot')
async def activate_bot(callback: CallbackQuery):
    await callback.answer()
    await main_menu(callback.message)

@router.callback_query(F.data == 'back_choose')
async def back_choose(callback: CallbackQuery):
    await callback.answer()
    await scripts_menu (callback.message)

@router.callback_query(F.data == 'back_start')
async def back_startss(callback: CallbackQuery):
    await main_menu(callback.message)