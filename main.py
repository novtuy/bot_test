from aiogram import Bot, Dispatcher, types
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.filters import Command
import asyncio
import logging
import os

logging.basicConfig(level=logging.INFO)

API_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Команда /start
@dp.message(Command(commands=["start"]))
async def start(msg: types.Message):
    await msg.answer("Привет! Я бот-повторялка. Напиши что-нибудь — и я повторю!")

# Эхо всех сообщений
@dp.message()
async def echo(msg: types.Message):
    await msg.answer(msg.text)

# Запуск бота
async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
