from time import perf_counter

from pyrogram import Client, filters
from pyrogram.types import Message

from utils.misc import modules_help, prefix


@Client.on_message(filters.command(["ping", "p"], prefix) & filters.me)
async def ping(_, message: Message):
    start = perf_counter()
    await message.edit("<b>Your ping:</b>")
    end = perf_counter()
    await message.edit(f"<b>Your ping: {round(end - start, 3)}s</b>")


modules_help["ping"] = {
    "ping": "Check ping to Telegram servers",
}
