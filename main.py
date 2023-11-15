import asyncio
import logging
import sys

from aiogram import types
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    FSInputFile,
)

from config import bot, dp, tg_link, inst_link


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    greeting = FSInputFile("greeting.MP4")
    await bot.send_video_note(chat_id=message.chat.id, video_note=greeting)
    button = InlineKeyboardButton(text="Отримати гайд", callback_data="script")
    kb = InlineKeyboardMarkup(inline_keyboard=[[button]])
    await message.answer(
        text="Привіт, друже👋 Радий, що ти не стоїш на місці і бажаєш розвивати свої продажі. Забирай готовий скрипт, який зможеш адаптувати під свою нішу👇",
        reply_markup=kb,
    )


@dp.callback_query(lambda callback: callback.data == "script")
async def send_script(callback: types.CallbackQuery) -> None:
    script_pdf = FSInputFile("script.pdf", filename="Як написати скрипт продажів.pdf")
    await bot.send_document(chat_id=callback.message.chat.id, document=script_pdf)

    button1 = InlineKeyboardButton(text="Instagram", url=inst_link)
    button2 = InlineKeyboardButton(text="Telegram", url=tg_link)

    markup = InlineKeyboardMarkup(inline_keyboard=[[button1, button2]])

    await bot.send_message(
        chat_id=callback.message.chat.id,
        text="Разові знання - це круто🤝 Але ще краще отримувати їх систематично. Підписуйся на мій Інстаграм та Телеграм-канал. Там я постійно ділюсь мега-цінними знаннями і транслюю своє життя та шлях до успіху🚀",
        reply_markup=markup,
    )


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
