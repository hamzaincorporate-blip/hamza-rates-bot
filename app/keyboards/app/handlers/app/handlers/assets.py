from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.keyboards.assets import get_assets_keyboard
from app.storage.memory import users

router = Router()


@router.callback_query(F.data.startswith("toggle_asset_"))
async def toggle_asset(callback: CallbackQuery):
    user_id = callback.from_user.id
    ticker = callback.data.replace("toggle_asset_", "")

    if user_id not in users:
        users[user_id] = {"lang": "en", "assets": []}

    selected_assets = users[user_id]["assets"]

    if ticker in selected_assets:
        selected_assets.remove(ticker)
    else:
        selected_assets.append(ticker)

    await callback.message.edit_reply_markup(
        reply_markup=get_assets_keyboard(selected_assets)
    )
    await callback.answer()
