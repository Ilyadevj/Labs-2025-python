import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

TOKEN = "8530282914:AAGL_N6PdjHhDUvsAlhDh9HMMrUxUfwPawc"

users_data = []

class UserState(StatesGroup):
    name = State()
    age = State()

async def start(message: types.Message, state: FSMContext):
    await message.answer("Введите ваше имя:")
    await state.set_state(UserState.name)

async def get_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите ваш возраст (только число):")
    await state.set_state(UserState.age)

async def get_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Возраст должен быть числом. Попробуйте ещё раз:")
        return

    data = await state.get_data()
    age = int(message.text)

    users_data.append({
        "name": data["name"],
        "age": age
    })

    await message.answer(
        f"Данные сохранены:\nИмя: {data['name']}\nВозраст: {age}"
    )

    await state.clear()

async def show_all(message: types.Message):
    if not users_data:
        await message.answer("Данных пока нет")
        return

    result = "Список пользователей:\n"
    for user in users_data:
        result += f"{user['name']} — {user['age']} лет\n"

    await message.answer(result)

async def main():
    print("Бот запущен")
    bot = Bot(token=TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    dp.message.register(start, Command("start"))
    dp.message.register(show_all, Command("all"))
    dp.message.register(get_name, UserState.name)
    dp.message.register(get_age, UserState.age)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
