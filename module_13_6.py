from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = "7338414504:AAF_qkRMXWLwCI-9JehERGoyo3wLRg-VSYk"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(resize_keyboard=True)
bottom = KeyboardButton(text='Рассчитать')
bottom2 = KeyboardButton(text='Информация')
kb.row(bottom, bottom2)
inline_kb = InlineKeyboardMarkup()
inline_bottom1 = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
inline_bottom2 = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
inline_kb.row(inline_bottom1, inline_bottom2)


class UserState(StatesGroup):
    weight = State()
    growth = State()
    age = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет', reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=inline_kb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = (10 * int(data["weight"])) + (6.25 * int(data["growth"])) - (5 * int(data["age"])) + 5
    await message.answer(f"Калорий для оптимального похудения {calories}")
    await state.finish()


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
