rom aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio


api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


# Запускается только тогда, когда написана команда '/start' в чате с ботом
@dp.message_handler(commands=['start'])
async def start_message(message):
    # Ответ бота в чате телеграм
    await message.answer("Привет! Я бот, помогающий твоему здоровью")


# Запускается при любом обращении. Не описаном ранее.
@dp.message_handler()
async def all_message(message):
    await message.answer("Введите команду /start, чтобы начать общение")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
