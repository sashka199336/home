import asyncio
import logging
import sys, os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile

from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

#
with open("token.txt") as f:
    TOKEN = f.read().strip()


bot = Bot(token=TOKEN)


dp = Dispatcher()


# Состояния
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


# Клавиатуры
def kb_menu(text: str | list):

    builder = ReplyKeyboardBuilder()
    if isinstance(text, str):
        text = [text]
    [builder.button(text=txt) for txt in text]
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def ikb_menu(text: str | list):

    builder = InlineKeyboardBuilder()
    if isinstance(text, str):
        text = [text]
    [builder.button(text=txt, callback_data=txt) for txt in text]
    return builder.as_markup()


builder = InlineKeyboardBuilder()
[builder.button(text=f'Product{i}', callback_data='product_buying') for i in range(1, 5)]
ikb_buy_menu = builder.as_markup()


# Обработчики команд
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:

    await message.answer("Привет! Я бот помогающий твоему здоровью.",
                         reply_markup=kb_menu(['Рассчитать', 'Информация', 'Купить']))


# Обработчики команд без префикса
@dp.message(F.text.lower().startswith('рассчитать'))
async def main_menu(message: Message) -> None:

    await message.answer("Выберите опцию:",
                         reply_markup=ikb_menu(['Рассчитать норму калорий', 'Формулы расчёта']))


@dp.message(F.text.lower().startswith('купить'))
async def get_buying_list(message: Message) -> None:
    for i in range(1, 5):
        await message.answer(f'Название: Product{i} | Описание: описание {i} | Цена: {i * 100}')
        # await bot.send_photo(message.chat.id, 'product.jpg')
        await message.answer_photo(FSInputFile('product.webp'))
    await message.answer('Выберите продукт для покупки:', reply_markup=ikb_buy_menu)



@dp.callback_query(F.data == 'Формулы расчёта')
async def callback_query_handler(callback: CallbackQuery) -> None:

    await callback.message.answer("10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")
    await callback.answer()


@dp.callback_query(F.data == 'Рассчитать норму калорий')
async def start_calc(callback: CallbackQuery, state: FSMContext) -> None:

    await state.set_state(UserState.age)
    await callback.message.answer("Введите свой возраст:")
    await callback.answer()


@dp.callback_query(F.data == 'product_buying')
async def buy(callback: CallbackQuery) -> None:
    await callback.message.answer('Вы успешно приобрели продукт!')
    await callback.answer()


# Обработчики состояний
@dp.message(UserState.age)
async def set_age(message: Message, state: FSMContext) -> None:

    if message.text.isdigit():
        await state.update_data(age=message.text)
        await state.set_state(UserState.growth)
        await message.answer("Введите свой рост:")
    else:
        await message.answer('Введите число, еще раз:')


@dp.message(UserState.growth)
async def set_growth(message: Message, state: FSMContext) -> None:

    if message.text.isdigit():
        await state.update_data(growth=message.text)
        await state.set_state(UserState.weight)
        await message.answer("Введите свой вес:")
    else:
        await message.answer('Введите число, еще раз:')


@dp.message(UserState.weight)
async def set_weight(message: Message, state: FSMContext) -> None:

    if message.text.isdigit():
        await state.update_data(weight=message.text)
        await state.set_state(UserState.growth)

        data = await state.get_data()
        await state.clear()

        result = float(data["weight"]) * 10 + float(data["growth"]) * 6.25 - float(data["age"]) * 5 + 5
        await message.answer(f'Ваша норма калорий: {result}')
    else:
        await message.answer('Введите число, еще раз:')


# Обработчик любого текстового сообщения
@dp.message()
async def echo_handler(message: Message) -> None:



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
