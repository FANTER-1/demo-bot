from aiogram import Bot, Dispatcher, types
import asyncio  # Имитация парсера

bot = Bot(token="luboy token")
dp = Dispatcher(bot)

@dp.message(Command("news"))
async def fake_parser(message: types.Message):
    news = [
        "Новость 1: Запуск нового сервиса",
        "Новость 2: Изменения в тарифах"
    ]
    await message.answer(" Последние новости:\n\n" + "\n\n".join(news))

if __name__ == '__main__':
    dp.run_polling(bot)