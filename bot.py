import asyncio
import logging
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats
from aiogram.filters.command import Command
from dotenv import dotenv_values

config = dotenv_values(".env")
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config["TG_TOKEN"])
# Диспетчер
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Создать турнир"),
            types.KeyboardButton(text="Помощь"),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer(
        "Привет, ты зашел в бота Rctournaments4all, что бы ты хотел сделать?",
        reply_markup=keyboard,
    )


@dp.message(F.text == "Помощь")
async def start(message: types.Message):
    await message.answer("Ты молодец, у тебя все получится!")


@dp.message(F.text == "Создать турнир")
async def start(message: types.Message):
    await message.answer(
        "Введите имена пилотов одним сообщением в порядке резултатов квалификации (от 1 места до последнего)."
    )


@dp.message()
async def tournament_cereator(message: types.Message):
    racers = message.text
    list_of_racers = racers.split()
    await message.answer(f"list_of_racers={list_of_racers}")


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
