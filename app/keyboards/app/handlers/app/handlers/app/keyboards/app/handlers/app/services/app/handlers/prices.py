from aiogram import Router, F
from aiogram.types import Message

from app.services.coingecko import get_prices
from app.storage.memory import users
from app.data.assets import ASSETS

router = Router()


@router.message(F.text.in_(["Get current prices now", "Получить курс сейчас", "Hozir kursni olish"]))
async def send_prices(message: Message):
    user_id = message.from_user.id

    if user_id not in users:
        users[user_id] = {"lang": "en", "assets": []}

    lang = users[user_id]["lang"]
    selected_assets = users[user_id]["assets"]

    if not selected_assets:
        if lang == "ru":
            await message.answer("Сначала, пожалуйста, выберите хотя бы один актив через /start.")
        elif lang == "uz":
            await message.answer("Avval /start orqali kamida bitta aktiv tanlang.")
        else:
            await message.answer("Please choose at least one asset first via /start.")
        return

    try:
        data = await get_prices(selected_assets)

        if lang == "ru":
            header = "Актуальные курсы:"
            updated = "Обновлено"
        elif lang == "uz":
            header = "Joriy kurslar:"
            updated = "Yangilandi"
        else:
            header = "Current prices:"
            updated = "Updated"

        lines = [header, ""]

        for ticker in selected_assets:
            coin_id = ASSETS[ticker]
            coin_data = data.get(coin_id, {})
            usd = coin_data.get("usd", "n/a")
            change = coin_data.get("usd_24h_change", "n/a")
            ts = coin_data.get("last_updated_at", "n/a")

            if isinstance(change, (int, float)):
                change = f"{change:+.2f}%"

            lines.append(f"• {ticker}: ${usd} | 24h: {change}")

        lines.append("")
        lines.append(f"{updated}: {ts}")

        await message.answer("\n".join(lines))

    except Exception:
        if lang == "ru":
            await message.answer("Извините, данные по курсам временно недоступны.")
        elif lang == "uz":
            await message.answer("Kechirasiz, kurs ma’lumotlari vaqtincha mavjud emas.")
        else:
            await message.answer("Sorry, price data is temporarily unavailable.")
