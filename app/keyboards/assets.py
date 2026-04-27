from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.data.assets import ASSETS


def get_assets_keyboard(selected_assets: list[str]):
    rows = []

    for ticker in ASSETS.keys():
        checked = "✅ " if ticker in selected_assets else ""
        rows.append([
            InlineKeyboardButton(
                text=f"{checked}{ticker}",
                callback_data=f"toggle_asset_{ticker}"
            )
        ])

    rows.append([
        InlineKeyboardButton(text="Next", callback_data="assets_next")
    ])

    return InlineKeyboardMarkup(inline_keyboard=rows)
