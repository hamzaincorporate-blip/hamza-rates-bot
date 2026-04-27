import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app.handlers.start import router as start_router
from app.handlers.onboarding import router as onboarding_router
from app.handlers.assets import router as assets_router
from app.handlers.finish_setup import router as finish_setup_router
from app.handlers.prices import router as prices_router

load_dotenv()
logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN не найден")

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(onboarding_router)
    dp.include_router(assets_router)
    dp.include_router(finish_setup_router)
    dp.include_router(prices_router)

    me = await bot.get_me()
    logging.info(f"Bot started: @{me.username}")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
