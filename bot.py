"""
This is a echo bot.
It echoes any incoming text messages.
"""

from aiogram import Bot, Dispatcher, types, filters

import asyncio
import logging

API_TOKEN = '7245640213:AAEQ2dLJuQFecEKHNnKW8aVQFPGA5Nc6XFk'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(filters.command.Command('start'))
async def send_welcome(message: types.Message):
    await message.reply('Hi. I am Basic bot')

@dp.message()
async def sendWiki(message: types.Message):
    respond = message.text
    await message.answer(respond)

async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())
