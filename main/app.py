from flask import Flask
from flask_discord_interactions import DiscordInteractions
from discord.discord import bp as discord_bp, build_discord_routes
from .blog import blog
from .config import Config
from devtools import debug

discord = DiscordInteractions()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    if not app.config.get('SITE_MODE'):
        discord.init_app(app)
        with app.app_context():
            discord.register_blueprint(discord_bp, app)
            build_discord_routes(discord, app)
    app.register_blueprint(blog)
    return app
