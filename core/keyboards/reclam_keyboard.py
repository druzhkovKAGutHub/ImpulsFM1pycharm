from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

reclam_text_cancel = "Размещение рекламы закончил"

reclam_keyboard = [
        [
            KeyboardButton(text=reclam_text_cancel)   
        ],
    ]

reclam_keyboard = ReplyKeyboardMarkup(keyboard=reclam_keyboard, resize_keyboard=True, one_time_keyboard=False)