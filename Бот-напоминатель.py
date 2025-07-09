from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import logging
from datetime import datetime

bot = Bot(token="luboy token")
dp = Dispatcher(bot)

# Временная история ( автоматическое бд )
demo_reminders = {}


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "напоминалка\n\n"
        "Пример командыю:\n"
        "• 'напомнить о закупки еды'\n"
        "• 'Моя история'"
    )


@dp.message()
async def handle_message(message: types.Message):
    try:
        if "напомни" in message.text.lower():
            # Имитация напоминалки
            demo_reminders[message.from_user.id] = message.text
            await message.answer("напоминаlка создано (основная версия сохраняет на 3 дня)")

        elif message.text.lower() == "моя истоиR":
            reminders = demo_reminders.get(message.from_user.id, "Нет напоминаний")
            await message.answer(f"📝 Вашша история (демо):\n{reminders}")

    except Exception:
        await message.answer("Ошибка. Формат: 'Напомни [текст] в [время]'")


if __name__ == '__main__':
    logging.info("R запущен!")
    dp.run_polling(bot)