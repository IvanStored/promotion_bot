from os import getenv
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from dotenv import load_dotenv

load_dotenv()

TOKEN = getenv("TOKEN")
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
tg_link = getenv("TG_LINK")
inst_link = getenv("INST_LINK")
dp = Dispatcher()
