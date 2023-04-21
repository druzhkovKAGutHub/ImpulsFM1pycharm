from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

muzyka_text_cancel = "Размещение предпочтения закончил"

muzyka_keyboard = [
        [
            KeyboardButton(text=muzyka_text_cancel)            
        ],
    ]

muzyka_keyboard = ReplyKeyboardMarkup(keyboard=muzyka_keyboard,resize_keyboard=True, one_time_keyboard=False)