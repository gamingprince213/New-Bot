import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

# Bot token from environment
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN is not set. Please set it in Render.")

# Set up bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

# 🌟 Keyboard buttons
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(
    KeyboardButton("📄 About"),
    KeyboardButton("📞 Contact"),
    KeyboardButton("❌ Close")
)

# /start command handler
@dp.message_handler(commands=["start"])
async def start_cmd(message: Message):
    await message.answer(
        "👋 Welcome! Choose an option below:",
        reply_markup=keyboard
    )

# Button handler
@dp.message_handler(lambda message: message.text in ["📄 About", "📞 Contact", "❌ Close"])
async def handle_buttons(message: Message):
    if message.text == "📄 About":
        await message.reply("I am a demo Telegram bot made with aiogram 🐍.")
    elif message.text == "📞 Contact":
        await message.reply("Contact developer at: @yourusername")
    elif message.text == "❌ Close":
        await message.reply("Keyboard removed.", reply_markup=types.ReplyKeyboardRemove())

# Echo handler for any other message
@dp.message_handler()
async def echo(message: Message):
    await message.answer(f"🪞 You said: {message.text}")

# Run bot
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
