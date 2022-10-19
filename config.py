import os


class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5682981728:AAEbr-VF2ZMwlmyoe-pFlsPBZE4XYmMY5E8")

    APP_ID = int(os.environ.get("APP_ID", 10247139))

    API_HASH = os.environ.get("API_HASH", "96b46175824223a33737657ab943fd6a")

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001763515187")
