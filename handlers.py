from aiogram.types import Message, ContentType
from aiogram.types import PreCheckoutQuery, LabeledPrice
from aiogram.dispatcher.filters import Command
from aiogram import types

from bot import bot, dp
# from config import PAYMENTS_TOKEN

from keyboards import keyboard

import requests


# PRICE = {
#	 '1': [LabeledPrice(label='Item1', amount=1000000)],
#	 '2': [LabeledPrice(label='Item2', amount=2000000)],
#	 '3': [LabeledPrice(label='Item3', amount=3000000)],
#	 '4': [LabeledPrice(label='Item4', amount=4000000)],
#	 '5': [LabeledPrice(label='Item5', amount=5000000)],
#	 '6': [LabeledPrice(label='Item6', amount=6000000)]
# }


@dp.message_handler(Command('start'))
async def start(message: Message):
	await bot.send_message(message.chat.id,
						   'Тестируем WebApp', reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('http'))
async def process_callback_http(callback_query: types.CallbackQuery):
	url = "http://127.0.0.1:8000/api/v1/women/"
	response = requests.get(url)

	await bot.send_message(callback_query.from_user.id, response.text)