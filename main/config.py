import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '../.env'))


class Config(object):
    DISCORD_CLIENT_ID = os.getenv("DISCORD_CLIENT_ID")
    DISCORD_PUBLIC_KEY = os.getenv("DISCORD_PUBLIC_KEY")
    DISCORD_CLIENT_SECRET = os.getenv("DISCORD_CLIENT_SECRET")
    TESTING_GUILD = os.getenv("TESTING_GUILD")
    DEBUG_MODE = os.getenv("DEBUG_MODE")
    SITE_MODE = os.getenv("SITE_MODE") or False
