# <C> MrktTech


import os

class Config(object):
    MRKT_BOT_TOKEN = os.environ.get("MRKT_BOT_TOKEN", "")
    API_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    CAPTION = os.environ.get("CAPTION", " Join : @CinemaCompanyMovie")
    BUTTON_TEXT = os.environ.get("BUTTON", "🔻Join Channel🔻")
    URL_LINK = os.environ.get("LINK", "T.ME/Tiyaan_bots")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    PORT = os.environ.get("PORT", "8080")
