from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

# Создаем асинхронную функцию
async def set_main_menu(bot: Bot):

    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command='/reclama',
                   description='Хочу заказать рекламу'),
        BotCommand(command='/muzyka',
                   description='Музыкальные предпочтения'),
        BotCommand(command='/otzyvy',
                   description='Оставить отзывы'),
        BotCommand(command='/predlozheniia',
                   description='Напишите ваши предложения'),
        BotCommand(command='/goroskop',
                   description='Что ждет тебя сегодня')
    ]

    await bot.set_my_commands(main_menu_commands, language_code='ru', scope=BotCommandScopeDefault())


