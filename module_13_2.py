from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.utils import executor

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await bot.send_message(chat_id=message.from_user.id, text='Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')
    await bot.send_message(chat_id=message.from_user.id, text='Введите команду /start, чтобы начать общение.')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
