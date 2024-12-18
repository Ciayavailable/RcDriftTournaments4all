import asyncio
import logging

from aiogram import Bot, Dispatcher, F, types
from aiogram.filters.command import Command
from aiogram.types import FSInputFile
from dotenv import dotenv_values
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram import F
from aiogram.types import CallbackQuery

from utils import get_runs, setka_creator_8, setka_jpg

config = dotenv_values(".env")
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config["TG_TOKEN"])  # type: ignore
# Диспетчер
dp = Dispatcher()

# Создаем объекты инлайн-кнопок



async def set_main_menu(bot: Bot):

    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command='/help',
                   description='Справка по работе бота'),
        BotCommand(command='/support',
                   description='Поддержка'),
        BotCommand(command='/contacts',
                   description='Другие способы связи'),
        BotCommand(command='/tournament',
                   description='Создать турнир')
    ]

    await bot.set_my_commands(main_menu_commands)
    
dp.startup.register(set_main_menu)


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет, ты зашел в бота Rctournaments4all, что бы ты хотел сделать?",
    )



@dp.message(Command("help"))
async def help(message: types.Message):
    await message.answer("Нажми на кнопку 'Создать турнир' или нажми на команду /tournament в меню.")
    
@dp.message(Command("support"))
async def help(message: types.Message):
    await message.answer("Тг для связи с поддержкой @twentypeek")

@dp.message(Command("contacts"))
async def help(message: types.Message):
    await message.answer("Номер для связи с админом +7(912)048-31-53")
    
@dp.message(Command("tournament"))
async def help(message: types.Message):
    await message.answer("Введите имена пилотов одним сообщением в порядке результатов квалификации (от 1 места до последнего).")

@dp.message(F.text == "Создать турнир")
async def start(message: types.Message):
    await message.answer(
        "Введите имена пилотов одним сообщением в порядке резултатов квалификации (от 1 места до последнего)."
    )


@dp.message()
async def tournament_cereator(message: types.Message):
    racers = message.text
    list_of_racers = racers.split()
    setka = setka_creator_8(list_of_racers)
    runs = get_runs(setka)
    for run in runs:
        await message.answer(f"run={run}")
    setka_jpg(setka)
    # Отправка файла из файловой системы
    image_from_pc = FSInputFile("result.jpg")
    result = await message.answer_photo(
        image_from_pc, caption="Изображение из файла на компьютере"
    )
    # await message.answer(f"list_of_racers={list_of_racers}")


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
