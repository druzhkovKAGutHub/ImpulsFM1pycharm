import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import BotCommandScopeDefault, KeyboardButtonPollType, ReplyKeyboardRemove, Message, ContentType, CallbackQuery
from aiogram.filters.command import Command, CommandObject
from aiogram.filters import Text
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.enums import ParseMode
import core.menu.basic as m_base
import PostgreImpulsFM as ps	
from config_reader import config
#from core.keyboards.reclam_keyboard import *
import core.keyboards.reclam_keyboard as rec_key
import core.keyboards.muzyka_keyboard as muz_key
import core.keyboards.goroskop_keybort as gor_keyb
import core.keyboards.othe_keyboard as othe_key
import core.web.get_text_horoscope as text_gor

user: dict = {'which_section': ""}

#API_TOKEN = '6271475626:AAG3g1nvJCvOIUMKXNiQlFqJsRRP5wGekv8'
#bot = Bot(token=config.bot_token.get_secret_value())
API_TOKEN = config.bot_token.get_secret_value()#'6150937954:AAFpU39nfdMhZcpPN4PewwXFuy-DUDLxFag'
ad = config.admin_id


bot = Bot(token=API_TOKEN)
dp = Dispatcher()

async def haderImpulsFM(message: types.Message):
    await message.answer_photo(photo="https://impulsfm.ru/wp-content/uploads/2023/03/cropped-%D0%98%D0%BC%D0%BF%D1%83%D0%BB%D1%8C%D1%81FM-logo-%D1%81%D0%B0%D0%B9%D1%82.png")


@dp.message(Command('reclama'))
async def reclamaInLineKeyBord(message: Message):
    user['which_section']="reclama"
    await haderImpulsFM(message)
    await message.answer(text='Оставте свои контакты. Напишите кратко, что хотели рекламировать.', reply_markup=rec_key.reclam_keyboard) 
    
@dp.message(Command('muzyka'))
async def muzykaInLineKeyBord(message: Message):
    user['which_section']="muzyka"
    await haderImpulsFM(message)
    await message.answer("Привет, "+message.from_user.first_name+
                         "!😉\n♾В эфире радио📻 Импульс FM🎶.\nЕсли вы хотите  услышать любимую песню💃 и передать привет родным, друзьям, коллегам,  всем-всем-всем👋, пожаловаться или похвалить нас,  скорее, скорее, скорее звоните📞 и оставляйте ваши пожелания🧑‍💻.\n Куда хотите перейти?"
                         ,reply_markup=muz_key.muzyka_keyboard)
    await message.answer(text='Напишите название песни.') #,reply_markup=loc_tel_poll_keybord

@dp.message(Command('otzyvy'))
async def otzyvyInLineKeyBord(message: Message):
    user['which_section']="otzyvy"
    await haderImpulsFM(message)    
    await message.answer(text='Что вы скажете о нашем радио.')

@dp.message(Command('predlozheniia'))
async def predlozheniiaInLineKeyBord(message: Message):
    user['which_section']="predlozheniia"
    await haderImpulsFM(message)
    await message.answer(text='Что бы вы хотели еще улышать на нашем радио.')

@dp.message(Command('goroskop'))
async def goroskopKeyBord(message: Message):
    user['which_section']="goroskop"
    await haderImpulsFM(message)
    await message.answer(text='Привет. выбери свой знак задиака', reply_markup=gor_keyb.get_zodiac_keyboard())

@dp.callback_query()
async def get_horoscope(call: CallbackQuery):
    await call.answer()
    zodiac = call.data
    text = await text_gor.get_text_horoscope(zodiac=zodiac)
    await call.message.edit_text(text=text, reply_markup=gor_keyb.get_zodiac_keyboard())

# Здесь F - это message

@dp.message(F.photo)
async def photo_msg(message: Message):    
    await message.answer("Это точно какое-то изображение! Но я их не сохраняю себе.")
    #await m_base.get_photo(message=message, bot=bot)

@dp.message(Text(text=[rec_key.reclam_text_cancel,muz_key.muzyka_text_cancel],ignore_case=True))
async def RemuveKeyBord(message: Message):
    ps.PostgreSQLWorker(message,bot, user["which_section"])
    if rec_key.reclam_text_cancel == message.text:
        await message.answer(text='Ваша реклама приянта. Спасибо за размещение.',reply_markup=ReplyKeyboardRemove())
    elif muz_key.muzyka_text_cancel == message.text:
        await message.answer(text='Спасибо. Мы учтем ваше предпочтение.',reply_markup=ReplyKeyboardRemove())


@dp.message()
async def with_puree(message: Message):
    if user['which_section']=='':
        await message.answer('Для начала работы по кнопочке "Меню" выберете раздел!')
    else:     
        #ps.PostgreSQLWorker(message,bot, user["which_section"])
        pass
    


async def stop_bot(bot:Bot):
    await bot.send_message(873646319, text='Бот остановлен!')

async def start_bot(bot:Bot):
    await bot.send_message(873646319,text='Бот запущен')

# Запуск процесса поллинга новых апдейтов
async def main():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                                "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )
    await bot.delete_webhook(drop_pending_updates=True)
    #dp.include_router(router=router)
    dp.startup.register(m_base.set_main_menu)
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    
 #   dp.message.register(m_base.get_photo, Command(commands='photo'))
#    dp.message.register(m_base.get_photo, Command(commands='audio'))
#    dp.message.register(m_base.get_photo, Command(commands='document'))
#    dp.message.register(m_base.get_photo, Command(commands='mediagroup'))
 #   dp.message.register(m_base.get_photo, Command(commands='photo'))
#    dp.message.register(m_base.get_photo, Command(commands='sticker'))
#    dp.message.register(m_base.get_photo, Command(commands='video'))
#    dp.message.register(m_base.get_photo, Command(commands='video_note'))
#    dp.message.register(m_base.get_photo, Command(commands='voice'))
    
    #dp.message.register(get_location, ContentTypeFilte)
    try:
        await dp.start_polling(bot)    
    finally :
        await bot.session.close()   

if __name__ == "__main__":
    asyncio.run(main())
