from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
import os

# Включаем логирование
# logging.basicConfig(level=logging.INFO)

# Токен бота
API_TOKEN = os.getenv("BOT_TOKEN")

# Создаем объекты бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Команда /start
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.reply("Привет! Я бот-повторялка. Напиши мне что-нибудь — и я повторю!")

# Все остальные сообщения
@dp.message_handler()
async def echo_message(message: types.Message):
    # Просто повторяем текст пользователя
    await message.reply(message.text)

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
