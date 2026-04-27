from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_menu_keyboard(lang: str = "en"):
    if lang == "ru":
        return ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Получить курс сейчас")],
                [KeyboardButton(text="Настройки")]
            ],
            resize_keyboard=True
        )

    if lang == "uz":
        return ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Hozir kursni olish")],
                [KeyboardButton(text="Sozlamalar")]
            ],
            resize_keyboard=True
        )

    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Get current prices now")],
            [KeyboardButton(text="Settings")]
        ],
        resize_keyboard=True
    )
