#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (C) PR0FESSOR-99

import os
from config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

USERNAME=Config.BOT_USERNAME


# start_Msg, help_msg, about_msg
# Team Mrkt Tech
MRKT = "@Tiyaan_bots"


@Client.on_message(filters.private & filters.command("start"))
async def start_meg(client, update):
    text = f"""<b> 👋Hello {update.from_user.mention}\n\nI am an AutoCaption bot\n\nAll you have to do is add me to your channel and I will show you my power\n\nFor more info check help Button\n\n {MRKT}</b>"""
    reply_markup =  InlineKeyboardMarkup( [[
        InlineKeyboardButton("help↗️", callback_data="heroku"),
        InlineKeyboardButton("🗣️Group", url="t.me/CinemaCompanyMovie"),
        InlineKeyboardButton("Channel📢", url="t.me/Tiyaan_bots")
        ]]
    )
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
  )

@Client.on_callback_query(filters.regex(r"^(heroku|about|motech)$"))
async def callback_data(client, update: CallbackQuery):

    query_data = update.data

    if query_data == "heroku":
        buttons = [[
            InlineKeyboardButton("🏠Home", url=f"https://t.me/{USERNAME}?start=start"),
            InlineKeyboardButton("❌️Close", callback_data="motech"),
            InlineKeyboardButton("About↗️", callback_data="about")
            ]]
    
        reply_markup = InlineKeyboardMarkup(buttons)

        await update.message.edit_text(
            f"""<b>🔻CCAutoCaption Bot🔻</b>""",
            reply_markup=reply_markup,
            parse_mode="html"
        )

    if query_data == "about":
        buttons = [[
            InlineKeyboardButton("🗣️Group", url="t.me/CinemaCompanyMovie"),
            InlineKeyboardButton("Channel📢", url="t.me/Tiyaan_bots"),
            InlineKeyboardButton("📃Bot List", url="t.me/Tiyaan_bots")
            ],[
            InlineKeyboardButton("🏠Home", url=f"https://t.me/{USERNAME}?start=start"),
            InlineKeyboardButton("🔙Back", callback_data="heroku"),
            InlineKeyboardButton("❌️Close", callback_data="Tiyaan_bots")
            ]]
    
        reply_markup = InlineKeyboardMarkup(buttons)

        await update.message.edit_text(
            """<b>➪ Bot Name</b> AutoCaptionBot\n\n➪ <b>Framework : Pyrogram</b>\n\n➪<b> Language : Python</b>\n\n➪<b> Server : Koyeb</b> \n\n<b>➪ Version : 1.0.0</b>\n\n<b>➪ Source Code  : <a href="https://t.me/Tiyaan_bots">Touch Me 🤗</a>\n\n➪ Developer :  @Sreehari3\n</a></b>""",
            reply_markup=reply_markup,
            parse_mode="html"
        )

    elif query_data == "Tiyaan_bots":
        await update.message.delete()
