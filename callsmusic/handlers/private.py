# Calls Music 2 - Telegram bot for streaming audio in group calls
# Copyright (C) 2021  Roj Serbest
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from pyrogram import Client
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import Message

from ..helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""I let you play music in your group’s voice chat.

The commands I currently support are:

/play - play the replied audio file or YouTube video
/pause - pause the audio stream
/resume - resume the audio stream
/skip - skip the current audio stream
/stop - clear the queue and remove the userbot from the call
/channel - set chat channel (once set, the bot will play in that channel’s call)
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        'Add me to your Group', url='https://t.me/Vchatprobot?startgroup=true',
                    ),
                    InlineKeyboardButton(
                        'Add my assistant', url='https://t.me/me_iz_zero',
                    ),
                ],
            ],
        ),
    )
