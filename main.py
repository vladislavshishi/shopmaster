import os
import logging
import asyncio

from aiogram import F
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.enums.parse_mode import ParseMode
from aiogram.types.web_app_info import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

logging.basicConfig(level=logging.DEBUG)

load_dotenv()
bot = Bot(os.getenv('TOKEN'), parse_mode=ParseMode.HTML)
dp = Dispatcher(bot=bot)


@dp.message(Command("start"))
async def start(message: types.Message):
	buttons = [
		[
			types.KeyboardButton(text="/start"),
			types.KeyboardButton(text="/contacts")
		],
		[
			types.KeyboardButton(text="/id"),
			types.KeyboardButton(text="/help")
		]
	]

	markup = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

	await message.answer(f'<b><i>{message.from_user.first_name}</i></b>, добро пожаловать!',
						 reply_markup=markup)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
	asyncio.run(main())
