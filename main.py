import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN не найден")

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    me = await bot.get_me()
    logging.info(f"Bot started: @{me.username}")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
