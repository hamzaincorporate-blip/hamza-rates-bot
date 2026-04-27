from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.keyboards.assets import get_assets_keyboard
from app.storage.memory import users

router = Router()


@router.callback_query(F.data.startswith("set_lang_"))
async def set_language(callback: CallbackQuery):
    user_id = callback.from_user.id

    if user_id not in users:
        users[user_id] = {"lang": "en", "assets": []}

    lang = callback.data.replace("set_lang_", "")
    users[user_id]["lang"] = lang

    if lang == "ru":
        text = "Пожалуйста, выберите один или несколько активов:"
    elif lang == "uz":
        text = "Iltimos, bir yoki bir nechta aktivni tanlang:"
    else:
        text = "Please choose one or more assets:"

    await callback.message.edit_text(
        text,
        reply_markup=get_assets_keyboard(users[user_id]["assets"])
    )
    await callback.answer()
