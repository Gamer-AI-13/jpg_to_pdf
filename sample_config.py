import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    # custom file name with .pdf extintion
    FILE_NAME = os.environ.get("FILE_NAME", "@imagetopdf_byAI_bot.pdf")
