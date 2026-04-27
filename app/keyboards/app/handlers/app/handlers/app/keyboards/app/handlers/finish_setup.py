from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.keyboards.menu import get_main_menu_keyboard
from app.storage.memory import users

router = Router()


@router.callback_query(F.data == "assets_next")
async def finish_setup(callback: CallbackQuery):
    user_id = callback.from_user.id

    if user_id not in users:
        users[user_id] = {"lang": "en", "assets": []}

    lang = users[user_id]["lang"]
    selected_assets = users[user_id]["assets"]

    if not selected_assets:
        if lang == "ru":
            text = "Пожалуйста, выберите хотя бы один актив."
        elif lang == "uz":
            text = "Iltimos, kamida bitta aktivni tanlang."
        else:
            text = "Please choose at least one asset."

        await callback.answer(text, show_alert=True)
        return

    if lang == "ru":
        done_text = "Готово. Ваши настройки сохранены. Мы будем отправлять курсы по расписанию."
        menu_text = "Главное меню:"
    elif lang == "uz":
        done_text = "Tayyor. Sozlamalaringiz saqlandi. Kurslarni jadval bo‘yicha yuboramiz."
        menu_text = "Asosiy menyu:"
    else:
        done_text = "Done. Your settings have been saved. We will send crypto prices on schedule."
        menu_text = "Main menu:"

    await callback.message.edit_text(done_text)
    await callback.message.answer(
        menu_text,
        reply_markup=get_main_menu_keyboard(lang)
    )
    await callback.answer()
