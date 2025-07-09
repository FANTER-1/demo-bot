from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

boт = Bot(token="luboy token")
dp = Dispatcher(boт)

@dp.message(Command("start"))
async def start(message: types.Message):
    kb = types.ReplyKeyboardMarkup(keyboard=[
        [types.KeyboardButton(text="Каталоr")],
        [types.KeyboardButton(text="Акции")]
    ], resize_keyboard=True)
    await message.answer("Выберите раздел:", reply_markup=kb)

@dp.message(lambda m: m.text in ["Каталог", "Акции"])
async def handle_buttons(message: types.Message):
    await message.answer(f"Раздел '{message.text}' в разработке ")

if __name__ == '__main__':
    dp.run_polling(boт)