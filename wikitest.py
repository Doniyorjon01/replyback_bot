import logging
import asyncio
import wikipedia
from aiogram import Dispatcher, Bot, types, filters

API_TOKEN = '7091779161:AAFEgyvcWK_eOZo8Spx_UiNkZf-P7NvbFfQ'
wikipedia.set_lang('uz')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(filters.command.Command('start'))
async def send_welcome(message: types.Message):
    await message.reply('Hi. I am WikiBot')


@dp.message()
async def send_wiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.reply(respond)
    except Exception as e:
        await message.reply(f'Bunday maqola mavjud emas! error: {e}')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
