from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def run_result_keyboard(pilot1: str, pilot2: str, run_number: int):
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text=pilot1, callback_data=pilot1))
    keyboard.add(InlineKeyboardButton(text=pilot2, callback_data=pilot2))
    keyboard.adjust(2)
    return keyboard.as_markup(resize_keyboard=True)
    