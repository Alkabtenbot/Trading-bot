import os
import requests
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_btc_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    return float(requests.get(url).json()["price"])

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("أهلاً! ابعت /price لتعرف سعر BTC")

@dp.message(Command("price"))
async def price(message: types.Message):
    price = get_btc_price()
    await message.answer(f"BTC Price: ${price:,.2f}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
