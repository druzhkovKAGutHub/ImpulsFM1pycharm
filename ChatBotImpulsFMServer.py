import asyncio
#import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import BotCommand, BotCommandScopeDefault, WebAppInfo
from aiogram.filters.command import Command
from aiogram.filters import Text
from aiogram.utils.keyboard import InlineKeyboardBuilder

API_TOKEN = '6150937954:AAFpU39nfdMhZcpPN4PewwXFuy-DUDLxFag'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Хочу выбрать и перейти")            
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Нажмите для перехода кнопочку ниже"
    )
    await message.answer_photo(photo="https://impulsfm.ru/wp-content/uploads/2023/03/cropped-%D0%98%D0%BC%D0%BF%D1%83%D0%BB%D1%8C%D1%81FM-logo-%D1%81%D0%B0%D0%B9%D1%82.png")
    await message.answer("Привет, "+message.from_user.first_name+"!😉\n♾В эфире радио📻 Импульс FM🎶.\nЕсли вы хотите  услышать любимую песню💃 и передать привет родным, друзьям, коллегам,  всем-всем-всем👋, пожаловаться или похвалить нас,  скорее, скорее, скорее звоните📞 и оставляйте ваши пожелания🧑‍💻.\n Куда хотите перейти?", reply_markup=keyboard)
    

@dp.message(Text("Хочу выбрать и перейти"))
async def with_puree(message: types.Message):
    #await message.reply("Отличный выбор!")
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Реклама", url="https://t.me/adv_impulsfm")
    )
    builder.row(types.InlineKeyboardButton(
        text="Музыкальные предпочтения",
        url="https://t.me/music_impulsfm")
    )

    builder.row(types.InlineKeyboardButton(
        text="Отзывы",
        url="https://t.me/feedback_impulsfm")
    )

    builder.row(types.InlineKeyboardButton(
        text="Предложения",
        url="https://t.me/wishes_impulsfm")
    )

    await message.answer(
        message.from_user.first_name+' - жми для перехода',
        reply_markup=builder.as_markup(),
    )
    
# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)    

if __name__ == "__main__":
    asyncio.run(main())    