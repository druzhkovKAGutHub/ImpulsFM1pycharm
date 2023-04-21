from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

loc_tel_poll_keybord = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Отправить геолокацию',request_location=True)],
                                                     [KeyboardButton(text='Отправить свой контакт', request_contact=True)],
                                                     [KeyboardButton(text='Создать опрос', request_poll=KeyboardButtonPollType(type='quiz'))]
    ], resize_keyboard=True, one_time_keyboard=False, input_field_placeholder='Отправте локация, номер телефона или создайте опрос'
                                                     )