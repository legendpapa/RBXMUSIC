from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from config import *
from PURVIMUSIC import app
from PURVIMUSIC.core.call import PURVI
from PURVIMUSIC.utils import bot_sys_stats
from PURVIMUSIC.utils.decorators.language import language
from PURVIMUSIC.utils.inline import supp_markup
from config import BANNED_USERS


@app.on_message(filters.command("mping", prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_photo(
        photo="https://files.catbox.moe/quiycz.jpg",
        caption=_["ping_1"].format(app.mention),
    )
    pytgping = await PURVI.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )
