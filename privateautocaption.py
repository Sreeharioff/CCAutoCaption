# MRKT TECH

import os
import logging
import pyrogram
from aiohttp import web
from mt_privateautocaption import web_server
from config import Config, PORT


if __name__ == "__main__" :
    plugins = dict(
        root="mt_privateautocaption"
    )
    MRKTTECH = pyrogram.Client(
        "CaptionBot",
        bot_token=Config.MRKT_BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workers=300
    )
    app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()
        
    MRKTTECH.run()
