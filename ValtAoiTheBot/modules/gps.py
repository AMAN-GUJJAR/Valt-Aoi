import os
from pyrogram import Client, filters
from pyrogram.types import *

from ValtAoiTheBot.conf import get_str_key
from ValtAoiTheBot import pbot

REPO_TEXT = "**A Powerful [BOT](https://telegra.ph/file/980cd3c855f8e7c0bcdc9.jpg) to Make Your Groups Secured and Organized ! My friend : 『 [Free De la hoya](t.me/FreedelahoyaRobot) 』\n╭──────────────\n┣─ » Python ~ 3.8.6\n┣─ » Update ~ Recently\n╰──────────────\n\n»»» @Pegasusupdates «««"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("ʀᴇᴘᴏꜱɪᴛᴏʀʏ", url=f"https://github.com/ValtAoiTheBot/ValtAoiTheBot"),
        InlineKeyboardButton(" ᴊᴏɪɴ ", url=f"https://t.me/ValtAoitheBotHero"),
      ],[
        InlineKeyboardButton(" Pegasus Network ", url="https://t.me/PegasusXteam"),
        InlineKeyboardButton("Pegasus Support ", url="https://t.me/pegasussupportofficial"),
      ],[
        InlineKeyboardButton(" Pegasus Updates ", url="https://t.me/Pegasusupdates"),
        InlineKeyboardButton(" My friend ", url="https://t.me/FreedelahoyaRobot"),
      ]]
    )
  
  
@pbot.on_message(filters.command(["source"]))
async def repo(pbot, update):
    await update.reply_text(
        text=REPO_TEXT,
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
